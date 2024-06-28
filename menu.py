
import funciones
import csv

op= 0

while op != 5:
    
    print("Bienvenido al Sistema de Gestión de Inventario")
    print("1)...Agregar productos al inventario")
    print("2)...Leer inventario")
    print("3)...Clasificar y Exportar productos")
    print("4)...Salir")
    
    op=input("Seleccione una opcion del 1 al 4: ")
    
    if op == "1":
        funciones.agregarp_op1()
    if op == "2":
        funciones.leerinventario_op2()
    if op == "3":
        funciones.clasificarExponer_op3()
        
    if op == "4":
        print("")
        print("Adiós¡!")
        print("")
        break