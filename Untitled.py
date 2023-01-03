#!/usr/bin/env python
# coding: utf-8

# # *Import Library*

# In[323]:


import pandas as pd
import numpy as np
import string


# # Data Loading

# In[322]:


detail=pd.read_csv('Hotel_details.csv')
atribut=pd.read_csv('Hotel_Room_attributes.csv')


# In[324]:


detail


# In[329]:


atribut


# # Exploratory Data Analysis

# In[325]:


del detail['id']
del detail['zipcode']


# In[326]:


detail.isnull().sum()


# In[327]:


detail.dropna(inplace=True)


# In[328]:


detail.drop_duplicates(subset='hotelid',keep=False,inplace=True)


# In[330]:


del atribut['id']


# In[331]:


atribut.isnull().sum()


# In[333]:


atribut=atribut.dropna()


# In[334]:


hotel=pd.merge(atribut,detail,left_on='hotelcode',right_on='hotelid',how='inner')


# In[335]:


hotel


# In[336]:


del hotel['hotelid']
del hotel['url']
del hotel['curr']
del hotel['Source']


# In[337]:


hotel=hotel[['hotelcode','hotelname','roomtype','starrating']]


# In[338]:


hotel.drop_duplicates(subset='hotelcode',keep='first',inplace=True)


# In[339]:


hotel


# In[340]:


hotel['roomtype']


# In[120]:


hotel.roomtype.unique()


# # Data Preparation

# In[140]:


string.punctuation


# In[341]:


def text_proses(teks):
    roomtype=[char for char in teks if char not in string.punctuation] #menghapus text yang berisi string punctation
    return''.join(roomtype)


# In[342]:


hotel['roomtype']=hotel['roomtype'].apply(text_proses)


# In[343]:


hotel['roomtype']=hotel['roomtype'].str.lower()


# In[156]:


hotel['roomtype']=hotel['roomtype'].str.replace(" ","_")


# In[226]:


hotel=hotel.reset_index(drop=True)


# In[227]:


hotel.head(25)


# In[158]:


tiperoom=np.sort(hotel.roomtype.unique())
for i in tiperoom:
    print(i)


# # Modeling and result

# In[159]:


from sklearn.feature_extraction.text import TfidfVectorizer
tf=TfidfVectorizer()
tf.fit(hotel['roomtype'])


# In[160]:


tf.get_feature_names()


# In[221]:


tfidf_matrix=tf.fit_transform(hotel['roomtype'])
tfidf_matrix.shape


# In[162]:


tfidf_matrix.todense()


# In[222]:


pd.DataFrame(
    tfidf_matrix.todense(), 
    columns=tf.get_feature_names(),
    index=hotel.hotelname
).sample(22, axis=1).sample(10, axis=0)


# In[228]:



from sklearn.metrics.pairwise import cosine_similarity

cosine_sim = cosine_similarity(tfidf_matrix,tfidf_matrix) 
cosine_sim
     


# In[229]:


cosine_sim_df = pd.DataFrame(cosine_sim, index=hotel['hotelname'], columns=hotel['roomtype'])
print('Shape:', cosine_sim_df.shape)
 
cosine_sim_df.sample(5, axis=1).sample(10, axis=0)
     


# In[230]:


indices=pd.Series(hotel.hotelname)
indices[:20]


# In[249]:


idx=indices[indices=='Apollo Hotel London'].index[0]
idx


# In[250]:


closest = pd.Series(cosine_sim[idx]).sort_values(ascending=False)
closest


# In[251]:


top_k_indexes=list(closest.iloc[0:6].index)
top_k_indexes


# In[236]:


hotel.hotelname[10]


# In[243]:


recomendatioan_hotel=[]
recomendatioan_hotel_roomtype=[]
for i in top_k_indexes:
    print(hotel.hotelname.iloc[i])


# # Recommendation

# In[317]:


def recomendation(nama, similarity_data=cosine_sim,k=9):
    print("TOP 10 Rekomendasi Buku")
    recomendatioan_hotel=[]
    recomendatioan_hotel_roomtype=[]
    recomendatioan_rate=[]
    idx=indices[indices==nama].index[0]
    
    
    closest = pd.Series(similarity_data[idx]).sort_values(ascending=False)
    top_k_indexes=list(closest.iloc[0:k+1].index)
    for i in top_k_indexes:
        recomendatioan_hotel.append(hotel.hotelname.iloc[i])
        recomendatioan_hotel_roomtype.append(hotel.roomtype.iloc[i])
        recomendatioan_rate.append(hotel.starrating.iloc[i])
    return pd.DataFrame(
        {
            'Hotelname':recomendatioan_hotel,
            'Roomtype':recomendatioan_hotel_roomtype,
            'Starrating': recomendatioan_rate
        })


# In[214]:


hotel[['roomtype','hotelname']].groupby('roomtype').count()


# In[215]:


hotel[hotel[r'roomtype']=='1_bedroom']


# In[246]:


hotel[hotel['hotelname']=="The Old Cider House"]


# In[188]:


hotel


# In[318]:


recomendation('Apollo Hotel London')


# In[297]:


recommended_hotel = recomendation('Apollo Hotel London')
recommended_hotel['Starrating'].sort_values()


# In[290]:


recommended_hotel.sort_values(['Starrating'],ascending=False)


# # Metrics Evaluation Using Rating

# In[301]:


k=10
threshold=3
hotel_starrating=recommended_hotel['Starrating'].values
hotel_relevant=hotel_starrating>=threshold
precision = len(hotel_starrating[hotel_relevant]) / k
print(f'The precision of the recommendation system is {precision:.1%}')


# In[313]:


hotel_roomtype=recommended_hotel['Roomtype'].values


# In[314]:


threshold='standard_triple_room'
hotel_roomtype==threshold


# In[312]:


recommended_hotel['Roomtype']


# # Metrics Evaluation Using Roomtype

# In[316]:


k=10
threshold='standard_triple_room'
hotel_roomtype=recommended_hotel['Roomtype'].values
hotel_relevant=hotel_roomtype==threshold
precision = len(hotel_roomtype[hotel_relevant]) / k
print(f'The precision of the recommendation system is {precision:.1%}')

