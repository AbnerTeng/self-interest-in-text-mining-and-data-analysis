## Default WordCloud

import matplotlib.pyplot as plt
from wordcloud import WordCloud

## import other packages from wordcloud
from wordcloud import STOPWORDS, ImageColorGenerator
paragraph = open("paragraph.txt").read()
stopword = set(STOPWORDS)
wordcloud = WordCloud(width = 4000, height = 3000, stopwords = STOPWORDS, margin = 3,
                      background_color = "white", colormap = "Set3", max_words = 25,
                      min_font_size = 8).generate(paragraph)
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis("off")

## mandarin WordCloud
font_path = 'font file'
ch_paragraph = " ".join(string) ## string 是已經斷好詞的結果
ch_wordcloud = WordCloud(font_path = font_path, width = 4000, height = 3000, stopwords = STOPWORDS,
                         margin = 3, scale = 10, background_color = "white", min_font_size = 8, prefer_horizontal = 1
                         ).generate(ch_paragraph)
plt.figure(figsize = (20, 10))
plt.imshow(ch_wordcloud, interpolation = 'bilinear')
plt.axis("off")
