# -*- coding: utf-8 -*-
"""
Criado em 13 de outubro as 19:43:44 2020

@autores: 
Adão Nando Tamba  - RA 418203575
Bruno Rocha de Souza – RA 420202776
Diego Araújo do Carmo - RA 417106313
Gerson Guedes de Assis Silva  - RA 417112263
Lucas Caetano Gouveia - RA 917120987
Roger Felipe Giffoni de Almeida - RA 418203429

"""
#Etapa 1: Importação das bibliotecas

import bs4 as bs
import urllib.request
import re
import nltk
import random
import string
import spacy
nltk.download('punkt')

#!python3 -m spacy download pt #Precisa instalar no CMD do ANACONDA

#import numpy as np #Diz que não é utilizado
# pip install bs4
#!pip install spacy --upgrade 
#spacy.__version__
#pip install spacy==2.2.3
#nltk.__version__

#Etapa 2: Carregamento e pré-processamento da base de dados

dados = urllib.request.urlopen('https://pt.wikipedia.org/wiki/Intelig%C3%AAncia_artificial')


dados = dados.read()

dados_html = bs.BeautifulSoup(dados, 'lxml')

paragrafos = dados_html.find_all('p')

conteudo = ''
for p in paragrafos:
  conteudo += p.text

conteudo = conteudo.lower()

lista_sentencas = nltk.sent_tokenize(conteudo)

pln = spacy.load('pt')

stop_words = spacy.lang.pt.stop_words.STOP_WORDS

string.punctuation

def preprocessamento(texto):
  # URLs
  texto = re.sub(r"https?://[A-Za-z0-9./]+", ' ', texto)

  # Espaços em branco
  texto = re.sub(r" +", ' ', texto)

  documento = pln(texto)
  lista = []
  for token in documento:
    lista.append(token.lemma_)

  lista = [palavra for palavra in lista if palavra not in stop_words and palavra not in string.punctuation]
  lista = ' '.join([str(elemento) for elemento in lista if not elemento.isdigit()])

  return lista

texto_teste = 'https://www.iaexpert.com.br ' + lista_sentencas[0]

resultado = preprocessamento(texto_teste)

lista_sentencas_preprocessada = []
for i in range(len(lista_sentencas)):
  lista_sentencas_preprocessada.append(preprocessamento(lista_sentencas[i]))
  

for _ in range(5):
  i = random.randint(0, len(lista_sentencas) - 1)

#Etapa 3: Frases de boas-vindas
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------

textos_boas_vindas_entrada = ('hey', 'ola', 'opa', 'oi', 'eae','tudo bem?','(.*) esta?','bem','bão',)
textos_boas_vindas_respostas = ('\nhey', '\nolá', '\nopa', '\noi', '\nbem-vindo', '\ncomo você está?')

'olá tudo bem'.split()

def responder_saudacao(texto):
  for palavra in texto.split():
    if palavra.lower() in textos_boas_vindas_entrada:
      return random.choice(textos_boas_vindas_respostas)  
  
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------

textos_viagens_entrada = ('(.*) viajar')
textos_viagens_respostas = ('Gostaria de ver viajem para o exterior ou Nacionais?')

def responder_Viagens(texto):
  for palavra in texto.split():
    if palavra.lower() in textos_viagens_entrada:
      return textos_viagens_respostas  
  
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------

textos_exterior_entrada = ('exterior','internacionais','2','segunda opção','internacional')
textos_exterior_respostas = ('\nViagens internacionais disponiveis para: Canada(Digite 1), EUA(Digite 2) e Inglaterra(Digite 3)\n ')

def responder_Exterior(texto):
  for palavra in texto.split():
    if palavra.lower() in textos_exterior_entrada:
      return textos_exterior_respostas  
  
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
  

