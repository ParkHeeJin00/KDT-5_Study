import string
import re
from collections import Counter

def S_preprocess(sentences, stop_mode='k', short=False):
    """
    문장 단위일 때, 구두점 제거 / 정규표현식으로 남길 문자 선택
    stop_mode : 'k' (한글만), 'ke' (한글+영문), 'ken' (한글+영문+숫자)
    short : 문자열이 1,2개인 단어 제거 여부 (True or False)
    전처리된 문장들이 하나의 문자열로 반환
    """
    preprocessed_sentences = []
    for n, sentence in enumerate(sentences):
        # str.maketrans - 문자열의 번역 테이블을 만드는 함수
        # 첫 번째 인자는 바꾸고자 하는 문자들, 두 번째 인자는 바꿀 문자들, 세 번째 인자는 제거하고자 하는 문자들
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))  # 구두점 제거

        if stop_mode == 'k':
            sentence = re.sub(r'[^가-힣]', '', sentence)  # 한글만 남기기
        elif stop_mode == 'ke':
            sentence = re.sub(r'[^가-힣a-zA-Z]', '', sentence)  # 한글과 영문만 남기기
        elif stop_mode == 'ken':
            sentence = re.sub(r'[^가-힣a-zA-Z0-9]', '', sentence)  # 한글과 영문, 숫자만 남기기

        # 문자열이 1,2개인 단어 제거
        if short:
            shortword = re.compile(r'\b(\w{1,2})\b') # \w{1,2}
            sentence = sentence.translate(str.maketrans('', '', shortword))

        preprocessed_sentences.append(sentence.split())  # 문장을 단어 단위로 펼쳐서 리스트에 추가
        if n % 1000 == 0:
            print('.')

    return preprocessed_sentences

def T_remove_stopword(voca_dict):
    '''
    단어사전 만들고 난 후에,
    불용어 제거
    '''
    # 불용어 제거
    with open(r'C:\Users\kdp\KDT-5\KDT-5_Study\자연어\data\hangul_stopword.txt', 'r', encoding='utf-8') as file:
        stopword = [line.strip() for line in file.readlines()]
    for key in list(voca_dict.keys()):
        if key in stopword:
            del voca_dict[key]

def build_vocab(corpus, n_vocab, special_tokens):
    counter = Counter()

    # 단어/토큰에 대한 빈도수 계산
    for tokens in corpus:
        counter.update(tokens)
    # 단어/어휘 사전 생성
    vocab = special_tokens # list
    # 단어/어휘 사전에 빈도수가 높은 단어 추가
    for token, count in counter.most_common(n_vocab):   # .most_common(n) : n개의 빈도수 높은 단어 추출
        vocab.append(token)
        
    return vocab

