# -*- coding: utf-8 -*-
import os
import time
import cv2
import procesarImagen as pi
import deteccion as d
import redneuronal as rn
import video as v
import entrenar as e
from alarma import Alarma
from pybrain.tools.xml.networkreader import NetworkReader


def main():
    """Es la clase principal en el cual se sigue la secuencia del procesamiento"""

    a = Alarma()
    """Al inicializar genera un sonido inidicado queel dispositivo esa funcionando
    sin contratiempos"""
    a.inicio()

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

    if os.path.isfile(path + '/rna_atento.xml'):
        red_atento = NetworkReader.readFrom('rna_atento.xml')
    else:
        e.entrenarAtento(red2)
        red_atento = NetworkReader.readFrom('rna_atento.xml')

    #Se la camara con la que se va a trabajar
    try:
        camara = v.capturarVideo()
    except:
        a.noCamara()


    while True:
        Somnolencia = 0.00001
        Atencion = 0.00001
        #Obtener Video
        val, frame = v.obtenerVideo(camara)

        #Procesar imagenes del video
        improcesada = pi.procesarImagen(frame)


        """Se detecta la cara del video, luego se activa las redes neuronales para detectar
           los estados de somnolencia y atencion en el conductor"""

        cara = d.deteccionFacial(improcesada)
        if cara == None:
            """Si el sistema no encuentra ninguna cara debera generar una notificacion de sonido
               para avisar que hay algun problema"""
            #time.sleep(15)
            #a.deteccionNula()
        else:

            Somnolencia = rn.estimularRN(red_somnolencia,cara.flatten())
            Atencion = rn.estimularRN(red_atento,cara.flatten())

            """Se ingresan los valores obtenidos al bloque difusor el cual generara las
               alarmas en los casos que convengan."""
            estado = a.motorDifuso(Somnolencia,Atencion)
            print "Estado de la alarma", estado
            a.alertar(estado)


if __name__ == "__main__":
    main()
