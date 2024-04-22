import numpy as np
import pytesseract
import cv2


config_tesseract = '--tessdata-dir tessdata'

# img = cv2.imread('/home/souzaigor499/Desafio/Projeto_Ciclo01_AlphaEdtech/images/ImagensEscaneada/doc002.jpg', 0) # passar o caminho da imagem já precessada


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
        # pega a largura e a altura da imagem
        (height, width) = img.shape
        # filtro de nitidez para melhoria da leitura
        kernel = np.array([[0, -1,  0],
                           [-1,  5, -1],
                           [0, -1,  0]])
        filter2d = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
        # define uma regiao de interesse na imagem a ser lida. Nesse caso, apenas 1/3 da imagem está sendo lido
        (x, y, w, h) = (0, 0, width, height // 3)

        img_mrz = filter2d[y:y+h, x:x+w]
        
        # utiliza a biblioteca pytesseract para a extração do texto
        mrz = pytesseract.image_to_string(img_mrz, lang='por', config=config_tesseract)
        
        # concatena o texto encontrado
        mrz = ''.join(mrz)
        
        
        # lógica para remover trechos de texto indesejados
        newlinhas_mrz = mrz.split('\n')
        linhas_mrz = []

        for line in newlinhas_mrz:
            if line == '' or line ==  ' ' or line == ', ':
                continue
            else:
                linhas_mrz.append(line)

        

        return linhas_mrz
    
    except Exception as e:
        print(f"Ocorreu um erro ao extrair o conteúdo da imagem: {e}")
        return None


def encontrarPalavras(img):
    '''
    Esta função procura por palavras-chave específicas em um texto extraído de uma imagem e retorna um dicionário
    contendo as palavras-chave encontradas e o texto que as segue.

    Args:
        img (numpy.ndarray): Uma imagem contendo o texto onde as palavras-chave serão procuradas.

    Returns:
        dict: Um dicionário contendo as palavras-chave encontradas como chaves e o texto que as segue como valores.
        Retorna None se nenhuma palavra-chave for encontrada.

    Esta função procura por cada palavra-chave na lista de palavras-chave pré-definidas dentro das linhas de texto extraídas
    de uma imagem. Se uma palavra-chave é encontrada em uma linha, o texto que a segue é armazenado no dicionário de palavras encontradas.
    As palavras-chave e seus respectivos textos encontrados são retornados como um dicionário.

    '''

    # dicionario para a conversão do mês encontrado por extenso em número
    meses_numeros = {
        'Janeiro': '01',
        'Fevereiro': '02',
        'Março': '03',
        'Abril': '04',
        'Maio': '05',
        'Junho': '06',
        'Julho': '07',
        'Agosto': '08',
        'Setembro': '09',
        'Outubro': '10',
        'Novembro': '11',
        'Dezembro': '12'
}

    # lista de chaves para serem utilizadas no dicionário a ser retornado ao fim da função
    chaves = [
                'NOME_CLIENTE',
                'CPF_CLIENTE'  ,
                'DATA_CLIENTE:' ,
                'DATA_CONTRATO'  ,
                'ENDERECO' ,
                'AGENCIA' ,
                'CONTA' ,
                'BANCO' ,
                'CEDULA' ,
                'VALOR_CREDITO' ,
                'NOME_AGENTE' ,
                'CPF_AGENTE'
                ]

    # lista de palavras para encontrar o texto após

    palavrasEncontradas = {
                       'Emitente: ' : '',                 # NOME CLIENTE
                       'CPF: ' : '',                      # CPF CLIENTE
                       'Dt de Nasc:' : '',                # DATA DE NASCIMENTO CLIENTE
                       'Local: ' : '',                    # DATA CONTRATO
                       'dereço:' : '',                    # ENDERECO DO CLIENTE
                       'Agência nº: ' : '',                # AGENCIA
                       'Conta nº:' : '',                  # CONTA
                       'anco nº:' : '',                   # BANCO
                       'BANCÁRIO Nº' : '',                # Nº DA CÉDULA
                       '$ ': '',                          # VALOR CRÉDITO 
                       'Nome do Agente:' : '',            # NOME DO AGENTE
                       'CPF do Agente: ' : '',            # CPF DO AGENTE
                       }
    try:
        linhas_mrz = conteudoText(img)
        print(linhas_mrz)
        for palavra, valor in palavrasEncontradas.items():
            for line in linhas_mrz:
                if palavra in line:
                    '''
                    Filtros para encontrar de forma mais otimizada as palavras desejadas.
                    Algumas são limitadas por slice e outras por split em palavras contidas na string
                    É possível que nem todos os filtros funcionem para todas as palavras já que a palavra do filtro pode não ser encontrada pelo OCR
                    
                    '''

                    if palavra == 'anco nº:':
                        valor = line.split(palavra, 1)[-1].strip()[:3]
                    elif palavra == 'Agência nº: ':
                        valor = line.split(palavra, 1)[-1].strip()[:4]
                    elif palavra == 'Endereço:':
                        valor = line.split(palavra, 1)[-1].strip().split(' - ', 1)[0].strip()
                    elif palavra == 'CPF: ':
                        valor = line.split(palavra, 1)[-1].strip()[:13]
                    elif palavra == 'Local: ':
                        valor = line.split(palavra, 1)[-1].strip().split(',', 1)[1].strip()
                    elif palavra == 'Nome do Agente:':
                        valor = line.split(palavra, 1)[-1].strip().split('CPF', 1)[0].strip()
                    elif palavra == 'principal do crédito ':
                        valor = (
                            line.split(palavra, 1)[-1]
                            .strip()[3:-2]
                            
                        )
                    else:
                        valor = (
                            line.split(palavra, 1)[-1]
                            .strip()
                            .replace("-", "")
                            .replace(":", "")
                            .replace(" ", "")
                        )

                    palavrasEncontradas[palavra] = valor
                    break
        if palavrasEncontradas:
            # inicializa uma lista vazia para armazenar os valores encontrados
            palavras = []
            for palavra in palavrasEncontradas:
                palavras.append(palavrasEncontradas[palavra])

            # mapeia as palavras encontradas e as chaves para criar um novo dicionário
            dicionario = dict(zip(chaves, palavras))

            # trecho para obter o mês de forma numérica
            data = dicionario['DATA_CONTRATO']
            partes = data.split()  # Dividir a string em partes
            dia = partes[0] if len(partes[0]) == 2 else '0' + partes[0]  # Obter o dia com zero à esquerda, se necessário
            mes = meses_numeros[partes[2]]  # Obter o número do mês usando o dicionário
            ano = partes[4]

            # redefine o valor do dicionário naquela posição
            dicionario['DATA_CONTRATO'] = f'{dia}/{mes}/{ano}'

            return dicionario
        else:
            raise Exception

    except Exception as e:
        print(f"Ocorreu um erro ao encontrar palavras: {e}")
        return None
