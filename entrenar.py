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

    for i,c in enumerate(os.listdir(os.path.dirname('/home/taberu/Imágenes/img_tesis/somnoliento/'))):
        im = cv2.imread('/home/taberu/Imágenes/img_tesis/somnoliento/'+c)
        pim = pi.procesarImagen(im)
        cara = d.deteccionFacial(pim)
        if cara == None:
            print "No hay cara"
        else:
            print i
            ds.appendLinked(cara.flatten(),10)

    print ds
    print ds['input']
    trainer = BackpropTrainer(red, ds)
    print "Entrenando hasta converger"
    print trainer.trainUntilConvergence()
    NetworkWriter.writeToFile(red, 'rna_somnolencia.xml')

def entrenarOjos(red):
    #Se inicializa el dataset
    ds = SupervisedDataSet(4096,1)

    """Se crea el dataset, para ello procesamos cada una de las imagenes obteniendo los rostros,
       luego se le asignan los valores deseados del resultado la red neuronal."""

    print "Guardando ojo izquierdo"
    for i,c in enumerate(os.listdir(os.path.dirname('/home/taberu/Imágenes/img_tesis/ojos_cerrados/'))):
        im = cv2.imread('/home/taberu/Imágenes/img_tesis/ojos_cerrados/'+c)
        pim = pi.procesarImagen(im)

        ojoiz = d.deteccionOjoIzquierdo(pim)
        if ojoiz == None:
            print "No hay ojo"
        else:
            print i
            ds.appendLinked(ojoiz.flatten(),10)

    print "Guardando ojo derecho"
    for j,b in enumerate(os.listdir(os.path.dirname('/home/taberu/Imágenes/img_tesis/ojos_cerrados/'))):
        imb = cv2.imread('/home/taberu/Imágenes/img_tesis/ojos_cerrados/'+c)
        pimb = pi.procesarImagen(imb)

        ojode = d.deteccionOjoDerecho(pimb)
        if ojode == None:
            print "No hay ojo"
        else:
            print i
            ds.appendLinked(ojode.flatten(),10)

    print ds
    print ds['input']
    trainer = BackpropTrainer(red, ds)
    print "Entrenando hasta converger"
    print trainer.trainUntilConvergence()
    NetworkWriter.writeToFile(red, 'rna_ojos.xml')

