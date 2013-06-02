# -*- coding: utf-8 -*-
import pyglet


class Alarma:

    def __init__(self):
        self.estado = ""
        self.iniBloqueDifusor()


    def iniBloqueDifusor(self):
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