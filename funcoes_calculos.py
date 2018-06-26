def CalculaMedia(lstdados):
	somatorio = 0
	media = 0 
	tam = len(lstdados) #quantidade total da amostra
	
	for valor in lstdados:
		somatorio = somatorio + valor;
	#fim  for
	media = somatorio/tam
	
	return media
#fim função media

def VerPar(lstdados):
	if len(lstdados)%2 == 0:
		return True
	#fim if
	
	return False
#fim função
	
def CalculaMediana(lstdados):	
	#Verifica se o tamanho da lista é par
	if VerPar:
		pos1 = lstdados[int((len(lstdados)/2)-1)]
		pos2 = lstdados[int((len(lstdados)/2))]
		media = CalculaMedia([pos1,pos2])
		return media
	#Se for impar
	else:
		pos = lstdados[int(len(lstdados)/2)]
		return pos
#fim função mediana

def CaculaOcorrencias(listaChaves,dicDados):
	maior = 0
	moda = 0
	
	for chave in listaChaves:
		if dicDados[chave] > maior:
			moda = chave
			maior = dicDados[chave]
		#fim if 
	#fim for
	
	return moda
#fim função
	
	
def CalculaModa(lstdados):
	dicDados = {} 	#dicionario de ocorrencias
	
	for valor in lstdados:
		if valor in dicDados.keys():
			dicDados[valor] = dicDados[valor]+1
		else:
			dicDados[valor] = 1
	#fim for

	listaChaves = dicDados.keys()
	moda = CaculaOcorrencias(listaChaves,dicDados)
	
	return moda
#fim função moda

def CalculaVariancia(lstdados):
	media = CalculaMedia(lstdados)
	somatorio = 0
	tam = len(lstdados)
	variancia = 0

	for valor in lstdados:
		somatorio = somatorio + ((valor - media) ** 2)
	#fim for 
	variancia = somatorio/tam-1
	
	return variancia
#fim função variancia

def VerificaDesvioPadrao(lstdados):
	variancia = CalculaVariancia(lstdados)
	variancia = variancia ** (1/2)
	
	return variancia
##fim função Desvio padrão

def PrimeiroQuartil(lstdados):
	pos = round((len(lstdados)+1)*0.25)
	return lstdados[pos]
#fim função 

def TerceiroQuartil(lstdados):
	pos = round((len(lstdados)+1)*0.75)
	return lstdados[pos]
#fim função 

def AmplitudeInterquartil(lstdados):
	primquartil = PrimeiroQuartil(lstdados)
	terquartil = TerceiroQuartil(lstdados)
	return terquartil - primquartil
#fim função 
def CalculaMedia(lstdados):
	somatorio = 0
	media = 0 
	tam = len(lstdados) #quantidade total da amostra
	
	for valor in lstdados:
		somatorio = somatorio + valor;
	#fim  for
	media = somatorio/tam
	
	return media
#fim função media

def VerPar(lstdados):
	if len(lstdados)%2 == 0:
		return True
	#fim if
	
	return False
#fim função
	
def CalculaMediana(lstdados):	
	#Verifica se o tamanho da lista é par
	if VerPar:
		pos1 = lstdados[int((len(lstdados)/2)-1)]
		pos2 = lstdados[int((len(lstdados)/2))]
		media = CalculaMedia([pos1,pos2])
		return media
	#Se for impar
	else:
		pos = lstdados[int(len(lstdados)/2)]
		return pos
#fim função mediana

def CaculaOcorrencias(listaChaves,dicDados):
	maior = 0
	moda = 0
	
	for chave in listaChaves:
		if dicDados[chave] > maior:
			moda = chave
			maior = dicDados[chave]
		#fim if 
	#fim for
	
	return moda
#fim função
	
	
def CalculaModa(lstdados):
	dicDados = {} 	#dicionario de ocorrencias
	
	for valor in lstdados:
		if valor in dicDados.keys():
			dicDados[valor] = dicDados[valor]+1
		else:
			dicDados[valor] = 1
	#fim for

	listaChaves = dicDados.keys()
	moda = CaculaOcorrencias(listaChaves,dicDados)
	
	return moda
#fim função moda

def CalculaVariancia(lstdados):
	media = CalculaMedia(lstdados)
	somatorio = 0
	tam = len(lstdados)
	variancia = 0

	for valor in lstdados:
		somatorio = somatorio + ((valor - media) ** 2)
	#fim for 
	variancia = somatorio/tam-1
	
	return variancia
#fim função variancia

def VerificaDesvioPadrao(lstdados):
	variancia = CalculaVariancia(lstdados)
	variancia = variancia ** (1/2)
	
	return variancia
##fim função Desvio padrão

def PrimeiroQuartil(lstdados):
	pos = round((len(lstdados)+1)*0.25)
	return lstdados[pos]
#fim função 

def TerceiroQuartil(lstdados):
	pos = round((len(lstdados)+1)*0.75)
	return lstdados[pos]
#fim função 

def AmplitudeInterquartil(lstdados):
	primquartil = PrimeiroQuartil(lstdados)
	terquartil = TerceiroQuartil(lstdados)
	return terquartil - primquartil
#fim função 
