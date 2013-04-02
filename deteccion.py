import cv2
import procesarImagen as pi
import video as v
from memory_profiler import profile

#@profile
def deteccionFacial(frame, gris):

    # load detection file (various files for different views and uses)
    cara = cv2.CascadeClassifier('/home/taberu/Tesis/haarcascades/haarcascade_frontalface_alt.xml')

    # Detecta la cara
    rectangulos = cara.detectMultiScale(gris)

    #Sobrepone el rectangulo sobre el video
    for x,y, width,height in rectangulos:
        pi.recortarImagen("Cara",frame,x,y,width,height)
        #return cv2.rectangle(frame, (x,y), (x+width, y+height), (255,0,0), 2)


#@profile
def deteccionOjoIzquierdo(frame, gris):
    ojo_izq = cv2.CascadeClassifier('/home/taberu/Tesis/haarcascades/haarcascade_lefteye_2splits.xml')

    # Detecta el ojo izquierdo
    rectangulos = ojo_izq.detectMultiScale(gris)

    #Sobrepone el rectangulo sobre el video
    for x,y, width,height in rectangulos:
        pi.recortarImagen("ojo izquierdo",frame,x,y,width,height)
        #return cv2.rectangle(frame, (x,y), (x+width, y+height), (255,0,0), 1)


#@profile
def deteccionOjoDerecho(frame, gris):
    # load detection file (various files for different views and uses)
    ojo_der = cv2.CascadeClassifier('/home/taberu/Tesis/haarcascades/haarcascade_righteye_2splits.xml')

    # Detecta el ojo derecho
    rectangulos = ojo_der.detectMultiScale(gris)

    #Sobrepone el rectangulo sobre el video
    for x,y, width,height in rectangulos:
        pi.recortarImagen("ojo derecho",frame,x,y,width,height)
        #return cv2.rectangle(frame, (x,y), (x+width, y+height), (255,0,0), 1)

def deteccionPupilas(frame):
    inv = pi.invertir(frame)
    #ginversa = convertirGris(inv)
    t = pi.generarThresholdBin(inv)
    v.mostrarVideo("Threshold Macabro", t)

#@profile
def deteccionBoca(frame, gris):
    boca = cv2.CascadeClassifier('/home/taberu/Tesis/haarcascades/haarcascade_mcs_mouth.xml')

    # Detecta el ojo izquierdo
    rectangulos = boca.detectMultiScale(gris)

    #Sobrepone el rectangulo sobre el video
    for x,y, width,height in rectangulos:
        return cv2.rectangle(frame, (x,y), (x+width, y+height), (255,0,0), 1)


#------------------------------------------DETECCION DE CARACTERISTICAS---------------------

def goodfeatures(frame):
    #Genera los puntos de seguimineto.
    feature_params = dict( maxCorners = 3000,qualityLevel = 0.1,minDistance = 2,blockSize = 1)
    features = cv2.goodFeaturesToTrack(frame, **feature_params)
    features = features.reshape((-1, 2))
    for x, y in features:
        return cv2.circle(frame, (x, y), 10, (0, 0, 255))