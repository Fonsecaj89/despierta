# -*- coding: utf-8 -*-
import os
import time
import cv2
import procesarImagen as pi
import aux2 as d
import redneuronal as rn
import video as v
import entrenar as e
from alarma import Alarma
from pybrain.tools.xml.networkreader import NetworkReader


def main():
    try:
        camara = v.capturarVideo()
    except:
        a.noCamara()


    while True:
        val, frame = v.obtenerVideo(camara)

        #Procesar imagenes del video
        improcesada = pi.procesarImagen(frame)


        """Se detecta la cara del video, luego se activa las redes neuronales para detectar
           los estados de somnolencia y atencion en el conductor"""

        cara = d.deteccionFacial(frame,improcesada)
        #Mostrar Resultados
        nombreOriginal = "Reconocimiento del Estado Facial de Somnolencia"
        v.mostrarVideo(nombreOriginal,frame)
        key = cv2.waitKey(1)
        if key==27:
            break
            camara.release()


if __name__ == "__main__":
    main()
