import cv2
import rn
from memory_profiler import profile


def capturarVideo():
    camara = cv2.VideoCapture(0)
    #Establecer resolucion del video en 320x240
    camara.set(3, 320)
    camara.set(4, 240)

    if not camara.isOpened():
        print("No se puede abrir la camara")

    return camara

#-----------------------------------------OBTENER VIDEO-----------------------------

def obtenerVideo(camara):
    val, frame = camara.read()
    return val, frame

def mostrarVideo(nombre,frame):
    cv2.imshow(nombre, frame)


#-----------------------------------------PROCESAR IMAGEN------------------------------
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

#------------------------------------------DETECCION DE CARACTERISTICAS---------------------

def goodfeatures(frame):
    #Genera los puntos de seguimineto.
    feature_params = dict( maxCorners = 3000,qualityLevel = 0.1,minDistance = 2,blockSize = 1)
    features = cv2.goodFeaturesToTrack(frame, **feature_params)
    features = features.reshape((-1, 2))
    for x, y in features:
        return cv2.circle(frame, (x, y), 10, (0, 0, 255))



#-------------------------------------DETECCION Y RECONOCIMIENTO FACIAL Y OJOS------------------


#@profile
def deteccionFacial(frame, gris):

    # load detection file (various files for different views and uses)
    cara = cv2.CascadeClassifier('/home/taberu/Tesis/haarcascades/haarcascade_frontalface_alt.xml')

    # Detecta la cara
    rectangulos = cara.detectMultiScale(gris)

    #Sobrepone el rectangulo sobre el video
    for x,y, width,height in rectangulos:
        return cv2.rectangle(frame, (x,y), (x+width, y+height), (255,0,0), 2)


def deteccionPupilas(frame):
    inv = invertir(frame)
    #ginversa = convertirGris(inv)
    t = generarThresholdBin(inv)


    mostrarVideo("Threshold Macabro", t)


def deteccionOjos(frame, gris):
    # load detection file (various files for different views and uses)
    ojo_izq = cv2.CascadeClassifier('/home/taberu/Tesis/haarcascades/haarcascade_eye.xml')

    # Detecta el ojo izquierdo
    rectangulos = ojo_izq.detectMultiScale(gris)

    #Sobrepone el rectangulo sobre el video
    for x,y, width,height in rectangulos:
        return cv2.rectangle(frame, (x,y), (x+width, y+height), (255,0,0), 1)

#@profile
def deteccionBoca(frame, gris):
    boca = cv2.CascadeClassifier('/home/taberu/Tesis/haarcascades/haarcascade_mcs_mouth.xml')

    # Detecta el ojo izquierdo
    rectangulos = boca.detectMultiScale(gris)

    #Sobrepone el rectangulo sobre el video
    for x,y, width,height in rectangulos:
        return cv2.rectangle(frame, (x,y), (x+width, y+height), (255,0,0), 1)

#@profile
def deteccionOjoIzquierdo(frame, gris):
    ojo_izq = cv2.CascadeClassifier('/home/taberu/Tesis/haarcascades/haarcascade_lefteye_2splits.xml')

    # Detecta el ojo izquierdo
    rectangulos = ojo_izq.detectMultiScale(gris)

    #Sobrepone el rectangulo sobre el video
    for x,y, width,height in rectangulos:
        return cv2.rectangle(frame, (x,y), (x+width, y+height), (255,0,0), 1)


#@profile
def deteccionOjoDerecho(frame, gris):
    # load detection file (various files for different views and uses)
    ojo_der = cv2.CascadeClassifier('/home/taberu/Tesis/haarcascades/haarcascade_righteye_2splits.xml')

    # Detecta el ojo derecho
    rectangulos = ojo_der.detectMultiScale(gris)

    #Sobrepone el rectangulo sobre el video
    for x,y, width,height in rectangulos:
        return cv2.rectangle(frame, (x,y), (x+width, y+height), (255,0,0), 1)




def main():

    camara = capturarVideo()

    #Crear Red Neuronal
    #red = rn.crearRN()

    while True:
        #Obtener Video
        val, frame = obtenerVideo(camara)

        #Procesar imagenes del video
        improcesada = procesarImagen(frame)

        #Deteccion
        deteccionFacial(frame, improcesada)
        deteccionOjoIzquierdo(frame, improcesada)
        deteccionOjoDerecho(frame, improcesada)

        #Estimular la Red Neuronal
        #rn.estimularRN(red,df)

        #Mostrar Resultados
        nombreOriginal = "Reconocimiento del Estado Facial de Somnolencia"
        mostrarVideo(nombreOriginal,frame)

        key = cv2.waitKey(10)
        if key==27:
          break
          camara.release()


if __name__ == "__main__":
    main()