# -*- coding: utf-8 -*-
import os
import cv2
import paralelo as p
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

    #Crear Red Neuronal
    red1 = rn.crearRN()
    red2 = rn.crearRN()
    red3 = rn.crearRN()

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

    #if os.path.isfile(path + '/rna_ojos.xml'):
        #red_ojos = NetworkReader.readFrom('rna_ojos.xml')
    #else:
        #e.entrenarOjos(red3)
        #red_ojos = NetworkReader.readFrom('rna_ojos.xml')


    #Se la camara con la que se va a trabajar
    try:
        camara = v.capturarVideo()
    except:
        a.noCamara()


    while True:
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
            a.deteccionNula()
        else:

            Somnolencia = rn.estimularRN(red_somnolencia,cara.flatten())
            Atencion = rn.estimularRN(red_atento,cara.flatten())
            print "somnolencia", Somnolencia, "atento", Atencion

        #ojo_izq = d.deteccionOjoIzquierdo(improcesada)
        #if ojo_izq == None:
           #"""Si el sistema no encuentra ninguna cara debera generar una notificacion de sonido
              #para avisar que hay algun problema"""
           #a.deteccionNula()
        #else:
            #resultado = rn.estimularRN(red_ojos,ojo_izq.flatten())
            #print "ojo izquierdo", resultado

        #ojo_der = d.deteccionOjoDerecho(improcesada)
        #if ojo_der == None:
           #"""Si el sistema no encuentra ninguna cara debera generar una notificacion de sonido
              #para avisar que hay algun problema"""
           #a.deteccionNula()
        #else:
            #resultado = rn.estimularRN(red_ojos,ojo_der.flatten())
            #print "ojo derecho", resultado


        #hilo_cara = p.hiloCara(improcesada,red1,a)
        #hilo_cara.start()
        #res_cara = hilo_cara.join()
        #resultado = hilo_cara.resultado
        #print res_cara, resultado

        #hilo_ojoiz = p.hiloOjoIz(improcesada,red2,a)
        #hilo_ojoiz.start()
        #res_ojoiz = hilo_ojoiz.join()

        #hilo_ojode = p.hiloOjoDe(improcesada,red2,a)
        #hilo_ojode.start()
        #res_ojode = hilo_ojode.join()


        """Se ingresan los valores obtenidos al bloque difusor el cual generara las
           alarmas en los casos que convengan."""
        a.motorDifuso(Somnolencia,Atencion)




        #Mostrar Resultados
        nombreOriginal = "Reconocimiento del Estado Facial de Somnolencia"
        v.mostrarVideo(nombreOriginal,frame)

        key = cv2.waitKey(10)
        if key==27:
          break
          camara.release()


if __name__ == "__main__":
    main()
