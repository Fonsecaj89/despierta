import cv2

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