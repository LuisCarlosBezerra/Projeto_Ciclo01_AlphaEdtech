import pytesseract
from pytesseract import Output
import numpy as np
from PIL import Image
import cv2
from image_processing.OCRFunctions import extraiTexto

#para o nosso documento, proporções maiores que 1 indicam que o documento está na posição original
#ou em uma posição de 180º(ponta cabeça).
#imagens com proporção menor que 1 indicam o documento em uma posição de 90 graus, à esquerda
#ou à direita.

def check_position(image_path):
    '''
    Programa para verificar se uma imagem está na posição horizontal ou vertica, para fazer
    os tratamentos necessários dela.

    arguments
        imagem_path (str): Recebe o caminho de uma imagem à ser carregada.

    Return
        img_output (Image): Objeto imagem na posição correta
      '''
    #a variável booleana abaixo vai validar se a nossa imagem está na horizontal(objetivo)
    vertical = False

    img = cv2.imread(image_path)
    largura = img.shape[1]
    altura = img.shape[0]
    proporcao = float(altura/largura)
    centro = (largura // 2, altura // 2)

    if proporcao > 1:
        vertical = True
    
    return vertical

def fix_horizontal(image_path):
    pass

def fix_vertical(image_path):
    pass



#PATH DAS IMAGENS
path = 'C:/Users/luis_/OneDrive/Documentos/Projeto_Ciclo01_Alpha/images/cedula-banco-daycoval.png'
path_d90 = 'C:/Users/luis_/OneDrive/Documentos/Projeto_Ciclo01_Alpha/images/cedula-banco-daycoval-d90.png'
path_e90 = 'C:/Users/luis_/OneDrive/Documentos/Projeto_Ciclo01_Alpha/images/cedula-banco-daycoval-e90.png'
path_180 = 'C:/Users/luis_/OneDrive/Documentos/Projeto_Ciclo01_Alpha/images/cedula-banco-daycoval-180.png'

#print(extraiTexto(path))

teste_posicao = check_position(path)

def confianca(dados):
    for i in range(0, len(dados['text'])):
                confianca = int(dados['conf'][i])
                # Filtra apenas palavras que tenha confiança maior que o valor estipulado
                if confianca > 40:
                    texto = dados['text'][i]
                    textoFinal += texto + ' '
                return textoFinal

# IMAGEM ORIGINAL
img = cv2.imread(path)
largura = img.shape[1]
altura = img.shape[0]
proporcao = float(altura/largura)

print(f'Proporção da imagem original: {proporcao}')
cv2.imshow("Correta", img)
cv2.waitKey()
print('---------------------------EXTRAINDO TEXTO IMAGEM ORIGINAL-----------------------------')
texto, tamanho = extraiTexto(path)
print(texto)
print(f'Total de caracteres lidos: {tamanho}')
print('---------------------------------------------------------------------------------------')
print()

# IMAGEM 90 GRAUS À DIREITA
img_d90 = cv2.imread(path_d90)
largura = img_d90.shape[1]
altura = img_d90.shape[0]
proporcao = float(altura/largura)

print(f'Proporção da imagem 90 graus à direita: {proporcao}')
cv2.imshow("Imagem 90 graus à direita: ", img_d90)
cv2.waitKey()

print('---------------------------EXTRAINDO TEXTO IMAGEM 90D-----------------------------')
texto, tamanho = extraiTexto(path_d90)
print(texto)
print(f'Total de caracteres lidos: {tamanho}')
print('----------------------------------------------------------------------------------')
print()

#IMAGEM 90 GRAUS À ESQUERDA
img_e90 = cv2.imread(path_e90)
largura = img_e90.shape[1]
altura = img_e90.shape[0]
proporcao = float(altura/largura)

print(f'Proporção da imagem 90 graus à esquerda: {proporcao}')
cv2.imshow("Imagem 90 graus à esquerda: ", img_e90)
cv2.waitKey()

print('---------------------------EXTRAINDO TEXTO IMAGEM 90E-----------------------------')
texto, tamanho = extraiTexto(path_e90)
print(texto)
print(f'Total de caracteres lidos: {tamanho}')
print('----------------------------------------------------------------------------------')
print()


# IMAGEM 180 GRAUS (PONTA CABEÇA)
img_180 = cv2.imread(path_180)
largura = img_180.shape[1]
altura = img_180.shape[0]
proporcao = float(altura/largura)

print(f'Proporção da imagem original: {proporcao}')
cv2.imshow("Virada em 180 graus (ponta cabeça): ", img_180)
cv2.waitKey()

print('---------------------------EXTRAINDO TEXTO IMAGEM 180º-----------------------------')
texto, tamanho = extraiTexto(path_180)
print(texto)
print(f'Total de caracteres lidos: {tamanho}')
print('-----------------------------------------------------------------------------------')
print()

path = 'C:/Users/luis_/OneDrive/Documentos/Projeto_Ciclo01_Alpha/images/cedula-banco-daycoval.png'
path_e90 = 'C:/Users/luis_/OneDrive/Documentos/Projeto_Ciclo01_Alpha/images/imgPrint/anomalia_1.png'
path_d90 = 'C:/Users/luis_/OneDrive/Documentos/Projeto_Ciclo01_Alpha/images/imgPrint/anomalia_2.png'
path_180 = 'C:/Users/luis_/OneDrive/Documentos/Projeto_Ciclo01_Alpha/images/imgPrint/anomalia_4.png'
path_torta = 'C:/Users/luis_/OneDrive/Documentos/Projeto_Ciclo01_Alpha/images/imgPrint/anomalia_5.png'
