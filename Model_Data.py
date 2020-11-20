import pandas as pd

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.decomposition import LatentDirichletAllocation

import pyLDAvis
import pyLDAvis.sklearn

import Extraction as ex

def extract_stopwords(path):
    stop_words = np.genfromtxt(path, dtype='str')
    stop_words = ex.format_text(pd.Series(stop_words))
    stop_words = list(map(lambda x: x, stop_words))
    return stop_words
#imprimiendo topicos 
def print_topics(model, vectorizer, top_n=5):    
    print("\nTopics in LDA model:")
    for idx, topic in enumerate(model.components_):
        print("Topic %d:" % (idx))
        print([(vectorizer.get_feature_names()[i], topic[i])for i in topic.argsort()[:-top_n - 1:-1]])

def create_vectorize_model(stop_words_es):
    tf_vectorizer = CountVectorizer(min_df=2, max_features=50, stop_words=stop_words_es)
    return tf_vectorizer

def vectorize_searches(strings,model_vectorize):
    data = ex.format_text(strings)
    dtm_tf = model_vectorize.fit_transform(data)
    return dtm_tf

def apply_model_topic(n_topics,vectorize):
    lda = LatentDirichletAllocation(n_components=n_topics, max_iter=100,learning_method='online',learning_offset=10,batch_size=10,random_state=1)
    lda.fit(vectorize) 
    return lda

def create_graphics(lda,vectorize,vectorize_model):
    p=pyLDAvis.sklearn.prepare(lda, vectorize, vectorize_model)
    pyLDAvis.save_html(p,'files/graphics.html')

def getVectorizer_Features_Name(tf_vectorize):
    return tf_vectorize.get_feature_names()

def detect_dominant_topic(lda_aplication,tf_vectorize,data):
    lda_output= lda_aplication.transform(tf_vectorize)
    topicnames = ["Topic " + str(i) for i in range(lda_aplication.n_components)]
    docnames = ["Doc " + str(i) for i in range(len(data))]
    df_document_topic = pd.DataFrame(np.round(lda_output,2), columns=topicnames, index=docnames)

    dominant_topic = np.argmax(df_document_topic.values, axis=1)
    df_document_topic['dominant_topic'] = dominant_topic
    print("Dominante: Topic- %s"%df_document_topic['dominant_topic'].value_counts().idxmax())
    return "Dominante: Topico- %s"%df_document_topic['dominant_topic'].value_counts().idxmax()


    
