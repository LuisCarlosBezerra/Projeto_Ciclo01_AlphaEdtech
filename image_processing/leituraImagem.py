


import pytesseract
import cv2



config_tesseract = '--tessdata-dir tessdata'

img = cv2.imread('C:/Users/luis_/OneDrive/Documentos/Projeto_Ciclo01_Alpha/outputs_tests_images/output_anomalia_4.jpg', 0) # passar o caminho da imagem já precessada



import pytesseract

def conteudoText(img):
    '''
    Esta função extrai o texto de uma imagem e retorna suas linhas.
    !!!NECESSÁRIO A IMAGEM JÁ TRATADA

    Args:
        img: Uma imagem (formato numpy array) contendo o texto que se deseja extrair.

    Returns:
        list: Uma lista de strings, onde cada string representa uma linha de texto extraída da imagem.

    Esta função recebe uma imagem como entrada, extrai o texto utilizando a biblioteca pytesseract
    e retorna uma lista contendo as linhas de texto extraídas. Ela segmenta a imagem, considerando
    apenas a parte superior do documento, onde geralmente está localizado o texto relevante.
    '''

    try:
        (height, width) = img.shape
        (x, y, w, h) = (0, 0, width, height // 3)

        img_mrz = img[y:y+h, x:x+w]

        mrz = pytesseract.image_to_string(img_mrz, lang='por', config=config_tesseract)

        mrz = ''.join(mrz)

        linhas_mrz = mrz.split('\n')

        return linhas_mrz
    
    except Exception as e:
        print(f"Ocorreu um erro ao extrair o conteúdo da imagem: {e}")
        return None


alvos = ['Emitente: ', 'BANCÁRIO Nº ', 'principal do crédito ']
palavrasEncontradas = {}

def encontrarPalavras(alvos, palavrasEncontradas, img):
    '''
    Esta função tem por objetivo encontrar determinadas palavras em um texto e retornar o texto que as segue.

    Args:
        alvos (list): Uma lista de strings contendo as palavras-chave a serem encontradas.
        palavrasEncontradas (dict): Um dicionário que será preenchido com as palavras-chave encontradas e o 
        texto que as segue.
        img: Uma imagem (formato numpy array) contendo o texto onde as palavras-chave serão procuradas.

    Returns:
        list: Uma lista contendo o texto que segue cada palavra-chave encontrada, ou None se nenhuma palavra-chave for encontrada.

    Esta função procura por cada palavra-chave na lista de alvos dentro das linhas de texto de um documento de 
    identificação. Se uma palavra-chave é encontrada em uma linha, o texto que a segue é armazenado no dicionário de palavras encontradas.
    '''
    try:
        linhas_mrz = conteudoText(img)
        for palavra in alvos:
            for line in linhas_mrz:
                if palavra in line:  
                    palavrasEncontradas[palavra] = line.split(palavra, 1)[-1].strip()
                    break

        if palavrasEncontradas:
            return list(palavrasEncontradas.values())
        else:
            raise Exception
    
    except Exception as e:
        print(f"Ocorreu um erro ao encontrar palavras: {e}")
        return None


teste = encontrarPalavras(alvos, palavrasEncontradas, img)

for i in teste:
    print(i)