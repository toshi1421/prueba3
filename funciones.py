import csv

def agregarp_op1():
    print("1)... Agregar productos al inventario")
    
    id = input("Agregue el id del producto")
    nombre = input("Agregue el nombre del producto: ")
    categoria = input("Agregue la categoría(Electronica, Textil y Calzado): ")
    precio = input("Agregue el precio del producto")
    
    with open('inventario.csv','a', newline='') as invproductos:
        escribirproductos = csv.writer(invproductos) 
        escribirproductos.writerow(['id','nombre','categoria','precio'])
        escribirproductos.writerow([id,nombre,categoria,precio])
        
       
    print(f"Se guardo el producto '{nombre}")  

def leerinventario_op2():
    with open('inventario.csv','r', newline='') as invproductos:
            invproductos = csv.reader(invproductos)
            for fila in invproductos:
                print(fila)

             
         
def clasificarExponer_op3():
    print("3)... Clasificar productos y Exportar productos")
    
    with open('inventario.csv', 'r', newline='') as invproductos:
        leer = csv.reader(invproductos) 
        electronica = []
        textil = []
        calzado = []
        for categoria in leer:
            if categoria[2]== 'electronica':
                electronica.append(categoria)
            elif categoria[2]=='textil':
                textil.append(categoria)
            elif categoria[2]=='calzado':
                calzado.append(categoria)
                
    with open('clasificacion_productos.txt','w', newline='') as clasarchivo:
        clasarchivo.write('electronica: ')
        for elemento in electronica:
            clasarchivo.write(str(elemento))
        clasarchivo.write('\ntextil: ')
        
        for elemento in textil:
            clasarchivo.write(str(elemento))
        clasarchivo.write('\ncalzado: ')
        
        for elemento in calzado:
            clasarchivo.write(str(elemento))
            
            
        print("archivo creado")
   
           
                 
              
        