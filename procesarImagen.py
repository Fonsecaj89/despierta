# -*- coding: utf-8 -*-
import cv2
import video as v

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


def filtroBilateral(frame):
    """Procesa la imagen en escala de grises utilizando filtro bilateral para reducir
       el ruido de la imagen producido, bien sea, por la baja luminosidad o por la
       calidad de la imagen obtenida."""
    fb = cv2.bilateralFilter(frame, 0, 32, 2)
    return fb

def convertirGris(frame):
    """Convierte la imagen a color a escala de grises"""
    try:
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    except:
        gris = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    return gris

def histograma(frame):
    """Procesa la imagen mejorada en escala de grises utilizando la equalizacion por
       histogramas."""
    #Imagen mejorada por Equalizacion de Histogramas.
    histograma = cv2.equalizeHist(frame)
    return histograma

