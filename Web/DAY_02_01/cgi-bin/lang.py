# 기준 경로 : DAY_02_01/cgi-bin

# 모듈 로딩
import cgi, sys, codecs, os, datetime
import cgitb
import torch
import pickle
import torch.nn as nn
from konlpy.tag import Mecab

# 에러 확인
cgitb.enable()  # Error 확인

# Web 인코딩 설정
sys.stdout = codecs.getwriter(encoding='utf-8')(sys.stdout.detach())

# 요청 처리 및 브라우징
# Client 요청 데이터 즉, Form 데이터 저장 인스턴스
form = cgi.FieldStorage()


# Web 브라우저 화면 출력 코드

filepath = '../HTML/lang.html'

def print_html(filename, data = '', pre = ''):
    # HTML 파일 읽기 => body 문자열
    with open(filename, 'r', encoding='utf-8') as f:
    
        # HTML Header
        print('Content-Type : text/html; charset = utf-8')
        print()  # 무조건 한줄 띄어야 함

        # HTML Body
        body = f.read().format(data, pre)
        print(body)

# 모델 클래스 정의

class TextModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_size, num_class):
        super(TextModel, self).__init__()
        self.embedding = nn.EmbeddingBag(vocab_size, embedding_dim, sparse=False)
        self.rnn = nn.GRU(embedding_dim, hidden_size, 1, batch_first=True)
        self.dropout = nn.Dropout(p=0.2)  # 드롭아웃 레이어 추가
        self.fc = nn.Linear(hidden_size, num_class)
        self.init_weights()

    def init_weights(self):
        initrange = 0.5
        self.embedding.weight.data.uniform_(-initrange, initrange)
        self.fc.weight.data.uniform_(-initrange, initrange)
        self.fc.bias.data.zero_()

    def forward(self, text, offsets):
        embedded = self.embedding(text, offsets)
        output, hidden = self.rnn(embedded)
        output = self.dropout(output) 
        return self.fc(output)

# 어휘사전 생성

def load_vocab(file_path):
    with open(file_path, 'rb') as f:  
        vocab = pickle.load(f)
    return vocab

vocab = load_vocab('model/vocab_tk.pkl')

# 모델 생성

mecab = Mecab()

model = torch.load('model/model_tkLang.pt')

def predict(model, text):
    text_pipeline = lambda x: vocab(x)
    with torch.no_grad():
        text = torch.tensor(text_pipeline(mecab.morphs(text)), dtype=torch.int64)
        offsets = torch.tensor([0])
        output = model(text, offsets)
        sigmoid = nn.Sigmoid()
        pre = sigmoid(output).item() 
        if pre >= 0.7: 
            result = '경상도 사투리'
        else:
            result = '표준말'
    return result


# 데이터 추출 / 예측 함수 실행
if 'text' in form:
    text = form.getvalue('text')
    result = predict(model, text)
else:
    result = "No Data"


# 브라우징 : 함수 실행
print_html(filepath, result)
