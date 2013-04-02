import cv2
import video as v
from memory_profiler import profile

#@profile
def procesarImagen(frame):

    gris = convertirGris(frame)
    noruido = filtroBilateral(gris)
    mejorado = histograma(noruido)
    return mejorado

#@profile
def filtroBilateral(frame):
    fb = cv2.bilateralFilter(frame, 0, 32, 2)
    return fb

#@profile
def convertirGris(frame):
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gris

#@profile
def histograma(frame):
    #Imagen mejorada por Equalizacion de Histogramas.
    histograma = cv2.equalizeHist(frame)
    return histograma

def generarAdaptiveThreshold(gris):
    thresh = cv2.adaptiveThreshold(gris,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    return thresh

def generarThresholdBin(inv):
    tval, thresh = cv2.threshold(inv, 200, 255, cv2.THRESH_BINARY)
    return thresh

def invertir(frame):
    inv = cv2.bitwise_not(frame)
    return inv

def recortarImagen(nombre,frame,x,y,width,height):
    v.mostrarVideo(nombre,frame[x/2:-width/2,y/2:-height/2])
