
import numpy as np
import pandas as pd
import nltk
from nltk.util import ngrams
from sklearn.feature_extraction.text import TfidfVectorizer


# data load

lyric_data = pd.read_csv(r"C:\Users\User\Desktop\music\data\lyrics\project\total_lyric.csv",encoding='cp949')


# lyrics

lyric = [lyric_data['Lyrics'][i] for i in range(len(lyric_data))]



# remove stop_words
def eli_stop(string, stop_word, rlc = ''):
    for sw in stop_word:
        string= string.replace(sw, rlc)
    return string

# tokenize pop -----------------------------
eli = ['(',')','....','?','...','&','$','-']
words = [eli_stop(sent,eli) for sent in lyric]

song_word = [i.split() for i in words]

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

stop = ['man', 'pack', 'high', 'hmmm', 'door', 'everybody', 'yesterday', 'look', 'bounce', 'shake', 'tentaci³n', 'qu', 'peekaboo', 'people', 'house', 'with', 'time', 'cold', 'mind', 'talk', 'fire', 'tonight', 'nobody', 'coraz³n', 'year', 'reason', 'eligi³', 'work', 'throw', 'Uh', 'damn', 'wanna', 'girl', 'cris', 'tommorow', 'count', 'hold', 'let', 'pussy', 'ride', 'stay', '*NSYNC', 'thing', 'floor', 'you', 'woman', 'body', 'yeah', 'fall', 'daddy', 'push', 'gonna', 'someone', 'hand', 'dprimante', 'as\xad', 'keep', 'name', 'gotta', 'nothing', "t'as", 'show', 'turn', 'boy', 'this', 'world', "T'es", 'when', 'game', 've', 'money', 'morning', 'type', 'nigga', 'point', 'bitch', 'Vas-y', 'come', 'gches', 'imagin', 'rise', 'vida', 'shit', 'gar§ons', 'miss', 'please', 'call', 'give', 'dfonc', 'chance', 'tomorrow', 'secoue-toi', 'cause', 'play', 'say', 'yours', 'bring', 'nami', 'something', 'Aye', 'anything', 'watch', 'fuck', 'donna', 'baby', 'lady', 'place', 'flech³', 'tell', 'phone', 'somebody', 'rveilles', "c'est", 'Ros', 'home', 'trap', 'oooh', 'Como', 'word', 'mine', 'everything', 'your', 'll', 'it', 'we', 'p¨re', 'everyone', 'ooh', 'rockabye', 'today', 'mama', 'wild', 'day', 'feel', 'city', 'pas³', 'that', 'nothin', 'clap', 'matter', 'back', 'know', 'night', 'life', 'make', 'dont', 'ten\xadas', "Qu'estce", 'Baby', 'heart', 'al', 'whoa', 'rock', 'hell', 'take', 'tryin', 'eye', 'want', 'brother', 'boom', 'roll', 'hallelujah', 'woah', 'level', 'hello', 'knock', 'funk', 'living', 'stop', 'summer', 'like', 'well', 'live', 'like', 'ready', 'save', 'long', 'pull', 'through','ohhh','bout', 'head', 'number', 'blue', 'gold', 'hair', 'hand', 'water', 'right', 'killing','mymymy','aaaah','aaah','aaanimal','aah','aall','fuking', 'fukup', 'fufufucking', 'jjjust', 'just', 'knoooooooow', 'ooohh', 'oooo', 'oooooh','ooooooooh', 'oozing', 'ooh', 'oohooh', 'oooh', 'meee', 'meeeeee', 'mmmm', 'mmhmm', 'mmmmmaybe', 'mmmmmm', 'naaaaahhhhhh', 'naaah', 'aaaaah']


final_word=[]
for fi_word in stem_words:
    final_word.append([i for i in fi_word if i not in stop])


postag_word = [nltk.pos_tag(i) for i in final_word]


use_tfidf = []
for out in postag_word:
    use_tfidf .append([si[0] for si in out if (si[1] == 'JJ')|(si[1] == 'JJR')|(si[1] == 'JJS')|(si[1] == 'VB')|(si[1] == 'VBD')|(si[1] == 'VBG')|(si[1] == 'VBN')|(si[1] == 'NN')|(si[1] == 'NNS')|(si[1] == 'NNP')|(si[1] == 'NNPS')])

final_tfidf_sent = [" ".join(i) for i in use_tfidf]

pop_ly_list3=np.unique(final_tfidf_sent).tolist()

wowo = [i for j in use_tfidf for i in j]

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(final_tfidf_sent)
pop_column_name = vectorizer.get_feature_names()

tfidf_mat = pd.DataFrame(tfidf.A, columns=pop_column_name)




# sentiment score ------------------------------------------------------------------------
# Use 'Emolex' sentiment vocab

postag_senti = [nltk.pos_tag(i) for i in final_word]

use_senti = []
for out in postag_senti:
    use_senti .append([si[0] for si in out if (si[1] == 'JJ')|(si[1] == 'JJR')|(si[1] == 'JJS')|(si[1] == 'VB')|(si[1] == 'VBD')|(si[1] == 'VBG')|(si[1] == 'VBN')])


senti = pd.read_table(r"C:\Users\User\Desktop\music\data\lyrics\project\emolex_score.txt",names=['word','senti_class','senti_score'])

senti = senti.pivot(index='word',columns='senti_class',values='senti_score')

senti_cls=['senti_anger','senti_anticipation','senti_disgust','senti_fear','senti_joy','senti_negative','senti_positive','senti_sadness','senti_surprise','senti_trust']


senti_count = []
for pop_song in use_senti:
    count=[]
    for i in range(len(pop_song)):
        if pop_song[i] in senti.index:
            count += [senti.ix[pop_song[i]].tolist()]
    count=pd.DataFrame(count)
    sum_li = count.sum(axis=0).tolist()
    senti_count.append(sum_li)

senti_score = pd.DataFrame(senti_count)
senti_score.columns=senti_cls

for n in range(len(senti_score)):
    for a in range(len(senti_score.values[n])):
        if str(senti_score.values[n][a]) == 'nan':
            senti_score.values[n][a] = 0

for n in range(len(senti_score)):
    for a in range(len(senti_score.values[n])):
        if senti_score.values[n][a] == 0:
            pass
        else:
            senti_score.values[n][a]=senti_score.values[n][a]/sum(senti_score.values[n])




