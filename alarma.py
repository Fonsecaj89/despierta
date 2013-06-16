# -*- coding: utf-8 -*-
import pyglet
from fuzzy import LogicaDifusa as ld

class Alarma:

    def __init__(self):
        self.somnolencia = ""
        self.atencion = ""
        self.estado = ""
        self.esres = ""
        self.aux = False
        self.reglas = ld.iniReglas()
        self.iniBloqueDifusor()


    def iniBloqueDifusor(self):
        self.somnolencia = ld.declararConjunto("Somnolencia",0.00,10.00)
        ld.variableLinguistica(self.somnolencia,"Pocas")
        ld.variableLinguistica(self.somnolencia,"Intermedias")
        ld.variableLinguistica(self.somnolencia,"Dormido")

        ld.asignarFuncionPertenencia(self.somnolencia,0,"Triangular",(0.00,02.50,05.00))
        ld.asignarFuncionPertenencia(self.somnolencia,1,"Triangular",(02.51,05.01,07.50))
        ld.asignarFuncionPertenencia(self.somnolencia,2,"Triangular",(05.02,07.51,10.00))


        self.atencion = ld.declararConjunto("Atento",0.00,10.00)
        ld.variableLinguistica(self.atencion,"Poco")
        ld.variableLinguistica(self.atencion,"Moderado")
        ld.variableLinguistica(self.atencion,"Atento")

        ld.asignarFuncionPertenencia(self.atencion,0,"Triangular",(0.00,02.50,05.00))
        ld.asignarFuncionPertenencia(self.atencion,1,"Triangular",(02.51,05.01,07.50))
        ld.asignarFuncionPertenencia(self.atencion,2,"Triangular",(05.02,07.51,10.00))


        self.estado = ld.declararConjunto("Estado",0.00,5.00)
        ld.variableLinguistica(self.estado,"Atento")
        ld.variableLinguistica(self.estado,"Distraido")
        ld.variableLinguistica(self.estado,"Somnoliento")
        ld.variableLinguistica(self.estado,"Dormido")

        ld.asignarFuncionPertenencia(self.estado,0,"Triangular",(0.00,1.00,2.00))
        ld.asignarFuncionPertenencia(self.estado,1,"Triangular",(1.01,2.01,3.00))
        ld.asignarFuncionPertenencia(self.estado,2,"Triangular",(2.02,3.01,4.00))
        ld.asignarFuncionPertenencia(self.estado,3,"Triangular",(3.02,4.01,5.00))


        ld.crearReglas(self.reglas,"if Somnolencia is Pocas and Atento is Poco then Estado is Distraido")
        ld.crearReglas(self.reglas,"if Somnolencia is Intermedias and Atento is Poco then Estado is Distraido")
        ld.crearReglas(self.reglas,"if Somnolencia is Dormido and Atento is Poco then Estado is Dormido")

        ld.crearReglas(self.reglas,"if Somnolencia is Pocas and Atento is Moderado then Estado is Distraido")
        ld.crearReglas(self.reglas,"if Somnolencia is Intermedias and Atento is Moderado then Estado is Somnoliento")
        ld.crearReglas(self.reglas,"if Somnolencia is Dormido and Atento is Moderado then Estado is Dormido")

        ld.crearReglas(self.reglas,"if Somnolencia is Pocas and Atento is Atento then Estado is Atento")
        ld.crearReglas(self.reglas,"if Somnolencia is Intermedias and Atento is Atento then Estado is Somnoliento")
        ld.crearReglas(self.reglas,"if Somnolencia is Dormido and Atento is Atento then Estado is Dormido")

    def motorDifuso(self,Somnolencia,Atencion):
        fsomnolencia = ld.fusificar(Somnolencia,self.somnolencia)
        fatencion = ld.fusificar(Atencion,self.atencion)


        motor = ld.inicializarMotor()
        ld.agregarAlMotor(motor,self.somnolencia,fsomnolencia)
        ld.agregarAlMotor(motor,self.atencion,fatencion)

        resultado = ld.procesar(self.reglas,motor,self.estado)
        return resultado

    def alertar(self,resultado):
        estado, val = resultado

        if not self.aux:
            self.aux = True
        else:
            if estado == "Distraido":
                self.distraido()
            if estado == "Somnoliento":
                self.somnoliento()
            if estado == "Dormido":
                self.somnoliento()


    def noCamara(self):
        song = pyglet.media.load('error.mp3')
        song.play()
        song.on_eos = lambda: pyglet.app.exit()
        pyglet.app.run()

    def deteccionNula(self):
        """Informa al usuario que el sistema no detecta ningun rostro"""
        song = pyglet.media.load('error.mp3')
        song.play()
        song.on_eos = lambda: pyglet.app.exit()
        pyglet.app.run()

    def distraido(self):
        song = pyglet.media.load('a2.mp3')
        song.play()
        song.on_eos = lambda: pyglet.app.exit()
        pyglet.app.run()

    def somnoliento(self):
        song = pyglet.media.load('a2-2.mp3')
        song.play()
        song.on_eos = lambda: pyglet.app.exit()
        pyglet.app.run()

    def inicio(self):
        song = pyglet.media.load('ok.mp3')
        song.play()
        song.on_eos = lambda: pyglet.app.exit()
        pyglet.app.run()
        print "lista"