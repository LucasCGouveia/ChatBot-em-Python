#Etapa 1: Importação das bibliotecas

import bs4 as bs #Beautiful Soup
#pip install bs4
#pip install spacy==2.2.3
import urllib.request
import re
import nltk
nltk.__version__
import numpy as np
import random
import string

#nltk.download('punkt')

#pip install spacy --upgrade

import spacy 
spacy.__version__ 


#python -m spacy download pt  DIGITAR NO ANACONDA PROMPT como adm 

#ETAPA 2: Carregamento e pré-processamento da base de dados

#Aqui alimentamos a variavel dados com o link que queremos ler
dados = urllib.request.urlopen('https://pt.wikipedia.org/wiki/Intelig%C3%AAncia_artificial')

#Aqui eu leio a pagina e jogo toda informação para variavel dados
dados = dados.read()
dados

#Usando a bliblioteca bs conseguimos separar todas as tags HTML e jogamos para dados_html
dados_html = bs.BeautifulSoup(dados, 'lxml')
dados_html

#pegamos todas as tags p aonde tem os textos que precisamos para o chatbot responder
paragrafos = dados_html.find_all('p')
len(paragrafos) # o len faz um count de quantos paraframos exite na variavel len

paragrafos[0] #Traz as Tags p

paragrafos[0].text #o .text remove as Tags(<P>)

# Aqui em baixo criamos um for para alimentar a variavel conteudo com todos os paraframos para p.text e jogamos no conteudo
conteudo = ''
for p in paragrafos:
  conteudo += p.text
  
  #aqui listamos o que tem em conteudo
  conteudo
  
  conteudo = conteudo.lower() # o lower coloca todas as letras como minusculas
conteudo

#com a bliblioteca nltk vamos separar as frases do texto da pagina com o sent_tokenize
lista_sentencas = nltk.sent_tokenize(conteudo)
lista_sentencas
  
len(lista_sentencas) # como vimos acima o len faz um count de quantas frases temos no lista_sentencas
#229

type(lista_sentencas)

lista_sentencas[1]

#pln = Processamento de linguagem natural
pln = spacy.load('pt') #<spacy.lang.pt.Portuguese at 0x22be39c6d00> 
pln

stop_words = spacy.lang.pt.stop_words.STOP_WORDS #aqui listamos as palavras de parada 

print(stop_words) #são palavras que...

type(stop_words)

len(stop_words) #413

string.punctuation #Pontuações para remover do texto em questão

# regexr.com  site recomendado para realizar testes em expressõs

# Funcao para tirar urls do texto
def preprocessamento(texto):
  # URLs
  texto = re.sub(r"https?://[A-Za-z0-9./]+", ' ', texto) #Remove URL
  # Espaços em branco
  texto = re.sub(r" +", ' ', texto) #Remove espaços
  
  documento = pln(texto)
  lista = []
  for token in documento:
    lista.append(token.lemma_)

  lista = [palavra for palavra in lista if palavra not in stop_words and palavra not in string.punctuation]
  lista = ' '.join([str(elemento) for elemento in lista if not elemento.isdigit()])
  
  return lista

texto_teste = 'https://www.Lucas.com.br ' + lista_sentencas[0]
texto_teste

resultado = preprocessamento(texto_teste)
resultado

lista_sentencas_preprocessada = []
for i in range(len(lista_sentencas)):
  lista_sentencas_preprocessada.append(preprocessamento(lista_sentencas[i]))
  
for _ in range(5):
  i = random.randint(0, len(lista_sentencas) - 1)
  print(lista_sentencas[i])
  print(lista_sentencas_preprocessada[i])
  print('-----')


#DAQUI PRA CIMA ENTENDI PORRA NENHUMA ele varre varias vezes as sentenças 
