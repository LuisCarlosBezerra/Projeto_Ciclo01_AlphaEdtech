import cv2 
import numpy as np 

#PATH DAS IMAGENS
padrao = 'C:/Users/luis_/OneDrive/Documentos/Projeto_Ciclo01_Alpha/images/ImagensEscaneada/doc002.jpg'
path_d90 = 'C:/Users/luis_/OneDrive/Documentos/Projeto_Ciclo01_Alpha/images/imgPrint/anomalia_1.png'
path_e90 = 'C:/Users/luis_/OneDrive/Documentos/Projeto_Ciclo01_Alpha/images/imgPrint/anomalia_2.png'
path_180 = 'C:/Users/luis_/OneDrive/Documentos/Projeto_Ciclo01_Alpha/images/ImagensEscaneada/doc001.jpg'
path_torto = 'C:/Users/luis_/OneDrive/Documentos/Projeto_Ciclo01_Alpha/images/ImagensEscaneada/doc006.jpg'


lista_anomalias = [path_d90,
                   path_e90,
                   path_180,
                   path_torto]


for index, anomalia in enumerate(lista_anomalias):
    

  img1_color = cv2.imread(anomalia)  
  img2_color = cv2.imread(padrao)    
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
  temp_path = 'C:/Users/luis_/OneDrive/Documentos/Projeto_Ciclo01_Alpha/outputs_tests_images/output_anomalia_' + str(index+1) + '.jpg'
  print(temp_path)
  cv2.imwrite(f'{temp_path}', transformed_img)
