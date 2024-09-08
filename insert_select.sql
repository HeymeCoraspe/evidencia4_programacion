insert into Intensidad values (0, 40, 70, 100)
insert into LamparaQuirurjica (Marca, Modelo, Color, Encendido, Apagado) values ('LG', 'BHF-987','black', 0, 1)
insert into LamparaQuirurjica (Marca, Modelo, Color, Encendido, Apagado) values ('SAMSUNG', 'AE-87','black', 0, 1)
insert into LamparaQuirurjica (Marca, Modelo, Color, Encendido, Apagado) values ('BGH', 'AIR9','WHITE', 0, 1)
insert into LamparaQuirurjica (Marca, Modelo, Color) values ('PHILLIPS', 'LED76a','WHITE')
insert into LamparaQuirurjica (Marca, Modelo, Color) values ('SAMSUNG', 'AE-87','black')
insert into LamparaQuirurjica (Marca, Modelo, Color, Encendido, Apagado) values ('LG', 'URX-30','WHITE', 0, 1)
insert into LamparaQuirurjica (Marca, Modelo, Color) values ('PHILLIPS', 'LED45a','GREY')
insert into Intensidad values (0, 30, 60, 90)
INSERT INTO Intensidad (ValorIntensidad, IntensidadBaja, IntensidadMedia,IntensidadAlta) VALUES (0, 25, 55, 85)


select * from Intensidad
select * from LamparaQuirurjica
SELECT * FROM LamparaQuirurjica WHERE Modelo LIKE '%LED%'
SELECT * FROM LamparaQuirurjica WHERE IdLampara=6
SELECT * FROM LamparaQuirurjica WHERE Color LIKE 'WH%' AND Marca LIKE 'PH%'
SELECT * FROM Intensidad WHERE IntensidadBaja > 30
SELECT * FROM Intensidad WHERE IntensidadBaja >30 OR IntensidadAlta>=90
