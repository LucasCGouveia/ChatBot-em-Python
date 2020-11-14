
# Etapa 4: Entendimento TF-IDF (Term frequency - inverse document frequency)

from sklearn.feature_extraction.text import TfidfVectorizer

frases_teste = lista_sentencas_preprocessada[:3]
frases_teste

frases_teste.append(frases_teste[0])
frases_teste

vetores_palavras = TfidfVectorizer()
palavras_vetorizadas = vetores_palavras.fit_transform(frases_teste)

type(palavras_vetorizadas) 
#scipy.sparse.csr.csr_matrix

palavras_vetorizadas

#<4x76 sparse matrix of type '<class 'numpy.float64'>'
#	with 113 stored elements in Compressed Sparse Row format>

print(vetores_palavras.get_feature_names())

len(vetores_palavras.get_feature_names())

print(vetores_palavras.vocabulary_)

print(vetores_palavras.idf_)

palavras_vetorizadas.todense()

palavras_vetorizadas.todense().shape