ValoresNacionais = [ 
[r'(.*) alagoas |alagoas|(.*) al |al',         
['Para Alagoas ida e volta fica: R$1.000,00\nMaceió: A capital de Alagoas reserva lindas praias aos seus visitantes e promete inesquecíveis passeios por seu litoral. Ela é uma capital de pequeno porte, tem ótimos restaurantes, bons preços nos hotéis e uma orla deliciosa para caminhar no fim de tarde. A tarefa mais difícil em Maceió é escolher sua praia preferida, já que são muitas praias bonitas para escolher! Veja aqui mais dicas de Maceió.\nPara voltar ao inicio digite "quit" ']],

[r'(.*) amazonas|(.*) amazonas|(.*) am|(.) am',       
['Para Amazonas ida e volta fica: R$1.210,00\nSugestão: \nManaus: Visitar Manaus é desbravar uma parte da história do Brasil que surpreendente e que muita gente não conhece. Rica culturalmente e com uma natureza impressionante, ela pode ser o ponto de partida para desbravar as belezas da floresta Amazônica, conhecer novos sabores e a pluralidade de nosso país. Visitando a cidade, não dá para perder um passeio para admirar o encontro das águas do Rio Negro e Solimões ou uma visita no Teatro Amazonas.\nPara voltar ao inicio digite "quit"']],

[r'(.*) bahia|bahia|(.*) ba|ba',      
['Para Bahia ida e volta fica: R$1.200,00\nSugestão: \nBarra Grande: A vila de Barra Grande é um popular destino na Península de Maraú, na Bahia. O acesso, que não é tão simples, faz com que o lugar seja um recanto de tranquilidade. Com piscinas naturais, uma vila pequenina e ritmo lento, ela é o ponto de chegada para explorar outras praias próximas, como a Praia de Taipu de Fora.\nCaraíva: O acesso um pouco mais trabalhoso do que outros destinos faz com que a pequena Caraíva permaneça como um local bucólico e bem preservado. Andar com os pés na areia e curtir sossegados dias na beira do mar, sem hora para nada, é o maior desejo de quem visita esse vilarejo baiano.\nPara voltar ao inicio digite "quit"']],

[r'(.*) ceará |ceará|(.*) ceara |ceara|(.*) ce |ce',        
['Para Ceará  ida e volta fica: R$1.300,00\nSugestão: \nSugestão: Jericoacoara: Já bastante conhecida entre os turistas brasileiros e até estrangeiros, Jeri é uma vila pequena na beira do mar, que está em uma região de dunas e próxima de lagoas de águas cristalinas. É um destino com vários hotéis e pousadas, ótimos restaurantes e que promete dias com lindos fins de tarde. Para quem gosta de velejar, é um lugar ótimo! Leia aqui sobre Jericoacoara – Ceará e também nosso Guia completo de Jericoacoara!\nPara voltar ao inicio digite "quit"']],

[r'(.*) goiás|goiás|(.*) goias|goias|(.*) go|go',    
['Para Goiás ida e volta fica: R$1.400,00\nSugestão: \nAlto Paraíso (Chapada dos Veadeiros)\nUma das cidades para se ter como base para visitar a Chapada dos Veadeiros é Alto Paraíso. Pequenina e simpática, ela é uma cidade simples, mas com várias pousadinhas, casas para alugar e bons restaurantes. A partir de lá você pode ir de carro para dezenas de cachoeiras incríveis, com os mais diversos cenários! Leia mais sobre a Chapada dos Veadeiros, em Goiás.\nPirenópolis\nApenas “Piri” para os mais íntimos, Pirenópolis é uma cidade pequena, muito frequentada nos fins de semana, que tem uma arquitetura charmosa e ruas de pedra. É uma cidade com várias cachoeiras ao redor e uma excelente estrutura para quem quer ficar bem hospedado. Muitas pessoas que vivem em Brasília procuram Piri quando querem relaxar. Leia mais sobre Pirenópolis no nosso guia completo sobre o destino.\nPara voltar ao inicio digite "quit"']],

[r'(.*) mato grosso do sul|(.*) ms|ms',       
['Para Mato Grosso do Sul ida e volta fica: R$1.900,00\nSugestão: \nExcelente para quem busca contato com a natureza, Bonito é perfeito! A cidade tem um ritmo de cidade de interior e dezenas de passeios para fazer, que incluem flutuação em rios cristalinos, caminhadas e banhos de cachoeira. Tudo é feita de forma bem organizada e de maneira a preservar o meio ambiente. Leia mais sobre Bonito – Mato Grosso do Sul, e também nosso Guia de Bonito e descubra as belezas desse que  certamente é um dos melhores lugares para viajar no Brasil para quem ama ecoturismo.\nPara voltar ao inicio digite "quit"']],

[r'(.*) paraiba|(.*) paraíba|(.*) pb|(.*) pb',       
['Para  Paraíba ida e volta fica: R$1.700,00\nSugestão: \nA capital paraibana tem uma orla gostosa para caminhar, piscinas naturais formadas no período de maré baixa e uma gastronomia maravilhosa! E quem visita o lugar ainda pode aproveitar para conhecer outras praias da Paraíba, como Tambaba, ou aproveitar o São João, uma festa muito importante por lá. O melhor de tudo é que não é preciso desembolsar valores altos para conhecer o lugar.\nPara voltar ao inicio digite "quit"']],

[r'(.*) mato grosso|(.*) mt|mt',       
['Para  Rio Grande do Norte  ida e volta fica: R$1.700,00\nSugestão: \nAinda desconhecida por muitas pessoas, São Miguel do Gostoso é uma cidade bem pequenininha do Rio Grande do Norte, na beira do mar, ideal para quem busca sossego. A cidade tem pouca estrutura e ainda não é tão explorada pelo turismo, mas tem praias com longos trechos de areia e para quem quer se afastar de uma cidade grande, é uma boa pedida.\nPara voltar ao inicio digite "quit"']],

[r'(.*) minas gerais|minas gerais|minas|(.*) minas|mg|(.*) mg',        
['Para Minas Gerais ida e volta fica: R$1.500,00\nSugestão: \nTiradentes: Com um centro histórico charmoso e ruas que são um convite aos passeios ao ar livre, Tiradentes é uma delícia de destino para curtir um pouco de tranqüilidade e espairecer. É um lugar de gastronomia invejável, ótimo para não fazer muita coisa e simplesmente aproveitar para estar por lá, descansar e apreciar belas paisagens.\nPara voltar ao inicio digite "quit"']],

[r'(.*) sergipe|se',       
['Para Sergipe ida e volta fica: R$1.700,00\nSugestão: \nA capital sergipana mescla ares de uma cidade do interior com os atrativos de uma cidade grande. A cidade tem uma ótima orla para caminhar, praias muitas vezes vazias e um lindo pôr do sol. A gastronomia com direito ao melhor da culinária nordestina é uma “atração” a não perder na cidade!\nPara voltar ao inicio digite "quit"']],

[r'(.*) rio de Janeiro|(.*) rio|rio de Janeiro|(.*) rj|rj',       
['Para Rio de Janeiro ida e volta fica: R$1.600,00\nSugestão: \nVisconde de Mauá: Com trilhas, cachoeiras, morros e muita interação com a natureza, Visconde de Mauá, no Rio de Janeiro e bem pertinho de Minas, é um destino para quem quer aproximação com a natureza. A cidade é muito legal para quem busca um fim de semana tranquilo, ideal para conhecer a fauna e flora da região e renovar a energias antes de voltar pro dia a dia cheio de atividades.\nPara voltar ao inicio digite "quit"']],

[r'(.*) são paulo|(.*) sp|sp|são paulo',       
['Para São paulo ida e volta fica: R$1.700,00\nSugestão: \nLocalizada no norte do Estado de São Paulo, Olímpia é um lugar famoso por seus parques aquáticos e por suas fontes de água termais, ótimas para relaxar em piscinas quentes. A cidade abriga o Thermas dos Laranjais, um dos maiores parque aquático']],

[r'(.*) tocantins|tocantins|(.*) to|to',       
['Para Tocantins ida e volta fica: R$1.600,00\nSugestão: \nJalapão: Descoberto por grande parte dos brasileiros há poucos anos, o Jalapão oferece as mais diversas paisagens naturais, entre elas fervedouros de águas cristalinas, cachoeiras e dunas. É um destino lindo e muito diferente, ideal para fugir dos grandes centros urbanos e relaxar dentre as belezas do cerrado. \nPara voltar ao inicio digite "quit"']],

[r'(.*) para|(.*) pa|(.*) pará|pa',       
['Para Pará ida e volta fica: R$1.850,00\nSugestão: \nAlter do Chão: Alter do Chão ganhou fama mundial ao ser considerada pelo jornal The Guardian como um dos melhores destinos de praia do Brasil. E o título é merecido: a cidade paraense tem mesmo praias dignas dos mais esplendorosos cenários do país e, vale ressaltar, tudo cercado pelo intenso verde amazônico e regado a muita água doce dos rios Tapajós e Arapiuns. O melhor destino do Pará te espera com bancos de areia branquinha, banhos de rio inesquecíveis, florestas encantadas e, claro, uma culinária espetacular!\nPara voltar ao inicio digite "quit"']],

[r'(.*) santa catarina|(.*) sc|santa catarina|sc',       
['Para  Santa Catarina ida e volta fica: R$5.600,00\nSugestão: \nPomerode: Conhecida como a cidade mais alemã do Brasil, Pomerode está em Santa Catarina e se destaca pela arquitetura em estilo enxaimel. Experimentar pratos da gastronomia alemã e cervejas variadas e artesanais está entre os programas tradicionais na pequena cidade.\nPara voltar ao inicio digite "quit"']],

[r'(.*) santa catarina|(.*) sc|santa catarina|sc',       
['Para  Santa Catarina ida e volta fica: R$5.600,00\nSugestão: \nPomerode: Conhecida como a cidade mais alemã do Brasil, Pomerode está em Santa Catarina e se destaca pela arquitetura em estilo enxaimel. Experimentar pratos da gastronomia alemã e cervejas variadas e artesanais está entre os programas tradicionais na pequena cidade.\nPara voltar ao inicio digite "quit"']],

[r'ac|acre|(.*) ac|(.*) acre',    
['Não temos disponiveis viagens para o Acre :( .\nPara voltar ao inicio digite "quit"']],

[r's|sim|yep',    
['Pode escolher então \nMas caso queira voltar ao inicio digite "quit"']],

[r'N|Não|nenhuma|nada',    
['Que pena gostaria de ver outro Pais? é so digitar "quit" que volto']],

[r'(.*) comprar|comprar|gostei|gostei (.*)|legal|(.*) legal|',    
['Que bom que gostou de algo, mas infelizmente eu não posso te cobrar para concluir a compra entre no site da Ro Santos']],

[r'quit',          
['Voltando']] 
]


