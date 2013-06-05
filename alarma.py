# -*- coding: utf-8 -*-
import pyglet
from fuzzy import LogicaDifusa as ld

class Alarma:

    def __init__(self):
        self.somnolencia = ""
        self.atencion = ""
        self.estado = ""
        self.reglas = ld.iniReglas()
        self.iniBloqueDifusor()


    def iniBloqueDifusor(self):
        self.somnolencia = ld.declararConjunto("Somnolencia",0.00,1.00)
        ld.variableLinguistica(self.somnolencia,"Pocas")
        ld.variableLinguistica(self.somnolencia,"Intermedias")
        ld.variableLinguistica(self.somnolencia,"Muchas")

        ld.asignarFuncionPertenencia(self.somnolencia,0,"Triangular",(0.00,0.250,0.500))
        ld.asignarFuncionPertenencia(self.somnolencia,1,"Triangular",(0.251,0.501,0.750))
        ld.asignarFuncionPertenencia(self.somnolencia,2,"Triangular",(0.502,0.751,0.100))


        self.atencion = ld.declararConjunto("Atento",0.00,1.00)
        ld.variableLinguistica(self.atencion,"Poco")
        ld.variableLinguistica(self.atencion,"Moderado")
        ld.variableLinguistica(self.atencion,"Excesivo")

        ld.asignarFuncionPertenencia(self.atencion,0,"Triangular",(0.00,0.250,0.500))
        ld.asignarFuncionPertenencia(self.atencion,1,"Triangular",(0.251,0.501,0.750))
        ld.asignarFuncionPertenencia(self.atencion,2,"Triangular",(0.502,0.751,0.100))



        self.estado = ld.declararConjunto("Estado",0.0,0.4)
        ld.variableLinguistica(self.estado,"Poco")
        ld.variableLinguistica(self.estado,"Moderado")
        ld.variableLinguistica(self.estado,"Mucho")

        ld.asignarFuncionPertenencia(self.estado,0,"Triangular",(0,1,2))
        ld.asignarFuncionPertenencia(self.estado,1,"Triangular",(1.01,2.01,3))
        ld.asignarFuncionPertenencia(self.estado,2,"Triangular",(2.02,3.01,4))


        #ld.crearReglas(self.reglas,"if Calorias_Quemadas is Pocas and Sudor_Perdido is Poco then Liquido is Poco")
        #ld.crearReglas(self.reglas,"if Calorias_Quemadas is Intermedias and Sudor_Perdido is Poco then Liquido is Poco")
        #ld.crearReglas(self.reglas,"if Calorias_Quemadas is Muchas and Sudor_Perdido is Poco then Liquido is Moderado")

        #ld.crearReglas(self.reglas,"if Calorias_Quemadas is Pocas and Sudor_Perdido is Moderado then Liquido is Poco")
        #ld.crearReglas(self.reglas,"if Calorias_Quemadas is Intermedias and Sudor_Perdido is Moderado then Liquido is Moderado")
        #ld.crearReglas(self.reglas,"if Calorias_Quemadas is Muchas and Sudor_Perdido is Moderado then Liquido is Moderado")

        #ld.crearReglas(self.reglas,"if Calorias_Quemadas is Pocas and Sudor_Perdido is Excesivo then Liquido is Moderado")
        #ld.crearReglas(self.reglas,"if Calorias_Quemadas is Intermedias and Sudor_Perdido is Excesivo then Liquido is Mucho")
        #ld.crearReglas(self.reglas,"if Calorias_Quemadas is Muchas and Sudor_Perdido is Excesivo then Liquido is Mucho")

    def motorDifuso(self,Somnolencia,Atencion):
        fsomnolencia = ld.fusificar(Somnolencia,self.somnolencia)
        fatencion = ld.fusificar(Atencion,self.atencion)


        motor = ld.inicializarMotor()
        ld.agregarAlMotor(motor,self.somnolencia,fsomnolencia)
        ld.agregarAlMotor(motor,self.atencion,fatencion)

        resultado = ld.procesar(self.reglas,motor,self.estado)
        return resultado

    def alertar():
        pass

    def deteccionNula(self):
        """Informa al usuario que el sistema no detecta ningun rostro"""
        #song = pyglet.media.load('directoria del audio')
        #song.play()
        #pyglet.app.run()
        pass

    def distraido(self):
        pass

    def somnoliento(self):
        pass