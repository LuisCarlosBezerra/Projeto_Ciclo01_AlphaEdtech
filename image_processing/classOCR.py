"""
Esta classe tem por objetivo instanciar um objeto OCR para manipulá-lo entre as funções de alinhamento e leitura de imagem,
respectivamente, provenientes dos módulos image_align e leituraImagem.

Para inicializar um objeto OCR, devem ser passados como argumentos o caminho da imagem a ser lida e o caminho da imagem
padrão que serve como referência para o alinhamento.

Attributes:
    img_path (str): O caminho da imagem a ser lida.
    padrao_path (str): O caminho da imagem padrão que serve como referência para o alinhamento.

Methods:
    alinhar_img(): Método que alinha a imagem de entrada com a imagem padrão de referência.
    extrairTexto(): Método que extrai o texto da imagem alinhada utilizando OCR.

Returns:
    dict: Um dicionário contendo as palavras-chave encontradas na imagem alinhada e o texto que as segue, ou None se nenhuma palavra-chave for encontrada.
"""

import image_align
import leituraImagem
import numpy as np


class OCR:
    # incializa a classe passando o caminho da imagem a ser lida e imagem padrão
    def __init__(
        self, img_path: str, padrao_path: str = "images/ImagensEscaneada/doc002.jpg"
    ) -> None:
        self.img_path = img_path
        self.padrao_path = padrao_path
        self.img = None

    # chama a função de alinhamento da imagem vinda de image_align e retorna a imagem alinhada
    def alinhar_img(self) -> np.ndarray:
        imgAlinhada = image_align.image_align(
            imagem_path=self.img_path, padrao_path=self.padrao_path
        )
        return imgAlinhada

    # chama a funçao de extração de texto vinda de leituraImagem e retorna um dicionário com suas respectivas chaves e valores
    def extrairTexto(self) -> dict:
        imgLer = self.alinhar_img()
        dictPalavras = leituraImagem.encontrarPalavras(imgLer)
        return dictPalavras


# Exemplo de Uso
OCR = OCR(r'C:\Users\luis_\OneDrive\Documentos\Projeto_Ciclo01_Alpha\images\ImagensEscaneada\doc006.jpg', r"C:\Users\luis_\OneDrive\Documentos\Projeto_Ciclo01_Alpha\images\ImagensEscaneada\doc002.jpg")

OCR.alinhar_img()
dicionario = OCR.extrairTexto()

for i in dicionario:
    print(f"{i}...................................{dicionario[i]}")
