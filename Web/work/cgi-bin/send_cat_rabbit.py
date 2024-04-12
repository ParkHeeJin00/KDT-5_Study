# 모듈 로딩
import cgi, sys, codecs, os, datetime
import cgitb
import datetime
import torch
import pickle
import torch.nn as nn
import torch.nn.functional as F
from PIL import Image
from torchvision import transforms
import os

cgitb.enable()  # Error 확인

# Web 인코딩 설정
sys.stdout = codecs.getwriter(encoding='utf-8')(sys.stdout.detach())

# 웹페이지의 form태그 내의 input 태그 입력값 데이터 가져와서 객체에 저장하고 있는 인스턴스
form = cgi.FieldStorage()

# 클라이언트의 요청 데이터 추출
if 'img_file' in form and 'message' in form:
    fileitem = form['img_file']  # form.getvalues('img_file')

    # 서버에 이미지 파일 저장 --------------------------------
    img_file = fileitem.filename

    suffix = datetime.datetime.now().strftime('%y%m%d_%H%M%S')


    save_path = f'./image/{suffix}_{img_file}'
    with open(save_path, 'wb') as f:
        f.write(fileitem.file.read())
    # -------------------------------------------------------

    img_path = f'/image/{suffix}_{img_file}'

    # 예측 True값으로 이용
    msg = form.getvalue('message') 
else:
    img_path = 'None'
    msg = 'None'

# 모델 클래스 정의 및 로딩
class CNN(nn.Module):
    def __init__(self):
        
        super(CNN, self).__init__()       # in = 3
        self.conv1 = nn.Conv2d(in_channels = 3, out_channels = 8, kernel_size = 3, padding = 1) 
        self.conv2 = nn.Conv2d(in_channels = 8, out_channels = 16, kernel_size = 3, padding = 1) 
        self.pool = nn.MaxPool2d(kernel_size = 2, stride = 2)  
        self.fc1 = nn.Linear(8*8*16, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 1)  # out = 1
    
    def forward(self, x): # 32 * 32
        x = self.conv1(x)
        x = F.leaky_relu(x)
        x = self.pool(x) # 16 * 16
        x = self.conv2(x)
        x = F.leaky_relu(x)
        x = self.pool(x) # 8 * 8
        
        x = x.view(-1, 8*8*16)  # 이미지 수, 이미지 데이터
        x = self.fc1(x)
        x = F.leaky_relu(x)
        x = self.fc2(x)
        x = F.leaky_relu(x)
        x = self.fc3(x)
        # 이진분류니까 sigmoid 마지막에
        x = F.sigmoid(x)
    
        return x

file_dir = os.path.dirname(os.path.dirname(__file__))

model = torch.load(file_dir + '/model/cat_rabbit.pt')


# 모델을 이용하여 이미지 분류
meanR, meanG, meanB =  0.51141757, 0.49473807, 0.42908782
stdR, stdG, stdB = 0.05996415, 0.058366448, 0.06198036

def predict_one(filename, true):
    # 이미지 열기

    img = Image.open(file_dir+filename)
    
    # BGR을 RGB로 변환
    img = img.convert('RGB')
    
    prepro = transforms.Compose([
        transforms.Resize((32, 32)),
        # ToTensor() -> 0~1의 값으로 정규화
        transforms.ToTensor(),
        # 각 채널의 평균과 표준편차 값으로 정규화
        transforms.Normalize(mean=[meanR, meanG, meanB], std=[stdR, stdG, stdB])
    ])
    
    # 이미지 정규화 및 텐서 변환
    test_img = prepro(img)

    model.eval()
    with torch.no_grad():
        per = model(test_img.unsqueeze(0))
    pre = torch.round(per).item()  # 텐서를 스칼라 값으로 변환
    
    if pre == 1:
        pre = 'rabbit'
    else:
        pre = 'cat' 

    if true == pre:
        res = '예측 성공!'
    else:
        res = '예측 실패..'
    ment = f'{per.item():.2f}% 확률로 {pre}입니다.'
    return res, ment

# 이미지 분류 결과
res, ment = predict_one(img_path, msg)
# 요청에 대한 응답 HTML
# HTML Header
print('Content-Type : text/html; charset=utf-8') # 한글 깨짐 방지 charset = utf-8
print()  # 무조건 한줄 띄어야 함

# HTML Body
print('<TITLE>Cat Rabbit Classify</TITLE>')
print(f'''
<center>
      <H1>Cat Rabbit Clssify</H1><hr color="pink" size="2">
      <img src = {img_path}><br>

      <h2>{res}</h2><br>
      <h2>{msg}</h2><br>
      <h3>{ment}</h3>

      </center>
      ''')
