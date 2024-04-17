from flask import Blueprint, render_template, request, url_for
import datetime
import os
import torch
import torchvision.transforms as transforms
from PIL import Image
import torch.nn as nn
import torch.nn.functional as F

class CNN32(nn.Module):
    def __init__(self):
        super(CNN32, self).__init__()

        self.conv1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1)
        self.bn1 = nn.BatchNorm2d(16)  # 배치 정규화 층 추가
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)

        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.bn2 = nn.BatchNorm2d(32)  # 배치 정규화 층 추가

        self.fc1 = nn.Linear(32 * 8 * 8, 32)
        self.fc2 = nn.Linear(32, 16)
        self.fc3 = nn.Linear(16, 6)  # 클래스의 수에 맞게 수정

        nn.init.kaiming_uniform_(self.conv1.weight)
        nn.init.kaiming_uniform_(self.conv2.weight)

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)  # 배치 정규화 적용
        x = F.relu(x)
        x = self.pool(x)  # 풀링 적용

        x = self.conv2(x)
        x = self.bn2(x)  # 배치 정규화 적용
        x = F.relu(x)
        x = self.pool(x)

        x = x.view(-1, 32 * 8 * 8)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.fc3(x)

        return x
model = CNN32()
model_path = os.path.join(os.getcwd(), 'ProjectWeb', 'static', 'model', 'movie_genre.pth')
model.load_state_dict(torch.load(model_path))
model.eval()  

# 블루프린트의 별칭, __name__, url_prefix
dataBP = Blueprint('project', 
                   __name__, 
                   url_prefix='/movie',
                   template_folder='templates')


## 라우팅 함수들
@dataBP.route('/')
def input_data():
    return render_template('input_data.html')



def predict_one(img_path):
    # 이미지 열기
    img = Image.open(img_path)
    
    # 이미지 채널 확인
    if img.mode != 'RGB':
        res = '예측 불가 : 이미지 파일의 채널이 맞지 않습니다.'
    else:
        # 전처리
        preprocessing = transforms.Compose([
            transforms.Resize((32, 32)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.38588074, 0.3442984, 0.32389283], std=[0.06522466, 0.06430584, 0.073496684])
        ])
        
        img = preprocessing(img)
        img = img.unsqueeze(0)
        
        # 모델 예측
        with torch.no_grad():
            output = model(img)
            _, preds = torch.max(output, 1)

        class_names = ['Action', 'Animation', 'Comedy&Drama', 'Horror', 'Romance', 'SF']
        res = class_names[preds]
    
    return res



@dataBP.route('/save/', methods=['POST'])
def save_data():

    i = request.files['img_file']
    print('-'*100)

    current_dir = os.getcwd()
    print(current_dir)
    suffix = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
    image_folder = os.path.join(current_dir, 'ProjectWeb', 'static', 'image')
    save_path = os.path.join(image_folder, f'{suffix}_{i.filename}')
    print(save_path)
    i.save(save_path)
    
    res = predict_one(save_path)
    img_path = url_for('static', filename=f'image/{suffix}_{i.filename}')

    return render_template('save_data.html', img_path=img_path, res=res)
