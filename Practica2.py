def creacion_dicci(notas_1, notas_2, nombres):
    notas_total=zip(notas_1,notas_2)
    alumnos=dict(zip(nombres,notas_total))
    return(alumnos)

def promedio_maximo(promedio):
    return (max(promedio, key = promedio.get))

def nota_minima(alumnos):
    return (min(alumnos, key=lambda x:min(alumnos[x][0], alumnos[x][1])))

nombres = ['Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás',  'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina']

notas_1 = [81,  60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 
           12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 
           85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
           64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
           95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

promedio={}
alumnos=creacion_dicci(notas_1,notas_2,nombres)
promedio_total=0

for elem in alumnos:
    promedio[elem] = alumnos[elem][0]+alumnos[elem][1]
    promedio_total=promedio_total+promedio[elem]

promedio_total=promedio_total/len(alumnos)

print(alumnos)
print(f"El/la estudiante con la nota promedio mas alta es {promedio_maximo(promedio)}")
print(f"El/la estudiante con la nota mas baja es {nota_minima(alumnos)}")