textos_nacionais_entrada = ('nacionais','brasilzão','brazil','brasil','br','1')
textos_nacionais_respostas = ('\nViagens Nacionais disponiveis para: Alagoas(Digite AL), Amazonas(Digite AM), Bahia(Digite BA), Ceará(Digite CE), Goiás(Digite GO), Mato grosso do sul(Digite MS), Mato grosso(Digite MT), Minas Gerais(Digite MG), Pará(Digite PA), Paraiba(Digite PB), Rio de Janeiro(Digite RJ), Santa Catarina(Digite SC), São Paulo(Digite SP) e Tocantins(Digite TO)')

def responder_Nacionais(texto):
  for palavra in texto.split():
    if palavra.lower() in textos_nacionais_entrada:
      return textos_nacionais_respostas  

textos_Estados_entrada = ('Alagoas','Bahia','Ceará','Goiás','Minas Gerais','Rio de Janeiro','São Paulo')
textos_Estado_respostas = ('')

def responder_Estados(texto):
  for palavra in texto.split():
    if palavra.lower() in textos_Estados_entrada:
      return textos_Estado_respostas
  
  
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------  

ValoresEUA = [ 
[r'(.*) texas|texas|1',         
['Para Texas ida e volta fica: R$1.000,00\nSugestão: \n OTexas é um grande estado no sul dos EUA com desertos, florestas de pinheiros e o rio Grande. Para voltar ao inicio digite "quit" ']],
[r'(.*) nova iorque|new york|2',     
['Para Nova York ida e volta fica: R$1.200,00\nSugestão: \nLocalizada em um dos maiores portos naturais do mundo, a cidade é composta por cinco boroughs: Bronx, Brooklyn, Manhattan, Queens e Staten Island \nPara voltar ao inicio digite "quit"']],
[r'(.*) alasca|alasca|3',        
['Para Alasca ida e volta fica: R$1.300,00\nSugestão: \nO Alasca é um destino para atividades ao ar livre como esqui, mountain biking e canoagem. \nPara voltar ao inicio digite "quit"']],
[r'(.*) washington|washington|4',    
['Para Washington ida e volta fica: R$1.400,00\nSugestão: \nSede de monumentos importantes, além de histórica, Washington D.C. é rica em arquitetura, detalhes, planejamento urbano e belas paisagens. \nPara voltar ao inicio digite "quit"']],
[r'(.*) nevada|nevada|5',        
['Para Nevada ida e volta fica: R$1.500,00\nSugestão: \nEm Nevada, Estados Unidos, está localizada a famosa cidade de Las Vegas. \nPara voltar ao inicio digite "quit"']],
[r'(.*) flórida|(.*) florida|flórida|florida|6',       
['Para Flórida ida e volta fica: R$1.600,00\nSugestão: \nA Flórida é um estado situado no extremo sudeste dos EUA, com o Oceano Atlântico de um lado e o Golfo do México do outro. \nPara voltar ao inicio digite "quit"']],
[r'(.*) califórnia|(.*) california|califórnia|california|7',    
['Para Califórnia ida e volta fica: R$1.700,00\nSugestão: \nO mesmo limita-se com o Oceano Pacífico a oeste, Oregon ao norte, Arizona e Nevada a leste e o Estado mexicano de Baja California ao sul. \nPara voltar ao inicio digite "quit"']],
[r'N|Não|nenhuma|nada',    
['Que pena gostaria de ver outro Pais? é so digitar "quit" que volto']],
[r's|sim|yep',    
['Pode escolher então \nMas caso queira voltar ao inicio digite "quit"']],
[r'comprar|gostei|gostei (.*)|legal|(.*) legal|',    
['Que bom que gostou de algo, mas infelizmente eu não posso te cobrar para concluir a compra entre no site da Ro Santos']],
[r'quit',          
['Voltando']] 
]


