# -*- coding: utf-8 -*-
import os
import cv2

path = os.path.dirname(__file__)

def deteccionFacial(gris):
    """Este modulo detecta los rostros utilizando el algoritmo Haar Cascade,
       retorna el area obtenida de la cara estableciendo el tamaño en 64*64"""

    #Cargar el archivo que contiene Haar Cascade
    cara = cv2.CascadeClassifier(path+'/haarcascades/haarcascade_frontalface_alt.xml')

    # Detecta la cara
    rectangulos = cara.detectMultiScale(gris)

    #Sobrepone el rectangulo sobre el video por cada cara encontrada
    for x,y, width,height in rectangulos:
        cara_cortada = gris[y:y+height,x:x+width]
        return cv2.resize(cara_cortada,(64,64))


