# -*- coding: utf-8 -*-
import cv2
import video as v
from memory_profiler import profile

#@profile
def procesarImagen(frame):
    """Este es el modulo principal del procesamiento de la imagen y sigue los
       siguientes pasos:
           -Convierte la imagen a escala de grises
           -Suaviza la imagen para reducir el ruido de la imagen
           -Mejora la imagen mediante la equalizacion por histogramas"""
    gris = convertirGris(frame)
    noruido = filtroBilateral(gris)
    mejorado = histograma(noruido)
    return mejorado


#@profile
def filtroBilateral(frame):
    """Procesa la imagen en escala de grises utilizando filtro bilateral para reducir
       el ruido de la imagen producido, bien sea, por la baja luminosidad o por la
       calidad de la imagen obtenida."""
    fb = cv2.bilateralFilter(frame, 0, 32, 2)
    return fb

#@profile
def convertirGris(frame):
    """Convierte la imagen a color a escala de grises"""
    try:
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    except:
        gris = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    return gris

#@profile
def histograma(frame):
    """Procesa la imagen mejorada en escala de grises utilizando la equalizacion por
       histogramas."""
    #Imagen mejorada por Equalizacion de Histogramas.
    histograma = cv2.equalizeHist(frame)
    return histograma

def generarAdaptiveThreshold(gris):
    """Segmenta la imagen por grupo de colores convirtiendolas en blanco y negro. A diferencia
       del threshold (umbral) binario, este metodo respeta los contornos de las formas obtenidas."""
    thresh = cv2.adaptiveThreshold(gris,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    return thresh

def generarThresholdBin(inv):
    """Segmenta la imagen por grupo de colores convirtiendolas en blanco y negro."""
    tval, thresh = cv2.threshold(inv, 220, 255, cv2.THRESH_BINARY)
    return thresh

def invertir(frame):
    """Convierte la imagen en su contraparte negativa"""
    inv = cv2.bitwise_not(frame)
    return inv

def recortarImagen(nombre,frame,x,y,width,height):
    """Recorta la imagen en el tamaño deseado"""
    v.mostrarVideo(nombre,frame[x/2:-width/2,y/2:-height/2])