textos_EUA_entrada = ('eua','estados unidos','united states','e.u.a','2')
textos_EUA_respostas = ('\nTemos disponiveis com hotel incluso viagens para:\nTexas (Digite 1), Nova York (Digite 2), Alasca (Digite 3) e Washington (Digite 4)\n\nSem Hotel Temos: Nevada (Digite 5), Flórida (Digite 6) e Califórnia (Digite 7) \nAlgo te interessou?')

def responder_EUA(texto):
  for palavra in texto.split():
    if palavra.lower() in textos_EUA_entrada:
      return textos_EUA_respostas  

#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------  

ValoresInglaterra = [ 
[r'(.*) londres|londres|1',     
['Para Londres ida e volta fica: R$1.000,00\nSugestão: \neu centro abriga as sedes imponentes do Parlamento, a famosa torre do relógio do Big Ben e a Abadia de Westminster. \nPara voltar ao inicio digite "quit"']],

[r'(.*) liverpool|liverpool|2',       
['Para Liverpool ida e volta fica: R$1.200,00\nSugestão: \nLiverpool é uma cidade portuária situada no noroeste da Inglaterra, onde o rio Mersey se encontra com o Mar da Irlanda. \nPara voltar ao inicio digite "quit"']],

[r'(.*) birmingham|birmingham|3',    
['Para Birmingham ida e volta fica: R$1.300,00\nSugestão: \nBirmingham é uma cidade grande na Inglaterra com vários pontos de referência. Para voltar ao inicio digite "quit"']],

[r'(.*) bradford|bradford|4',     
['Para Bradford ida e volta fica: R$1.400,00\nSugestão: \nBradford é uma cidade e distrito metropolitano de West Yorkshire, norte da Inglaterra. \nPara voltar ao inicio digite "quit"']],

[r'N|Não|nenhuma|nada',    
['Que pena gostaria de ver outro Pais? é so digitar "quit" que volto']],

[r's|sim|yep',    
['Pode escolher então \nMas caso queira voltar ao inicio digite "quit"']],

[r'(.*) comprar|comprar|gostei|gostei (.*)|legal|(.*) legal|',    
['Que bom que gostou de algo, mas infelizmente eu não posso te cobrar para concluir a compra entre no site da Ro Santos']],

[r'quit',          
['Voltando']] 
]

