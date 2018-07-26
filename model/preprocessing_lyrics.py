
import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.util import ngrams
import lda
from sklearn.feature_extraction.text import CountVectorizer


# data load ------------------------------------------------------------------------

pop_data = pd.read_csv(r"C:\Users\User\Desktop\music\data\lyrics\lyrics_data.csv",names=['Title','Singer','Lyrics'],encoding='cp949')
pop_data2 = pd.read_csv(r"C:\Users\User\Desktop\music\data\lyrics\lyrics_data2.csv",names=['Title','Singer','Lyrics'],encoding='cp949')
fork_data = pd.read_csv(r"C:\Users\User\Desktop\music\data\lyrics\fork_lyrics_data.csv",names=['Title','Singer','Lyrics'],encoding='cp949')
randb_data = pd.read_csv(r"C:\Users\User\Desktop\music\data\lyrics\randb_lyrics_data.csv",names=['Title','Singer','Lyrics'],encoding='cp949')
rock_data = pd.read_csv(r"C:\Users\User\Desktop\music\data\lyrics\rock_lyrics_data.csv",names=['Title','Singer','Lyrics'],encoding='cp949')


# merge ------------------------------------------------------------------------

lyric_data = pd.concat((pop_data,pop_data2,fork_data,randb_data,rock_data),axis=0)
lyric_data.index=range(len(lyric_data))

# lyrics ------------------------------------------------------------------------

lyric = [lyric_data['Lyrics'][i] for i in range(len(lyric_data))]


# remove stop_words ---------------------------------------------------------------------
def eli_stop(string, stop_word, rlc = ''):
    for sw in stop_word:
        string= string.replace(sw, rlc)
    return string

eli = ['(',')','....','?','...','&','$','-']
words = [eli_stop(sent,eli) for sent in lyric]

# tokenize pop ------------------------------------------------------------------------
# gram_word ---------------------------------------------------------------------------

song_word = [i.split() for i in lyric]

gram_list = []
for i in song_word:
    gram_list.append([i[l] for l in range(len(i)) if len(i[l])>3])

gram_list2 = []
for i in gram_list:
    gram_list2.append([i[l] for l in range(len(i)) if len(i[l])<15])


# stemming ------------------------------------------------------------------------

lemma = nltk.wordnet.WordNetLemmatizer()
stem_words = []
for word in gram_list2:
    stem_words.append([lemma.lemmatize(word[i]) for i in range(len(word))])

# remove stopwords ---------------------------------------------------------------------

pop_ly_list=np.unique(stem_words).tolist()

stop = ['man', 'pack', 'high', 'hmmm', 'door', 'everybody', 'yesterday', 'look', 'bounce', 'shake', 'tentaci³n', 'qu', 'peekaboo', 'people', 'house', 'with', 'time', 'cold', 'mind', 'talk', 'fire', 'tonight', 'nobody', 'coraz³n', 'year', 'reason', 'eligi³', 'work', 'throw', 'Uh', 'damn', 'wanna', 'girl', 'cris', 'tommorow', 'count', 'hold', 'let', 'pussy', 'ride', 'stay', '*NSYNC', 'thing', 'floor', 'you', 'woman', 'body', 'yeah', 'fall', 'daddy', 'push', 'gonna', 'someone', 'hand', 'dprimante', 'as\xad', 'keep', 'name', 'gotta', 'nothing', "t'as", 'show', 'turn', 'boy', 'this', 'world', "T'es", 'when', 'game', 've', 'money', 'morning', 'type', 'nigga', 'point', 'bitch', 'Vas-y', 'come', 'gches', 'imagin', 'rise', 'vida', 'shit', 'gar§ons', 'miss', 'please', 'call', 'give', 'dfonc', 'chance', 'tomorrow', 'secoue-toi', 'cause', 'play', 'say', 'yours', 'bring', 'nami', 'something', 'Aye', 'anything', 'watch', 'fuck', 'donna', 'baby', 'lady', 'place', 'flech³', 'tell', 'phone', 'somebody', 'rveilles', "c'est", 'Ros', 'home', 'trap', 'oooh', 'Como', 'word', 'mine', 'everything', 'your', 'll', 'it', 'we', 'p¨re', 'everyone', 'ooh', 'rockabye', 'today', 'mama', 'wild', 'day', 'feel', 'city', 'pas?³', 'that', 'nothin', 'clap', 'matter', 'back', 'know', 'night', 'life', 'make', 'dont', 'ten\xadas', "Qu'estce", 'Baby', 'heart', 'al', 'whoa', 'rock', 'hell', 'take', 'tryin', 'eye', 'want', 'brother', 'boom', 'roll', 'hallelujah', 'woah', 'level', 'hello', 'knock', 'funk', 'living', 'stop', 'summer', 'like', 'well', 'live', 'like', 'ready', 'save', 'long', 'pull', 'through','ohhh','bout', 'head', 'number', 'blue', 'gold', 'hair', 'hand', 'water', 'right', 'killing']

