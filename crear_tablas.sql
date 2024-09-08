--CREATE DATABASE Evidencia4_DB
--GO
--use Evidencia4_DB
--GO
CREATE TABLE Intensidad(
	IdIntensidad int IDENTITY (1,1),
	ValorIntensidad int null,
	IntensidadBaja int not null,
	IntensidadMedia int not null,
	IntensidadAlta int not null
	CONSTRAINT IdIntensidad PRIMARY KEY(IdIntensidad)
);
GO
CREATE TABLE LamparaQuirurjica(
	IdLampara int IDENTITY (1,1), --IDENTITY (1,1) autoincremental comienza en 1 y aumente de a 1 
	Marca varchar(20) not null,
	Modelo varchar(20) not null,
	Color varchar(20) null,
	Encendido bit null,
	Apagado bit null,
	IdIntensidad int,
	CONSTRAINT IdLampara PRIMARY KEY(IdLampara),
	CONSTRAINT FK_Intensidad FOREIGN KEY (IdIntensidad) REFERENCES Intensidad(IdIntensidad) --creación de FK
);