textos_Inglaterra_entrada = ('inglaterra','england','Reino unido','3')
textos_Inglaterra_respostas = ('\nTemos disponiveis apenas sem hotel incluso viagens para:\nLondres(Digite 1), Liverpool(Digite 2), Birmingham(Digite 3) e Bradford(Digite 4)\nAlgo te interessou?')

def responder_Inglaterra(texto):
  for palavra in texto.split():
    if palavra.lower() in textos_Inglaterra_entrada:
      return textos_Inglaterra_respostas  

#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------- 

ValoresCanada = [ 
[r'(.*) quebec|quebec|1',         
['Para Quebec ida e volta fica: R$1.000,00\nSugestão: A cidade de Quebec fica às margens do rio São Lourenço, na província canadense de Quebec, onde a maioria da população fala francês. \nPara voltar ao inicio digite "quit" ']],

[r'(.*) ontário|ontário|2',     
['Para Ontário ida e volta fica: R$1.100,00\nSugestão: Ontário é a província central do Canadá. \nPara voltar ao inicio digite "quit"']],

[r'(.*) nova escócia|(.*) nova escocia|nova escócia|nova escocia|3',       
['Para Nova Escócia ida e volta fica: R$1.600,00\nSugestão: A Nova Escócia abriga papagaios-do-mar e focas, além de ser um destino procurado para a prática de esportes aquáticos, como o caiaque.\nPara voltar ao inicio digite "quit"']],

[r'(.*) Manitoba|Manitoba|4',    
['Para Manitoba ida e volta fica: R$1.200,00\nSugestão: \nManitoba é frequentemente considerada uma das três províncias das pradarias, é também a quinta província mais populosa.\nPara voltar ao inicio digite "quit"']],

[r'(.*) ottawa|ottawa|5',     
['Para Ottawa ida e volta fica: R$1.300,00\nSugetão: \n Às margens do rio Ottawa, a cidade abriga a Colina do Parlamento, com sua incrível arquitetura vitoriana, e museus como a National Gallery do Canadá, que exibe coleções indígenas e outras obras de arte do país. \nPara voltar ao inicio digite "quit"']],

[r'N|Não|nenhuma|nada',    
['Que pena gostaria de ver outro Pais? é so digitar "quit" que volto']],

[r's|sim|yep',    
['Pode escolher então \nMas caso queira voltar ao inicio digite "quit"']],

[r'(.*) comprar|comprar|gostei|gostei (.*)|legal|(.*) legal|',    
['Que bom que gostou de algo, mas infelizmente eu não posso te cobrar para concluir a compra entre no site da Ro Santos']],

[r'quit',          
['Voltando']] 
]

