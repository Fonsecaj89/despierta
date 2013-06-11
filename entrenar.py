# -*- coding: utf-8 -*-
import os
import cv2
import deteccion as d
import procesarImagen as pi
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.xml.networkwriter import NetworkWriter

def entrenarSomnolencia(red):
    #Se inicializa el dataset
    ds = SupervisedDataSet(4096,1)

    """Se crea el dataset, para ello procesamos cada una de las imagenes obteniendo los rostros,
       luego se le asignan los valores deseados del resultado la red neuronal."""

    print "Somnolencia - cara"
    for i,c in enumerate(os.listdir(os.path.dirname('/home/taberu/Imágenes/img_tesis/somnoliento/'))):
        try:
            im = cv2.imread('/home/taberu/Imágenes/img_tesis/somnoliento/'+c)
            pim = pi.procesarImagen(im)
            cara = d.deteccionFacial(pim)
            if cara == None:
                print "No hay cara"
            else:
                print i
                ds.appendLinked(cara.flatten(),10)
        except:
            pass

    trainer = BackpropTrainer(red, ds)
    print "Entrenando hasta converger"
    trainer.trainUntilConvergence()
    NetworkWriter.writeToFile(red, 'rna_somnolencia.xml')



def entrenarAtento(red):
    #Se inicializa el dataset
    ds = SupervisedDataSet(4096,1)

    """Se crea el dataset, para ello procesamos cada una de las imagenes obteniendo los rostros,
       luego se le asignan los valores deseados del resultado la red neuronal."""


    print "Atento - cara"
    for i,e in enumerate(os.listdir(os.path.dirname('/home/taberu/Imágenes/img_tesis/atento/color/'))):
        print e
        try:
            im3 = cv2.imread('/home/taberu/Imágenes/img_tesis/atento/color/'+e)
            pim3 = pi.procesarImagen(im3)
            cara3 = d.deteccionFacial(pim3)
            if cara3 == None:
                print "No hay cara"
            else:
                print i
                ds.appendLinked(cara3.flatten(),10)
        except:
            pass
    for i,e1 in enumerate(os.listdir(os.path.dirname('/home/taberu/Imágenes/img_tesis/atento/bn/'))):
        print e1
        try:
            im4 = cv2.imread('/home/taberu/Imágenes/img_tesis/atento/bn/'+e1)
            cara4 = d.deteccionFacial(im4)
            if cara4 == None:
                print "No hay cara"
            else:
                print i
                ds.appendLinked(cara4.flatten(),10)
        except:
            pass

    trainer = BackpropTrainer(red, ds)
    print "Entrenando hasta converger"
    trainer.trainUntilConvergence()
    NetworkWriter.writeToFile(red, 'rna_atento.xml')


