import cgi
import torch
import torch.nn as nn
import os

# form 태그 입력값 데이터 저장할 인스턴스
form = cgi.FieldStorage()

# 클라이언트의 요청 데이터 추출
if 'open' in form and 'high' in form and 'low' in form and 'volume' in form:
    open_value = form.getvalue('open')
    high_value = form.getvalue('high')
    low_value = form.getvalue('low')
    volume_value = form.getvalue('volume')
    
    # 입력값을 FloatTensor로 변환
    input_data = torch.FloatTensor([[float(open_value), float(high_value), float(low_value), float(volume_value)]]).unsqueeze(0)
else:
    input_data = None

# 모델 클래스 정의 및 로딩
class StockModel(nn.Module):
    def __init__(self):
        super(StockModel, self).__init__()
        self.rnn = nn.LSTM(5, 8, 3, batch_first=True)
        self.dropout = nn.Dropout(p=0.2)
        self.fc1 = nn.Linear(8, 1)
        self.relu = nn.ReLU()
        self.init_weights()

    def init_weights(self):
        initrange = 0.5
        nn.init.uniform_(self.rnn.weight_ih_l0, a=-initrange, b=initrange)
        nn.init.uniform_(self.rnn.weight_hh_l0, a=-initrange, b=initrange)
        nn.init.zeros_(self.rnn.bias_ih_l0)
        nn.init.zeros_(self.rnn.bias_hh_l0)
        nn.init.uniform_(self.fc1.weight, a=-initrange, b=initrange)
        nn.init.zeros_(self.fc1.bias)

    def forward(self, data):
        output, hidden = self.rnn(data)
        output = self.dropout(output)
        output = self.fc1(output[:, -1, :]) 
        output = self.relu(output)
        return output

file_dir = os.path.dirname(os.path.dirname(__file__))

model = torch.load(file_dir+'/model/stock_model.pt')
model.eval()

# # 모델 예측
if input_data is not None:
    prediction = model(input_data)
else:
    prediction = "입력값이 없습니다."

# 예측값 출력
print("Content-type: text/html; charset=utf-8\n")
print()
print(f'''
<center>
      <H1>Stock Regression</H1><hr color="blue" size="2">

      <h2>넣은 DATA</h2>
      <fieldset>

      <h3>Open : {open_value}</h2>
      <h3>High : {high_value}</h2>
      <h3>Low : {low_value}</h2>
      <h3>Volume : {volume_value}</h2>

      </fieldset>
      <h2>예측값</h2><br>
      <fieldset>
      <h3>{prediction.item()}</h2><br>
      </fieldset>

      </center>
      ''')