textos_Canada_entrada = ('canada','canadá','1')
textos_Canada_respostas = ('\nTemos disponiveis com hotel incluso viagens para:\nQuebec(Digite 1), Ontário(Digite 2), Nova Escócia(Digite 3), Manitoba(Digite 4) e Ottawa(Digite 5)\nAlgo te interessou?')

def responder_Canada(texto):
  for palavra in texto.split():
    if palavra.lower() in textos_Canada_entrada:
      return textos_Canada_respostas  

#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------- 

#Etapa 4: Entendimento TF-IDF (Term frequency - inverse document frequency)

from sklearn.feature_extraction.text import TfidfVectorizer

frases_teste = lista_sentencas_preprocessada[:3]

frases_teste.append(frases_teste[0])

vetores_palavras = TfidfVectorizer()
palavras_vetorizadas = vetores_palavras.fit_transform(frases_teste)

palavras_vetorizadas.todense()

palavras_vetorizadas.todense().shape

#Etapa 5: Entendimento similaridade cosseno

from sklearn.metrics.pairwise import cosine_similarity

palavras_vetorizadas[0].todense()

cosine_similarity(palavras_vetorizadas[0], palavras_vetorizadas[1])

cosine_similarity(palavras_vetorizadas[0], palavras_vetorizadas[3])

similaridade = cosine_similarity(palavras_vetorizadas[0], palavras_vetorizadas)

similaridade.argsort()

i = similaridade.argsort()[0][-2]

