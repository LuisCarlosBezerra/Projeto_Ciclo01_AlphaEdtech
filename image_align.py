import cv2
import numpy as np

def image_align(imagem_path, padrao_path='C:/Users/luis_/OneDrive/Documentos/Projeto_Ciclo01_Alpha/images/imgPrint/doc1.png'):
    img1_color = cv2.imread(imagem_path)  
    img2_color = cv2.imread(padrao_path)    
    img1 = cv2.cvtColor(img1_color, cv2.COLOR_BGR2GRAY) 
    img2 = cv2.cvtColor(img2_color, cv2.COLOR_BGR2GRAY) 
    height, width = img2.shape 
    orb_detector = cv2.ORB_create(5000) 
        
    kp1, d1 = orb_detector.detectAndCompute(img1, None) 
    kp2, d2 = orb_detector.detectAndCompute(img2, None) 
        
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True) 
    matches = list(matcher.match(d1, d2) )
    print(type(matches))
    matches.sort(key = lambda x: x.distance) 
    matches = matches[:int(len(matches)*90)] 
    no_of_matches = len(matches) 
    p1 = np.zeros((no_of_matches, 2)) 
    p2 = np.zeros((no_of_matches, 2)) 
        
    for i in range(len(matches)): 
        p1[i, :] = kp1[matches[i].queryIdx].pt 
        p2[i, :] = kp2[matches[i].trainIdx].pt 
    homography, mask = cv2.findHomography(p1, p2, cv2.RANSAC) 
    transformed_img = cv2.warpPerspective(img1_color, 
                        homography, (width, height)) 
    save_path = './outputs_tests_images/output.png'
    cv2.imwrite(save_path, transformed_img)
    return save_path


if __name__ == "__main__":
    #padrao = 'images/imgPrint/doc1.png'
    imagem = 'images/imgPrint/anomalia_4.png'
    image_align(imagem)