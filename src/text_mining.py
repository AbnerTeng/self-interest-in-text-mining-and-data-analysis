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

class word_cloud():
    def import_text(self):
        self.text = "kklab, being a technology venture, collaborates with our partners to turn ideas into products using leading edge technologies. KKLab so far has two AI products to offer: KKRaaS and Lyricist.ai. KKRaaS is a B2B generic recommendation platform while Lyricist.ai is a lyrics generator. There are many more AI related projects in incubation.We are seeking a talented machine learning engineer to build audio/music AI systems. This role will be working with other machine learning engineers to develop algorithms ranging from audio/music analysis to audio/music generation. The algorithm has to strike a perfect balance between computation efficiency and model accuracy.We are looking for a candidate who is self-motivated with machine learning knowledge and passionate about engineering excellence.Responsibility Working with cross-country stakeholders and teams to build a music AI system.Understand, modify, and implement state-of-the-art technologies in audio/music analysis and generation from academia into products.Understand and breakdown state-of-the-art models into reusable components and develop new models by using those reusable components.Understand qualitative feedback from human labellers and translate it into quantitative metrics.Build simple prototypes and demo sites for newly developed models.RequirementSolid understanding of various machine learning models and techniques in audio/music analysis and generation.( eg. DDSP-VST, Magenta, etc )Fluent with Python.Familiar with popular machine learning frameworks such as tensorflow, pytorch, scikit, etc.Understanding of music theory is a plus.Professional experience in music (band member, music critic) is a plus.Fluent in Mandarin (interview will be conducted in Mandarin)Interview processHiring manager / 15~30m / phoneTeam, bar raiser / 60~90m / Google MeetGM, hiring manager / 60~90m / Google Meet"
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
        plt.show()

if __name__ == '__main__':
    word_cloud = word_cloud()
    word_cloud.import_text()
    word_cloud.frequency()
    word_cloud.draw_wordcloud()


