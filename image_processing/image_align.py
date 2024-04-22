import cv2
import numpy as np

def image_align(imagem_path = 'images/imgPrint/doc1.png', padrao_path='/home/souzaigor499/Desafio/Projeto_Ciclo01_AlphaEdtech/images/imgPrint/doc1.png'):
    """
    Essa função tem como objetivo receber uma imagem qualquer e realizar o tratamento de orientação, deixando-a perfeitamente
    alinhada para uso nas etapas de OCR. É necessária uma imagem padrão para ser a referência para o alinhamento. Essa imagem padrão
    já está previamente salva dentro da função, mas também pode ter o seu caminho passado como argumento na chamada da função.

    Argumentos:
        imagem_path (str): Caminho da imagem à ser alinhada.
        padrao_path (str): Caminho da imagem padrão (imagem referência de alinhamento).

    Return:
        save_path (str): Caminho da imagem que foi alinhada, salva temporariamente.
    """
    #criando um objeto imagem à partir do path da imagem à ser alinhada, forneceda como parâmetro
    img1_color = cv2.imread(imagem_path) 
    #criando um objeto imagem à partir do path padrão (imagem de referência)
    img2_color = cv2.imread(padrao_path)   
    #convertendo as 2 imagens para grayscale 
    img1 = cv2.cvtColor(img1_color, cv2.COLOR_BGR2GRAY) 
    img2 = cv2.cvtColor(img2_color, cv2.COLOR_BGR2GRAY) 
    #recebendo os valores de altura e comprimento da imagem padrão.
    height, width = img2.shape 
    #criando um objeto ORB
    orb_detector = cv2.ORB_create(5000) 
    #mapeando os pontos chave para cada uma das imagens. À partir da comparação é possível identivicar o quanto elas estão desalinh-
    #das entre si.
    kp1, d1 = orb_detector.detectAndCompute(img1, None) 
    kp2, d2 = orb_detector.detectAndCompute(img2, None) 
    
    #verificação de similaridade entre as imagens
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True) 
    matches = list(matcher.match(d1, d2) )
    # print(type(matches))
    matches.sort(key = lambda x: x.distance) 
    matches = matches[:int(len(matches)*90)] 
    no_of_matches = len(matches) 
    p1 = np.zeros((no_of_matches, 2)) 
    p2 = np.zeros((no_of_matches, 2)) 

    #realizando a correção em uma nova imagem
    for i in range(len(matches)): 
        p1[i, :] = kp1[matches[i].queryIdx].pt 
        p2[i, :] = kp2[matches[i].trainIdx].pt 
    homography, mask = cv2.findHomography(p1, p2, cv2.RANSAC) 
    transformed_img = cv2.warpPerspective(img1_color, 
                        homography, (width, height)) 

    #ret, bin = cv2.threshold(transformed_img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    #imagem_escala_cinza = cv2.cvtColor(transformed_img, cv2.COLOR_BGR2GRAY)

    # save_path = './outputs_tests_images/output.png'
    # cv2.imwrite(save_path, transformed_img)
    kernel = np.ones((3, 3), np.uint8)
    # img = cv2.resize(transformed_img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
    #img = cv2.dilate(transformed_img, kernel, iterations=3)
    #img = cv2.erode(transformed_img, kernel, iterations=1)
    suave = cv2.blur(transformed_img, (1,1))
    # converte a imagem tranformada em escala de cinza para ser utilizada na função leituraImagem.encontrarPalavras()
    imagem_escala_cinza = cv2.cvtColor(suave, cv2.COLOR_BGR2GRAY)
    ret, bin = cv2.threshold(imagem_escala_cinza,160,255,cv2.THRESH_BINARY_INV)
    bin = cv2.blur(bin, (2,2))
    bin = cv2.erode(bin, kernel, iterations=1)
    return bin


if __name__ == "__main__":
    padrao = r'C:\Users\luis_\OneDrive\Documentos\Projeto_Ciclo01_Alpha\images\ImagensEscaneada\doc004.jpg'
    imagem = r'C:\Users\luis_\OneDrive\Documentos\Projeto_Ciclo01_Alpha\images\ImagensEscaneada\doc006.jpg'
    image = image_align(imagem, padrao)
    cv2.imshow('image', image)
    cv2.waitKey()