final_word=[]
for fi_word in stem_words:
    final_word.append([i for i in fi_word if i not in stop])


postag_word = [nltk.pos_tag(i) for i in final_word]

use_word = []
for out in postag_word:
    use_word .append([si[0] for si in out if (si[1] == 'NN')|(si[1] == 'NNS')|(si[1] == 'NNP')|(si[1] == 'NNPS')])

# bi-gram_word -------------------------------------------------------------------------
bi_gram = [list(ngrams(i,2)) for i in gram_list2]


bi_gram_word=[]
for i in bi_gram:
    bi_gram_word.append([str(a[0])+' '+str(a[1]) for a in i])



# stemming
lemma = nltk.wordnet.WordNetLemmatizer()

stem_bi_gram = []
for word in bi_gram_word:
    stem_bi_gram.append([lemma.lemmatize(word[i]) for i in range(len(word))])

# remove stopwords

pop_ly_list2=np.unique(stem_bi_gram).tolist()

eli = ['(',')','....','?','...','&','$','-']
bi_words = []
for i in stem_bi_gram:
    bi_words.append([eli_stop(i[sent],eli) for sent in range(len(i))])



# merge use words ------------------------------------------

use_word = pd.DataFrame(use_word)
use_bi_gram = pd.DataFrame(bi_words)


final_use_word = pd.concat((use_word,use_bi_gram),axis=1)
final_use_word = final_use_word.values.tolist()

final_text = []
for i in final_use_word:
    final_text.append([i[a] for a in range(len(i)) if i[a] != None])



# vocabulary -------------------------------------------------------------------
voca = [i for j in final_text for i in j]

# lda modelling ------------------------------------------------------------------------------

final_sent = [" ".join(i) for i in final_text]

c_vectorizer=CountVectorizer(analyzer='word',vocabulary=list(set(voca)))
count=c_vectorizer.fit_transform(final_sent)
topic_vocab=c_vectorizer.get_feature_names()
titles = lyric_data['Title']

model=lda.LDA(n_topics=5,n_iter=300,random_state=1)
model.fit(count)


topic_word=model.topic_word_
n_top_words=10

topic_list = []
for i, topic_dist in enumerate(topic_word):
    print('Topic',i ,topic_dist)
    topic_words=np.array(topic_vocab)[np.argsort(topic_dist)][:-n_top_words:-1]
    print('Topic', i ,topic_words)
    topic_list.append(topic_words)


doc_topic = model.doc_topic_
print("type(doc_topic): {}".format(type(doc_topic)))
print("shape: {}".format(doc_topic.shape))

topic_list = pd.DataFrame(topic_list)
topic_list['Topic'] = ['love','music','party','nature','breakup']

lda_topic_mat = pd.DataFrame(doc_topic)
lda_topic_mat.columns = topic_list['Topic']


