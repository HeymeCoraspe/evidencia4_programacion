import pytest
from LAMPARA_QUIRURJICA_CLASS import LamparaQuirurjica

def test_inicializacion():
    lampara = LamparaQuirurjica(50, "LG", "HC-16", "Negro")
    assert lampara.marca == "LG"
    assert lampara.modelo == "HC-16"
    assert lampara.color == "Negro"
    assert lampara.intensidad == 50
    assert lampara.encendido

def test_encender_lampara():
    lampara = LamparaQuirurjica(0, "LG", "HC-16", "Negro")
    lampara.encendido = False
    resultado = lampara.encender_lampara()
    assert lampara.encendido  
    assert lampara.intensidad == lampara.intensidadMedia 
    assert resultado == f" Lampara encendida, intensidad: {lampara.intensidadMedia}%"

def test_apagar_lampara():
    lampara = LamparaQuirurjica(50, "LG", "HC-16", "Negro")
    resultado = lampara.apagar_lampara()
    assert not lampara.encendido  
    assert lampara.intensidad == 0  
    assert resultado == " Lampara apagada"

def test_mostrar_intensidad_baja():
    lampara = LamparaQuirurjica(30, "LG", "HC-16", "Negro")
    resultado = lampara.mostrar_intensidad()
    assert resultado == " Intensidad baja: 30%"

def test_mostrar_intensidad_media():
    lampara = LamparaQuirurjica(70, "LG", "HC-16", "Negro")
    resultado = lampara.mostrar_intensidad()
    assert resultado == " Intensidad media: 70%"

def test_mostrar_intensidad_alta():
    lampara = LamparaQuirurjica(90, "LG", "HC-16", "Negro")
    resultado = lampara.mostrar_intensidad()
    assert resultado == " Intensidad alta: 90%"


##IMPLEMENTAR CLASE
class LamparaQuirurjica:
    def __init__(self, intensidad, marca=None, modelo=None, color=None, encendido=True,
                 intensidadBaja=40, intensidadMedia=70, intensidadAlta=100):
        
        self.intensidad = intensidad
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = encendido
        self.intensidadBaja = intensidadBaja
        self.intensidadMedia = intensidadMedia
        self.intensidadAlta = intensidadAlta

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}"

    def encender_lampara(self):
        if not self.encendido:
            self.encendido = True
            self.intensidad = self.intensidadMedia
            return f" Lampara encendida, intensidad: {self.intensidadMedia}%"
        else:
            return f" Lampara encendida, intensidad: {self.intensidad}%"

    def apagar_lampara(self):
        self.encendido = False
        self.intensidad = 0
        return " Lampara apagada"

    def mostrar_intensidad(self):
        if self.intensidad <= 40:
            return f" Intensidad baja: {self.intensidad}%"
        elif self.intensidad > 40 and self.intensidad <= 80:
            return f" Intensidad media: {self.intensidad}%"
        elif self.intensidad > 80 and self.intensidad <= 100:
            return f" Intensidad alta: {self.intensidad}%"
        else:
            return " Intensidad no permitida, la máxima es 100%"
