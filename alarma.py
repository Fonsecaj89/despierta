# -*- coding: utf-8 -*-
import pyglet
from fuzzy import LogicaDifusa as ld

class Alarma:

    def __init__(self):
        self.auxs = 0
        self.auxd = 0
        self.somnolencia = ""
        self.atencion = ""
        self.estado = ""
        self.esres = ""
        self.aux = False
        self.reglas = ld.iniReglas()
        self.iniBloqueDifusor()


    def iniBloqueDifusor(self):
        self.somnolencia = ld.declararConjunto("Somnolencia",0.00000,10.00000)
        ld.variableLinguistica(self.somnolencia,"Pocas")
        ld.variableLinguistica(self.somnolencia,"Intermedias")
        ld.variableLinguistica(self.somnolencia,"Dormido")

        ld.asignarFuncionPertenencia(self.somnolencia,0,"Triangular",(0.00000,02.50000,05.00000))
        ld.asignarFuncionPertenencia(self.somnolencia,1,"Triangular",(02.50001,05.00001,07.50000))
        ld.asignarFuncionPertenencia(self.somnolencia,2,"Triangular",(05.00002,07.50001,10.00000))


        self.atencion = ld.declararConjunto("Atento",0.00000,10.00000)
        ld.variableLinguistica(self.atencion,"Poco")
        ld.variableLinguistica(self.atencion,"Moderado")
        ld.variableLinguistica(self.atencion,"Atento")

        ld.asignarFuncionPertenencia(self.atencion,0,"Triangular",(0.00000,02.50000,05.00000))
        ld.asignarFuncionPertenencia(self.atencion,1,"Triangular",(02.500001,05.00001,07.50000))
        ld.asignarFuncionPertenencia(self.atencion,2,"Triangular",(05.00002,07.50001,10.00000))


        self.estado = ld.declararConjunto("Estado",0.00000,5.00000)
        ld.variableLinguistica(self.estado,"Atento")
        ld.variableLinguistica(self.estado,"Distraido")
        ld.variableLinguistica(self.estado,"Somnoliento")
        ld.variableLinguistica(self.estado,"Dormido")

        ld.asignarFuncionPertenencia(self.estado,0,"Triangular",(0.00000,1.00000,2.00000))
        ld.asignarFuncionPertenencia(self.estado,1,"Triangular",(1.00001,2.00001,3.00000))
        ld.asignarFuncionPertenencia(self.estado,2,"Triangular",(2.00002,3.00001,4.00000))
        ld.asignarFuncionPertenencia(self.estado,3,"Triangular",(3.00002,4.00001,5.00000))


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
        if Somnolencia<0.00000:
           Somnolencia = 0.00001
        if Somnolencia>10:
           Somnolencia = 9.99999
        if Atencion<0.00000:
           Atencion = 0.00001
        if Atencion>10:
           Atencion = 9.99999
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
        def exiter(dt):
            pyglet.app.exit()
        pyglet.clock.schedule_once(exiter, song.duration)
        pyglet.app.run()

    def deteccionNula(self):
        """Informa al usuario que el sistema no detecta ningun rostro"""
        song = pyglet.media.load('error.mp3')
        song.play()
        def exiter(dt):
            pyglet.app.exit()
        pyglet.clock.schedule_once(exiter, song.duration)
        pyglet.app.run()

    def distraido(self):
        if self.auxd == 10:
            song = pyglet.media.load('a2.mp3')
            song.play()
            def exiter(dt):
                pyglet.app.exit()
            pyglet.clock.schedule_once(exiter, song.duration)
            pyglet.app.run()
        else:
            self.auxd = self.auxd + 1

    def somnoliento(self):
        if self.auxs == 10:
            song = pyglet.media.load('a2-2.mp3')
            song.play()
            def exiter(dt):
                pyglet.app.exit()
            pyglet.clock.schedule_once(exiter, song.duration)
            pyglet.app.run()
        else:
            self.auxs = self.auxs + 1

    def inicio(self):
        song = pyglet.media.load('ok.mp3')
        song.play()
        def exiter(dt):
            pyglet.app.exit()
        pyglet.clock.schedule_once(exiter, song.duration)
        pyglet.app.run()
