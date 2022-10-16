from cgitb import text
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud
import nltk
nltk.download('punkt')
nltk.download('stopwords')
import os
import nltk.corpus
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import os


class word_cloud():
    def load_data(self):
        self.fwd = os.path.abspath(os.path.join(os.getcwd(), ".."))
        self.file_path = self.fwd + "/datas/job_data.xlsx"
        self.data = pd.read_excel(self.file_path)
        return self.data

    def import_text(self):
        self.text = self.data['description'][4]
        self.stop_words = set(stopwords.words('english'))
        self.token = word_tokenize(self.text)

        self.filtered_words = [i for i in self.token if not i.lower() in self.stop_words]
        self.filtered_words = []

        for i in self.token:
            if i not in self.stop_words:
                self.filtered_words.append(i)

        self.wo_punc = [j for j in self.filtered_words if j.isalnum()]
        return self.wo_punc


    def frequency(self):
        from nltk.probability import FreqDist
        self.text_freq = FreqDist(self.wo_punc)
        self.text_freq = self.text_freq.most_common(10)
        return self.text_freq

    def draw_wordcloud(self):
        self.wo_punc = " ".join(self.wo_punc)

        self.wordcloud = WordCloud(width = 800, height = 600, background_color = 'white', min_font_size = 10).generate(self.wo_punc)
        plt.figure(figsize = (8, 8), facecolor = None)
        plt.imshow(self.wordcloud)
        plt.axis("off")
        plt.tight_layout(pad = 0)
        plt.savefig(self.fwd + "/figs/graph4.png")
        plt.show()
        

if __name__ == '__main__':
    word_cloud = word_cloud()
    word_cloud.load_data()
    word_cloud.import_text()
    word_cloud.frequency()
    word_cloud.draw_wordcloud()


