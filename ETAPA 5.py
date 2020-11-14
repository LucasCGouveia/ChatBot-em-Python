

# Etapa 5: Entendimento similaridade cosseno

from sklearn.metrics.pairwise import cosine_similarity

palavras_vetorizadas[0].todense()

cosine_similarity(palavras_vetorizadas[0], palavras_vetorizadas[1])
# array([[0.09485423]])

cosine_similarity(palavras_vetorizadas[0], palavras_vetorizadas[3])
# array([[1.]]) - 100% similares

cosine_similarity(palavras_vetorizadas[0], palavras_vetorizadas) 
# aqui compara a similaridade com todos os vetores 0,1,2,3

similaridade = cosine_similarity(palavras_vetorizadas[0], palavras_vetorizadas)
similaridade.argsort() # saber qual maior similaridade
similaridade

i = similaridade.argsort()[0][-2]
i

i = i.flatten() # Converte a variavel i em Array
i







