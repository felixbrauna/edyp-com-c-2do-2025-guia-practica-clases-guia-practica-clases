# Este archivo corresponde al Ejercicio 1 de la guía práctica sobre Clases.
# Aquí deberás implementar la clase Camion y resolver los puntos a, b, c, d y f según las consignas

class Camion:
        
        patentes_usadas=[]
        
        def __init__(self, patente, marca ,carga,anio):
            self.patente = patente
            self.marca = marca
            self.carga = carga
            self.anio = anio
            if patente not in Camion.patentes_usadas:
                Camion.patentes_usadas.append(patente)
            else:
                raise ValueError ('La patente ya a sido utilizada')

        def __str__(self):
            return f"Camión: #{self.patente} \nCarga: {self.carga} \nMarca: {self.marca} \nAño: {self.anio}"
        
        #Comparar solo por patenetes
        def __eq__(self, other):
            if not isinstance(other,Camion):
                return False
            
            return(self.patente==other.patente
                #and    self.marca==other.marca
                #and self.carga==other.carga
                #and self.anio==other.anio
                )
        def seter(self,carga):
            self.carga=carga
        

def main():
 camiones=[]
 while True:
     
     hacer=int(input('Que desea hacer 1.Cargar un nuevo camion 2.Modificar la carga  3.Listade por año 4.Marcas 5. Irse'))
     if hacer==1:
         patente=input('Escriba una patente')
         marca=input('escriba una marca')
         carga = int(input("Ingrese la carga máxima (kg): "))
         anio = int(input("Ingrese el año: "))
         try:
             nuevo_camion=(Camion(patente,marca,carga,anio))
             camiones.append(nuevo_camion)
         except Exception as e:
             print(f'hubo un eror {e}')
             
     if hacer==2:
         patente = input("Escriba la patente del camión que está buscando: ") 
         encontrado = False 
         for camion in camiones: 
             if camion.patente == patente: 
                 encontrado = True 
                 carga_nueva = int(input("Escriba la nueva carga: "))
                 camion.carga = carga_nueva 
                 print("Carga modificada con éxito")
                 break 
         if not encontrado: print("El camión buscado no existe")
             
     if hacer==3:
         if camiones==[]:
             print('no hay camiones cargados')
         else:
             ordenados = sorted(camiones, key=lambda c: c.anio, reverse=True)
             for camion in ordenados:
                print(camion)
                
     if hacer==4:
         if not camiones:
             print('No hay ningún camión registrado')
        
         else:
            conteo_marcas = {}

         for camion in camiones:
            if camion.marca in conteo_marcas:
             conteo_marcas[camion.marca]+=1
            else:
                conteo_marcas[camion.marca]=1
         
         n=0
         marca2=''
         frecuencia2=0 
         for marca,frecuencia in conteo_marcas.items():
             if n==0:
                 marca2=marca
                 frecuencia2=frecuencia
                 n=n+1
             else:
                 if frecuencia2<frecuencia:
                     marca2=marca
                     frecuencia2=frecuencia
                     
         print(marca2)            
             
     if hacer==5:
         print('termino el codigo')
         break
            
            
main()


