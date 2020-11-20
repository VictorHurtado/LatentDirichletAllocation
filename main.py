
import csv
import pandas as pd
import numpy as np

########################
import Extraction as ex
import Model_Data as md
import generate_pdf as pdf


if __name__== "__main__":
   # os.system('python KeyLogger.py')
   # time.sleep(30)
   ex.extract('files/Busquedas.txt')
   datos= pd.read_csv('files/Busquedas.csv')
   if len(datos)>=20:

      print(datos)
      num_of_topics=5
      n_top_words = 5
      strings = datos.iloc[:,0]
      data = ex.format_text(strings)
      stop_words_es=md.extract_stopwords('files/stopword.txt')
      tf_vectorize_model= md.create_vectorize_model(stop_words_es)
      tf_vectorize= md.vectorize_searches(data,tf_vectorize_model)
      lda_aplication=md.apply_model_topic(num_of_topics,tf_vectorize)
      tf_feature_names = tf_vectorize_model.get_feature_names()
      md.print_topics(lda_aplication,tf_vectorize_model)
      
      md.create_graphics(lda_aplication,tf_vectorize,tf_vectorize_model)
      dominant_topic=md.detect_dominant_topic(lda_aplication,tf_vectorize,data)
    
      pdf.write_topics(lda_aplication,tf_feature_names,dominant_topic)
      pdf=pdf.PDF()
      pdf.add_page()
      pdf.logo('files/img/logo.png',5,5,50,30)
      pdf.texts('files/texto.txt')
      pdf.titles('Analisis de topicos.')
      pdf.sub_titles('Inteligencia Artificial USC - Cali',74.5,21.5)
      pdf.output('files/pdf_extract_file.pdf','F')
   else:
      print("\ncantidad insuficiente de busquedas")