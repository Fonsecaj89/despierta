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

    #print "Distraido - cara"
    #for i,dc in enumerate(os.listdir(os.path.dirname('/home/taberu/Imágenes/img_tesis/distraido/color/'))):
        #print dc
        #try:
            #im1 = cv2.imread('/home/taberu/Imágenes/img_tesis/distraido/color/'+dc)
            #pim1 = pi.procesarImagen(im1)
            #cara1 = d.deteccionFacial(pim1)
            #if cara1 == None:
                #print "No hay cara"
            #else:
                #print i
                #ds.appendLinked(cara1.flatten(),5)
        #except:
            #pass
    #for i,dbn in enumerate(os.listdir(os.path.dirname('/home/taberu/Imágenes/img_tesis/distraido/bn/'))):
        #print dbn
        #try:
            #im2 = cv2.imread('/home/taberu/Imágenes/img_tesis/distraido/bn/'+dbn)
            #cara2 = d.deteccionFacial(im2)
            #if cara2 == None:
                #print "No hay cara"
            #else:
                #print i
                #ds.appendLinked(cara2.flatten(),5)
        #except:
            #pass

    #print "Atento - cara"
    #for i,e in enumerate(os.listdir(os.path.dirname('/home/taberu/Imágenes/img_tesis/atento/color/'))):
        #print e
        #try:
            #im3 = cv2.imread('/home/taberu/Imágenes/img_tesis/atento/color/'+e)
            #pim3 = pi.procesarImagen(im3)
            #cara3 = d.deteccionFacial(pim3)
            #if cara3 == None:
                #print "No hay cara"
            #else:
                #print i
                #ds.appendLinked(cara3.flatten(),0)
        #except:
            #pass
    #for i,e1 in enumerate(os.listdir(os.path.dirname('/home/taberu/Imágenes/img_tesis/atento/bn/'))):
        #print e1
        #try:
            #im4 = cv2.imread('/home/taberu/Imágenes/img_tesis/atento/bn/'+e1)
            #cara4 = d.deteccionFacial(im4)
            #if cara4 == None:
                #print "No hay cara"
            #else:
                #print i
                #ds.appendLinked(cara4.flatten(),0)
        #except:
            #pass

    print ds
    print ds['input']
    trainer = BackpropTrainer(red, ds)
    print "Entrenando hasta converger"
    trainer.trainUntilConvergence()
    NetworkWriter.writeToFile(red, 'rna_somnolencia.xml')



def entrenarAtento(red):
    #Se inicializa el dataset
    ds = SupervisedDataSet(4096,1)

    """Se crea el dataset, para ello procesamos cada una de las imagenes obteniendo los rostros,
       luego se le asignan los valores deseados del resultado la red neuronal."""

    #print "Somnolencia - cara"
    #for i,c in enumerate(os.listdir(os.path.dirname('/home/taberu/Imágenes/img_tesis/somnoliento/'))):
        #try:
            #im = cv2.imread('/home/taberu/Imágenes/img_tesis/somnoliento/'+c)
            #pim = pi.procesarImagen(im)
            #cara = d.deteccionFacial(pim)
            #if cara == None:
                #print "No hay cara"
            #else:
                #print i
                #ds.appendLinked(cara.flatten(),0)
        #except:
            #pass

    #print "Distraido - cara"
    #for i,dc in enumerate(os.listdir(os.path.dirname('/home/taberu/Imágenes/img_tesis/distraido/color/'))):
        #print dc
        #try:
            #im1 = cv2.imread('/home/taberu/Imágenes/img_tesis/distraido/color/'+dc)
            #pim1 = pi.procesarImagen(im1)
            #cara1 = d.deteccionFacial(pim1)
            #if cara1 == None:
                #print "No hay cara"
            #else:
                #print i
                #ds.appendLinked(cara1.flatten(),5)
        #except:
            #pass
    #for i,dbn in enumerate(os.listdir(os.path.dirname('/home/taberu/Imágenes/img_tesis/distraido/bn/'))):
        #print dbn
        #try:
            #im2 = cv2.imread('/home/taberu/Imágenes/img_tesis/distraido/bn/'+dbn)
            #cara2 = d.deteccionFacial(im2)
            #if cara2 == None:
                #print "No hay cara"
            #else:
                #print i
                #ds.appendLinked(cara2.flatten(),5)
        #except:
            #pass

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

    print ds
    print ds['input']
    trainer = BackpropTrainer(red, ds)
    print "Entrenando hasta converger"
    trainer.trainUntilConvergence()
    NetworkWriter.writeToFile(red, 'rna_atento.xml')


