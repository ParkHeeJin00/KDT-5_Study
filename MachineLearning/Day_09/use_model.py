## -------------------------------------------------------------------
## 모델을 활용한 서비스 제공
## -------------------------------------------------------------------

# 모듈 로딩
from joblib import load
import numpy as np

# 전역 변수
model_file = '../model/iris_dt.pkl'

# 모델 로딩
model = load(model_file)

# 로딩된 모델 확인
print(model.classes_)

# 붓꽃 정보 입력 => 4개 피쳐
datas = input('붓꽃의 꽃받침길이, 꽃받침너비, 꽃잎길이, 꽃잎너비 입력: ')
if len(datas):
    datas_list = list(map(float,datas.split(',')))  # map의 반환값 : map 객체 -> list로 형변환
    print(datas_list)
    if len(datas_list) != 4:
        print('입력된 정보가 올바르지 않습니다.')
    else:
        # 입력된 정보에 해당하는 품종 알려주기
        # 모델의 predict(2D)
        pre_iris = model.predict([datas_list])[0]
        probas = model.predict_proba([datas_list])[0]
        max_proba_index = np.argmax(probas)
        pre_iris_per = probas[max_proba_index]
        print(f'해당 꽃이 {pre_iris}일 확률은 {pre_iris_per}%입니다.')
else:
    print('입력된 정보가 없습니다.')
