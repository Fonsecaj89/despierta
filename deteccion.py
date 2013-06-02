# -*- coding: utf-8 -*-
import os
import cv2
import numpy as np
import procesarImagen as pi
import video as v
from memory_profiler import profile

path = os.path.dirname(__file__)

#@profile
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


#@profile
def deteccionOjoIzquierdo(gris):
    """Este modulo detecta el ojo izquierdo utilizando el algoritmo Haar Cascade,
       retorna el area obtenida del ojo estableciendo el tamaño en 64*64"""

    #Cargar el archivo que contiene Haar Cascade
    ojo_izq = cv2.CascadeClassifier(path+'/haarcascades/haarcascade_lefteye_2splits.xml')

    # Detecta el ojo izquierdo
    rectangulos = ojo_izq.detectMultiScale(gris)

    #Sobrepone el rectangulo sobre el video
    for x,y, width,height in rectangulos:
        ojoiz_cortado = gris[y:y+height,x:x+width]
        return cv2.resize(ojoiz_cortado,(64,64))


#@profile
def deteccionOjoDerecho(gris):
    """Este modulo detecta el ojo derecho utilizando el algoritmo Haar Cascade,
       retorna el area obtenida del ojo estableciendo el tamaño en 64*64"""

    #Cargar el archivo que contiene Haar Cascade
    ojo_der = cv2.CascadeClassifier(path+'/haarcascades/haarcascade_righteye_2splits.xml')

    # Detecta el ojo derecho
    rectangulos = ojo_der.detectMultiScale(gris)

    #Sobrepone el rectangulo sobre el video
    for x,y, width,height in rectangulos:
        ojode_cortado = gris[y:y+height,x:x+width]
        return cv2.resize(ojode_cortado,(64,64))


