from wordcloud import WordCloud
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

text = open('../souse/alice.txt').read()

# 예외하는 문자 추가하기
STOPWORDS.add('said')
STOPWORDS.add('Alice')
print('STOPWORDS:', STOPWORDS)
img_mask = np.array(Image.open('../souse/cloud.png'))
wordcloud = WordCloud(width=400, height=400,
background_color="white", max_font_size=200,
stopwords=STOPWORDS,

repeat=True,
colormap='inferno', mask=img_mask).generate(text)

# words_: 객체의 비율 정보가 담긴 딕셔너리 반환
print(wordcloud.words_)
plt.figure(figsize=(10, 8))
plt.axis('off')
plt.imshow(wordcloud)
plt.show()