i = i.flatten()

def responder(texto_usuario):
  resposta_chatbot = ''
  lista_sentencas_preprocessada.append(texto_usuario)

  tfidf = TfidfVectorizer()
  palavras_vetorizadas = tfidf.fit_transform(lista_sentencas_preprocessada)

  similaridade = cosine_similarity(palavras_vetorizadas[-1], palavras_vetorizadas)

  indice_sentenca = similaridade.argsort()[0][-2]
  vetor_similar = similaridade.flatten()
  vetor_similar.sort()
  vetor_encontrado = vetor_similar[-2]

  if (vetor_encontrado == 0):
    resposta_chatbot = resposta_chatbot + 'Desculpe, mas não entendi!'
    return resposta_chatbot
  else:
    resposta_chatbot = resposta_chatbot + lista_sentencas[indice_sentenca]
    return resposta_chatbot

EvitaBug = 0 
continuar = True
print("=" * 50)
print("\nOlá, sou o Chatbot de viagens da empresa Ro Santos!")
print('Agora que me apresentei é sua vez!!! Qual seu nome?')
nome_usuario = input()
print('Muito Prazer ' + nome_usuario + ' agora podemos continuar...\n')
print('Caso te estresse e queira sair pode me dar um tchau ou simplesmente digitar sair\n')    
while (continuar == True):
  print('Nós da Ro Santos Vendemos viagens Nacionais(Digite 1) e Internacionais(Digite 2). Gostaria de consultar valores de viagens:\n')  
  texto_usuario = input()
  texto_usuario = texto_usuario.lower()
  if (texto_usuario != 'sair' and texto_usuario != 'tchau'):
    EvitaBug = EvitaBug + 1  
    if (responder_saudacao(texto_usuario) != None):
      print('\nChatbot de Viagens: ' + responder_saudacao(texto_usuario))
      #print('Viado:')
    else:
        
      if (responder_Nacionais(texto_usuario) != None):
        print('\nChatbot de Viagens: ' + responder_Nacionais(texto_usuario))
        print('Para onde deseja ir?\n\n' + nome_usuario + ' :')
        from nltk.chat.util import Chat
        chat = Chat(ValoresNacionais)
        chat.converse()
        
      else:
        
        if (responder_Exterior(texto_usuario) != None):
          print('\nChatbot de Viagens: ' + responder_Exterior(texto_usuario))
          print('Para onde deseja ir?\n\n' + nome_usuario + ' :')
          texto_usuario = input()
        
          if (texto_usuario.lower() == 'eua' or texto_usuario == '2'):  
            print('\nChatbot de Viagens: \nBoa escolha '+ nome_usuario + responder_EUA(texto_usuario))
            from nltk.chat.util import Chat
            chat = Chat(ValoresEUA)
            chat.converse() 
            
          elif(texto_usuario.lower() == 'canada' or texto_usuario == '1'):
            print('\nChatbot de Viagens: \nBoa escolha '+ nome_usuario + responder_Canada(texto_usuario))
            from nltk.chat.util import Chat
            chat = Chat(ValoresCanada)
            chat.converse() 
            
          elif(texto_usuario.lower() == 'inglaterra' or texto_usuario == '3'):
            print('\nChatbot de Viagens: \nBoa escolha '+ nome_usuario + responder_Inglaterra(texto_usuario))
            from nltk.chat.util import Chat
            chat = Chat(ValoresInglaterra)
            chat.converse() 
          
          else:
            if (responder_Nacionais(texto_usuario) != None):
              print('\nChatbot de Viagens: ' + responder_Nacionais(texto_usuario))
              print('\nPara onde deseja ir neste Brasilzão?')
        
            else:
              print('\nInfelizmente não temos viajens para: ' + texto_usuario)  

        else:
            print('\nChatbot de Viagens: \nDesculpa não entendi, vamos de novo!!!\n ')
            #print(EvitaBug)
            #print(responder(preprocessamento(texto_usuario)))
            #lista_sentencas_preprocessada.remove(preprocessamento(texto_usuario))
            if(EvitaBug >= 50):
              continuar = False        
  else:
    continuar = False
    print('\nChatbot de Viagens: \nAté breve!')
































