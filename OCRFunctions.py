'''
Para o funcionamento dessa função é necessária a instalação da biblioteca pytesseract, PIL e cv2, bem como a execução dos seguintes códigos:
mkdir tessdata
wget -O ./tessdata/por.traineddata https://github.com/tesseract-ocr/tessdata/blob/main/por.traineddata?raw=true

Está função ter por objetivo aplicar o OCR em uma imagem e retornar seu conteúdo de texto em uma string


1º
Chamar a função extraiTexto() passando o caminho para a imagem, converter suas cores de bgr para rgb e extrair os dados com o image_to_data()

2º

passando a imagem, dados e minConf com argumentos

Futuras implementações: 
Definir uma confiança mínima de forma automática


'''

import pytesseract
from pytesseract import Output
from PIL import Image
import cv2







def extraiTexto(file_path):
    '''
    Finalidade:
    Aplicar OCR na imagem ao extrair os caracteres presentes na imagem e retornar em uma string

    image_path:
    É uma variável que contém o caminho URL da imagem selecionada através da futura interface
    
    dados: dados importantes sobre o texto que está sendo extraído, bem como a confiança de cada palavra
    
    minConf: valor mínimo para uma palavra ser considerada para estar presente no texto final

    
    '''
    try:
        img = cv2.imread(file_path)
        if img is not None:
            
            textoFinal = ''
            
            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            minConf = 40
            dados  = pytesseract.image_to_data(rgb,  lang='por', output_type=Output.DICT)
            # Aplica o OCR na imagem afim de buscar tanto os textos quanto dados sobre o texto
            
            
            for i in range(0, len(dados['text'])):
                confianca = int(dados['conf'][i])
                # Filtra apenas palavras que tenha confiança maior que o valor estipulado
                if confianca > minConf:
                    texto = dados['text'][i]
                    textoFinal += texto + ' '
        
            return textoFinal
    
    
    
    except FileNotFoundError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro durante a extração do texto: {e}")
        
    
    
path = '/home/souzaigor499/Desafio/Projeto_Ciclo01_AlphaEdtech/ImagensTeste/ola.jpg'

print(extraiTexto(path))
