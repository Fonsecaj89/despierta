# -*- coding: utf-8 -*-
import os
import cv2
import deteccion as d
import procesarImagen as pi
import redneuronal as rn
import video as v
import entrenar as e
from alarma import Alarma
from pybrain.tools.xml.networkreader import NetworkReader


def main():
    """Es la clase principal en el cual se sigue la secuencia del procesamiento"""

    a = Alarma()

    #Crear Red Neuronal
    red1 = rn.crearRN()
    red2 = rn.crearRN()

    #Se verifica si el archivo xml que contiene la red neuronal entrenada existe
    path = os.path.dirname(__file__)

    if os.path.isfile(path + '/rna_somnolencia.xml'):
        red_somnolencia = NetworkReader.readFrom('rna_somnolencia.xml')
    else:
        e.entrenarSomnolencia(red1)
        red_somnolencia = NetworkReader.readFrom('rna_somnolencia.xml')

    if os.path.isfile(path + '/rna_ojos.xml'):
        red_ojos = NetworkReader.readFrom('rna_ojos.xml')
    else:
        e.entrenarOjos(red2)
        red_ojos = NetworkReader.readFrom('rna_ojos.xml')


    #Se la camara con la que se va a trabajar
    camara = v.capturarVideo()


    while True:
        #Obtener Video
        val, frame = v.obtenerVideo(camara)

        #Procesar imagenes del video
        improcesada = pi.procesarImagen(frame)


        #Deteccion
        cara = d.deteccionFacial(improcesada)
        ojo_izq = d.deteccionOjoIzquierdo(improcesada)
        ojo_der = d.deteccionOjoDerecho(improcesada)


        """Se ingresan los valores resultantes de las detecciones a las redes neuronales,
           en caso de no haber ninguna deteccion, se generara una alarma"""

        if cara == None:
            """Si el sistema no encuentra ninguna cara debera generar una notificacion de sonido
               para avisar que hay algun problema"""
            a.deteccionNula()
        else:
            print "Somnolencia", rn.estimularRN(red_somnolencia,cara.flatten())

        if ojo_izq == None:
            """Si el sistema no encuentra ninguna cara debera generar una notificacion de sonido
               para avisar que hay algun problema"""
            a.deteccionNula()
        else:
            print "Ojo izquierdo", rn.estimularRN(red_ojos,ojo_izq.flatten())

        if ojo_der == None:
            """Si el sistema no encuentra ninguna cara debera generar una notificacion de sonido
               para avisar que hay algun problema"""
            a.deteccionNula()
        else:
            print "Ojo derecho", rn.estimularRN(red_ojos,ojo_der.flatten())



        """Se ingresan los valores obtenidos al bloque difusor el cual generara las
           alarmas en los casos que convengan."""




        #Mostrar Resultados
        nombreOriginal = "Reconocimiento del Estado Facial de Somnolencia"
        v.mostrarVideo(nombreOriginal,frame)

        key = cv2.waitKey(10)
        if key==27:
          break
          camara.release()


if __name__ == "__main__":
    main()
