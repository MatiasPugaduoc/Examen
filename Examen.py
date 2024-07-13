import csv
import random

Respuesta=0


#Generacion de sueldos

sueldo1=int(random.randint(300000,2500000))
sueldo2=int(random.randint(300000,2500000)) 
sueldo3=int(random.randint(300000,2500000)) 
sueldo4=int(random.randint(300000,2500000)) 
sueldo5=int(random.randint(300000,2500000)) 
sueldo6=int(random.randint(300000,2500000)) 
sueldo7=int(random.randint(300000,2500000)) 
sueldo8=int(random.randint(300000,2500000)) 
sueldo9=int(random.randint(300000,2500000)) 
sueldo10=int(random.randint(300000,2500000)) 


 

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez",\
                "Laura Hernández","MiguelSánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

#print(listasueldosempleados)
waa=(sueldo1,sueldo2,sueldo3,sueldo4,sueldo5,sueldo6,sueldo7,sueldo8,sueldo9,sueldo10)


lista800000=[]
listaentre=[]
listasuperior=[]



lista=[]
listausados=[]
for i in range(10):
    listarandom=random.choice(waa)
    #print(listarandom)
    if listarandom<800000:
        lista800000.append(listarandom)
    if listarandom>800000 and listarandom<2000000:
        listaentre.append(listarandom)
    listarandom2=random.choice(trabajadores)
    if listarandom<2000000:
        listasuperior.append(listarandom)
    if listarandom2 in listausados:
        while listarandom2 in listausados:
            listarandom2=random.choice(trabajadores)
    #print(listarandom2)
    listausados.append(listarandom2)
    




    listawia={listarandom2:listarandom,
        
        
        }

print(listawia)

)

def estadisticas():
    listabien=[]
    listabien.append(listawia)
    listasorteada=listabien.sort()
    print("El menor valor es",listabien[0:1])
    print("El mayor valor es",listabien[0:-1])


def reporte():
    with open('Archivo_scv','w') as archivo_scv:
        escritor_csv = csv.writer(archivo_scv)
        escritor_csv.writerow(["Nombre empleado        ,","sueldo base","descuento salud","descuento AFP","Sueldo liquido"])
        escritor_csv.writerows([listawia])

while Respuesta!="5":
    Respuesta=input("Ingrese la opcion que desea:")
    print("1. Asignar sueldos aleatorios.")
    if Respuesta==1:
        print(listawia)
     
    print("2. Clasificar sueldos.")
    print("3. Ver estadísticas.")
    print("4. Reporte de sueldos.")
    print("5. Salir del programa.")
    Respuesta=input("Ingrese la opcion que desea:")
    
    if Respuesta=="5":
     exit()