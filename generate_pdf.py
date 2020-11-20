from fpdf import FPDF



inicial="""Luego  de  realizar  un  análisis  de  cada  uno  de  los  términos  que  se  encuentran  al  interior  de las  distintas búsquedas hechas que las podría encontrar en:    
    
    file location: Keylogger/files/Busquedas.csv

se  han  detectado  5  tópicos  latentes  al  interior,  por  lo  tanto  dentro  de  cada  tópico  se  han  clasificado  los términos y su nivel de relevancia por cada uno, a continuación podrá evidenciar cual es el termino más relevante dentro del topico:
"""
medio= """Finalmente, luego de analizar cuál es la relevancia de cada tópico al interior de cada uno de las búsquedas, se logra detectar que el tópico relevante es: 
"""
final= """pdt: Recuerda que el topico dominante es aquel que predomina entre el conjunto de busquedas, este topico permite identificar cuales son los terminos de importancia  para ti, pues las palabras pertenecen a este son las que representan las busquedas que mas predominan en tu trabajador.
"""
def write_topics(model, feature_names,df_document_topic, top_n=5):  
  
    with open('files/texto.txt','w') as file:  #### This is the code to print the topics. top_n can be changed. 
        file.write(inicial)
        file.write("\nTopicos en el modelo LDA :")
        for topic_idx, topic in enumerate(model.components_):
            message = "\nTopico %d: " % topic_idx
            message += " ".join([feature_names[i] + " " + str(int(topic[i])) + " "
                                for i in topic.argsort()[:-top_n - 1:-1]])        
            print(message)
            file.write(message)
        print()
        file.write("\n\n\n"+medio)
        file.write("\n"+df_document_topic)
        file.write("\n\nPara  conocer  cuáles  son  el  listado  completo  de  términos  de  forma  interactiva,  accede  al  siguiente  archivo alojado en tu computadora: ")
        file.write("\n\n\n  file location: KeyLogger/files/graphics.html")
        
        file.write("\n\n\n"+final)


class PDF(FPDF):
    pass
    def logo(self,name,x,y,w,h):
        self.image(name,x,y,w,h)
    def texts(self,name):
        with open(name,'rb') as xy:
            txt=xy.read().decode('latin-1')
        self.set_xy(20.0,45.0)
        self.set_text_color(0,0,0)
        self.set_font('Arial','',12)
        
        self.multi_cell(160,5,txt,align='J')

    def sub_titles(self,title,x,y):
        self.set_xy(x,y)
        self.set_font('Arial','B',12)
        self.set_text_color(71,75,78)
        self.cell(w=210.0,h=10.0,align='c',txt=title,border=0)

    def titles(self,title):
        self.set_xy(0,0)
        self.set_font('Arial','B',18)
        self.set_text_color(0,0,0)
        self.cell(w=210.0,h=40.0,align='C',txt=title,border=0)

