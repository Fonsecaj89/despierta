import cv2
import deteccion as d
import procesarImagen as pi
import redneuronal as rn
import video as v


def main():

    camara = v.capturarVideo()

    #Crear Red Neuronal
    #red = rn.crearRN()

    while True:
        #Obtener Video
        val, frame = v.obtenerVideo(camara)

        #Procesar imagenes del video
        improcesada = pi.procesarImagen(frame)

        #Deteccion
        d.deteccionFacial(frame, improcesada)
        d.deteccionOjoIzquierdo(frame, improcesada)
        d.deteccionOjoDerecho(frame, improcesada)

        #Estimular la Red Neuronal
        #rn.estimularRN(red,df)

        #Mostrar Resultados
        nombreOriginal = "Reconocimiento del Estado Facial de Somnolencia"
        v.mostrarVideo(nombreOriginal,frame)

        key = cv2.waitKey(10)
        if key==27:
          break
          camara.release()


if __name__ == "__main__":
    main()
