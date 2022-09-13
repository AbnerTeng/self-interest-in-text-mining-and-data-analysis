# %%
from typing import Counter
import nltk

from nltk.corpus import treebank

nltk.download('treebank')
nltk.download('universal_tagset')
print(treebank.tagged_sents(tagset = "universal")[0])
# %%
from collections import defaultdict

POS_dict = defaultdict(dict)
for word_pos_pair in treebank.tagged_words(tagset = 'universal'):
    word = word_pos_pair[0].lower()  ## 小寫
    POS = word_pos_pair[1]
    POS_dict [word][POS] = POS_dict[word].get(POS, 0)+1

for word in list(POS_dict.keys())[900:1000]:
    if len(POS_dict[word]) > 1:
        print(word, POS_dict[word])
# %%
tagger_dict = {}
for word in POS_dict:
    tagger_dict[word] = max(POS_dict[word], key = lambda x: POS_dict[word][x])

def tag(sentences):
    return [(word, tagger_dict.get(word, "NN")) for word in sentences]  ##沒看過的字就標註成 NN

text = """I am currently a first-year graduate student with financial engineering major at NCCU. I have strong passion for data science, statistics, programming languages (Python, C++) and quantitative finance.""".split()
print(tag(text))
# %%
size = int(len(treebank.tagged_sents(tagset = "universal")) * 0.8)
train = treebank.tagged_sents(tagset = "universal")[:size]
test = treebank.tagged_sents(tagset = "universal")[size:]

from nltk import UnigramTagger

unigram_tagger = UnigramTagger(train)
print(unigram_tagger.evaluate(test))
# %%
## 嘗試處理一段 .html 文件
text_html = """
<body>
    <!-- JavaScript plugins (requires jQuery) -->
    <script src="http://code.jquery.com/jquery.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>

    <div class="container">
        <div class="page-header">
            <h3>About Me</h3>
        </div>
        <div class="page-info">

A web developer with experience in a variety of exciting projects, with the most up-to-date and relevant programming foundations available. My wide experience in
a diversity of technologies guides me with the best way to get your business success.
My interest in academic leads me to research in the field of NLP(Natural Language 
Processing). Other than the knowledge in CS/IT, I'm also a broad learner who loves 
to read each and every kind of books.
        </div>
    </div>
</body>
"""

## 透過正規劃化移除 html
import re

text_html = re.sub("<[^>]+>", "", text_html).strip()
print(text_html)
# %%
## 把跳行符號取代為空格
text_html = text_html.split("\n\n")[1].replace("\n", "" )
print(text_html)
# %%
## 把文件分割成句子
import nltk
nltk.download("punkt")
sent_segmenter = nltk.data.load('tokenizers/punkt/english.pickle')

sentences = sent_segmenter.tokenize(text_html)
print(sentences)
# %%
##把句子分割成單字
word_tokenizer = nltk.tokenize.regexp.WordPunctTokenizer()

tokenized_sentence = word_tokenizer.tokenize(sentences[0])
print(tokenized_sentence)
# %%
## 也可以把文件直接分割
word_tokenizer = nltk.tokenize.regexp.WordPunctTokenizer()

tokenized_text = word_tokenizer.tokenize(text_html)
print(tokenized_text)
# %%
## 正規化
nltk.download('omw-1.4')
nltk.download("wordnet")
lemmatizer = nltk.stem.wordnet.WordNetLemmatizer()

def lemmatize(word):
    lemma = lemmatizer.lemmatize(word, 'v')
    if lemma == word:
        lemma = lemmatizer.lemmatize(word, 'n')
    return lemma

print([lemmatize(token) for token in tokenized_sentence])
# %%
##定義 Counter
from nltk.probability import FreqDist
counter = FreqDist(tokenized_sentence)
counter = counter.most_common(10)
print(counter)
