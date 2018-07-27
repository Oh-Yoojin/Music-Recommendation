
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from itertools import combinations

lda_topic = pd.read_csv(r"C:\Users\User\Desktop\music\data\lyrics\project\lda_topic.csv")
tfidf_mat = pd.read_csv(r"C:\Users\User\Desktop\music\data\lyrics\project\tfidf_mat.csv",encoding='cp949')
sentiment_score = pd.read_csv(r"C:\Users\User\Desktop\music\data\lyrics\project\sentiment_score.csv")
ful_data = pd.read_csv(r"C:\Users\User\Desktop\music\data\lyrics\project\total_lyric.csv",encoding='cp949')


# merge table -----------------------------------------------------------------

final_data = pd.concat((lda_topic,tfidf_mat,sentiment_score),axis=1)
final_data = final_data.drop(2485)


# pairwise_cosine_similarity -----------------------------------------------------------------

total_song_list = [str(ful_data.values[i][0])+'/'+str(ful_data.values[i][1]) for i in range(len(ful_data))]

final_data.index = total_song_list

pair = list(combinations(total_song_list,2))

cos_simi = []
for num in range(len(total_song_list)):
    cos_simi.append(cosine_similarity(final_data.ix[total_song_list[num]].values,final_data.values).tolist())
    print(num,len(total_song_list))

a=[]
for i in cos_simi:
    a.append(i[0])

lyric_similarity=pd.DataFrame(a)
lyric_similarity.index=total_song_list
lyric_similarity.columns=total_song_list


# compare similarity -----------------------------------------

last_fm_simi = pd.read_csv(r"C:\Users\User\Desktop\music\data\lyrics\project\similarity_data.csv",encoding='cp949')

# Chandelier/Sia

test1=last_fm_simi.ix[1].values[2:].tolist()
my_test1= np.argsort(lyric_similarity['Chandelier/Sia'])[::-1][:10]


# Shake It Off/Taylor Swift

test2=last_fm_simi.ix[14].values[2:].tolist()
my_test2= np.argsort(lyric_similarity['Shake It Off/Taylor Swift'])[::-1][:10]


# Uptown Girl/Westlife

test3=last_fm_simi.ix[30].values[2:].tolist()
my_test3= np.argsort(lyric_similarity['Uptown Girl/Westlife'])[::-1][:10]


# Let Her Go/Passenger

test4=last_fm_simi.ix[40].values[2:].tolist()
my_test4= np.argsort(lyric_similarity['Let Her Go/Passenger'])[::-1][:10]


# Piano Man/Billy Joel

test5=last_fm_simi.ix[100].values[2:].tolist()
my_test5= np.argsort(lyric_similarity['Piano Man/Billy Joel'])[::-1][:10]
