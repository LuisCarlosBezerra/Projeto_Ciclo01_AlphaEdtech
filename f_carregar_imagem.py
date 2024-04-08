"""
Este script utiliza a biblioteca OpenCV (cv2) para carregar e processar imagens.
Também utiliza a biblioteca numpy para especificar os tipos de objetos na função

Documentação OpenCV: https://docs.opencv.org/
"""

import cv2
import numpy

def carregar_imagem(caminho_imagem: str) -> numpy.ndarray:
    """
    Finalidade:
    Carrega uma imagem a partir do caminho especificado.

    Argumentos:
        caminho_imagem (str): O caminho para o arquivo de imagem a ser carregado.

    Retornos:
        numpy.ndarray or None: O objeto ndarray que representa a imagem carregada.
                               Retorna None se houver um erro ao carregar a imagem.
    """
    try:
        imagem = cv2.imread(caminho_imagem)
        if imagem is not None:
            print("Imagem carregada com sucesso!")
            return imagem
        else:
            raise ValueError("A imagem foi carregada como vazia.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique se o caminho fornecido está correto.")
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")
    return None