def entrenarOjos(red):
    #Se inicializa el dataset
    ds = SupervisedDataSet(4096,1)

    """Se crea el dataset, para ello procesamos cada una de las imagenes obteniendo los rostros,
       luego se le asignan los valores deseados del resultado la red neuronal."""

    print "Guardando ojo izquierdo"
    for i,c in enumerate(os.listdir(os.path.dirname('/home/taberu/Imágenes/img_tesis/ojos_cerrados/'))):
        try:
            im = cv2.imread('/home/taberu/Imágenes/img_tesis/ojos_cerrados/'+c)
            pim = pi.procesarImagen(im)
            ojoiz = d.deteccionOjoIzquierdo(pim)
            if ojoiz == None:
                print "No hay ojo"
            else:
                print i
                ds.appendLinked(ojoiz.flatten(),10)
        except:
            pass

    print "Guardando ojo derecho"
    for j, b in enumerate(os.listdir(os.path.dirname('/home/taberu/Imágenes/img_tesis/ojos_cerrados/'))):
        try:
            imb = cv2.imread('/home/taberu/Imágenes/img_tesis/ojos_cerrados/'+b)
            pimb = pi.procesarImagen(imb)
            ojode = d.deteccionOjoDerecho(pimb)
            if ojode == None:
                print "No hay ojo"
            else:
                print i
                ds.appendLinked(ojode.flatten(),10)
        except:
            pass

    for i,c1 in enumerate(os.listdir(os.path.dirname('/home/taberu/Imágenes/img_tesis/distraido/'))):
        try:
            im1 = cv2.imread('/home/taberu/Imágenes/img_tesis/ojos_cerrados/'+c1)
            pim1 = pi.procesarImagen(im1)
            ojoiz1 = d.deteccionOjoIzquierdo(pim1)
            if ojoiz1 == None:
                print "No hay ojo"
            else:
                print i
                ds.appendLinked(ojoiz1.flatten(),5)
        except:
            pass

    print "Guardando ojo derecho"
    for j,b1 in enumerate(os.listdir(os.path.dirname('/home/taberu/Imágenes/img_tesis/distraido/'))):
        try:
            imb1 = cv2.imread('/home/taberu/Imágenes/img_tesis/ojos_cerrados/'+b1)
            pimb1 = pi.procesarImagen(imb1)

            ojode1 = d.deteccionOjoDerecho(pimb1)
            if ojode1 == None:
                print "No hay ojo"
            else:
                print i
                ds.appendLinked(ojode1.flatten(),5)
        except:
            pass

    for i,c2 in enumerate(os.listdir(os.path.dirname('/home/taberu/Imágenes/img_tesis/atento/'))):
        try:
            im2 = cv2.imread('/home/taberu/Imágenes/img_tesis/ojos_cerrados/'+c2)
            pim2 = pi.procesarImagen(im2)
            ojoiz2 = d.deteccionOjoIzquierdo(pim2)
            if ojoiz2 == None:
                print "No hay ojo"
            else:
                print i
                ds.appendLinked(ojoiz2.flatten(),5)
        except:
            pass

    print "Guardando ojo derecho"
    for j,b2 in enumerate(os.listdir(os.path.dirname('/home/taberu/Imágenes/img_tesis/atento/'))):
        try:
            imb2 = cv2.imread('/home/taberu/Imágenes/img_tesis/ojos_cerrados/'+b2)
            pimb2 = pi.procesarImagen(imb2)
            ojode2 = d.deteccionOjoDerecho(pimb2)
            if ojode2 == None:
                print "No hay ojo"
            else:
                print i
                ds.appendLinked(ojode2.flatten(),5)
        except:
            pass
    print ds
    print ds['input']
    trainer = BackpropTrainer(red, ds)
    print "Entrenando hasta converger"
    trainer.trainUntilConvergence()
    NetworkWriter.writeToFile(red, 'rna_ojos.xml')

