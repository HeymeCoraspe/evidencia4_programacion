class LamparaQuirurjica:
	def __init__(self, marca=None, modelo=None, color=None, intensidad=0, encendido=True,
			  intensidadBaja=40, intensidadMedia=70, intensidadAlta=100):
		
		self.intensidad=intensidad
		self.marca=marca
		self.modelo=modelo
		self.color=color
		self.encendido=encendido
		self.intensidadBaja=intensidadBaja
		self.intensidadMedia=intensidadMedia
		self.intensidadAlta=intensidadAlta
		
#Método que muestra las características de la lámpara 
	def __str__(self):
		return (f" Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}")

#métodos para acciones de la lámpara
	def encender_lampara(self):
		if not self.encendido:
			self.encendido=True
			self.intensidad=self.intensidadMedia
			return (" Lámpara apagada")
		else:
			return(f" Lampara encendida, intensidad: {self.intensidadMedia}%")

	def apagar_lampara(self):	
			self.encendido=False
			self.intensidad=0
			return (" Lampara apagada")

	def mostrar_intensidad(self):
		if self.intensidad <= 40:
			return(f" Intensidad baja: {self.intensidad}%")
		elif self.intensidad > 40 and self.intensidad <=80:
			return(f" Intensidad media: {self.intensidad}%")
		elif self.intensidad > 80 and self.intensidad <=100:
			return(f" Intensidad alta: {self.intensidad}%")
		elif self.intensidad >100:
			return(" Intensidad no permitida, la máxima es 100%")
	
	def configurar_intensidad(self):	
		valorIntensidad=int(input(" Ingrese 1 para intensidad baja, 2 para media y 3 para alta: "))
		if valorIntensidad== 1:
			return(f" Intensidad configurada en {valorIntensidad}: {self.intensidadBaja}%")
		elif valorIntensidad== 2:
			return(f" Intensidad configurada en {valorIntensidad}: {self.intensidadMedia}%")
		elif valorIntensidad== 3:
			return(f" Intensidad configurada en {valorIntensidad}: {self.intensidadAlta}%")
		else:
			return(" Valor de intensidad invalido")


#Instancia
if __name__ == "__main__":	
	miLampara=LamparaQuirurjica("LG","HC-16","Negro")
	#miLampara=LamparaQuirurjica(120)

print(miLampara.__str__())
#print(miLampara.encender_lampara())
#print(miLampara.apagar_lampara())
#print(miLampara.mostrar_intensidad())
#print(miLampara.configurar_intensidad())