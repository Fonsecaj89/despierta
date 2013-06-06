# -*- coding: utf-8 -*-
import os
import cv2
import paralelo as p
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


        """Se ingresan a los hilos los parametros de la imagen procesada, la red neuronal
           y la alarma para que el sistema procese los módulos paralelamente y así poder
           mejorar los tiempos de reacción al estado de somnolencia. Luego se inicializa
           el hilo"""

        hilo_cara = p.hiloCara(improcesada,red1,a)
        hilo_cara.start()

        hilo_ojoiz = p.hiloOjoIz(improcesada,red2,a)
        hilo_ojoiz.start()

        hilo_ojode = p.hiloOjoDe(improcesada,red2,a)
        hilo_ojode.start()

        """Obtenemos los valores de cada variable para ser procesados por el sistema de
           alarmas"""
        res_cara = hilo_cara.join()
        res_ojoiz = hilo_ojoiz.join()
        res_ojode = hilo_ojode.join()

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
