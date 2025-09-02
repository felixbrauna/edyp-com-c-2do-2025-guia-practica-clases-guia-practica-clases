# Ejercicio 2: Modelar una computadora
# 
# En este archivo debés crear la clase Computadora siguiendo las consignas del README.
# Recordá:
# - Definir atributos relevantes en el constructor (__init__), con valores por defecto.
# - Implementar el método __str__ para mostrar la información esencial.
# - Instanciar al menos 3 computadoras con distintos valores.
# - Llevar la cuenta de computadoras creadas (usar variable de clase).
# - Implementar al menos 2 métodos de los sugeridos (updateOS, PM, addRAM, getCapacity).
# - Crear otra clase para un componente (ej: Disco, RAM, etc.) con su propio __init__, __str__ y al menos un método.
# 
# ¡No olvides probar todos los métodos y comentar tu criterio para los valores


class computadora:
    cantidad=0 
    
    
    def __init__(self,id:int='1',marca:str='Lenovo',modelo:str='A500',anio:str='2006',RAM:int='1500'):
        self.id=id
        self.marca=(marca)
        self.modelo=self.setter_modelo(modelo)
        self.anio=anio
        self.ram=RAM
        
    def __str__(self):
        return  f'La computadora de {self.marca} con id {self.id} tiene un modelo  {self.modelo} q  es del año {self.anio}, ademas cuenta con un ram {self.ram}'

    @classmethod
   
    def veces(cls):
        print(f'La cantidad de computadoras creadas son {cls.cantidad}')
    def getter_marca(self):
        return self.marca
    
        
    def setter_modelo(self,valor):
        if len(valor)==0 or not isinstance(valor,str):
            raise ValueError ('La marca debe ser una cadena no vacia')
        
        else:
            return valor
        

class RAM:
    def __init__(self, capacidad:int):
        if capacidad <= 0:
            raise ValueError("La capacidad de la RAM debe ser mayor a 0")
        self.capacidad = capacidad  
    
    def __str__(self):
        return f"RAM {self.capacidad}GB "           
    
    def aumentar_capacidad(self):
        aumentar=int(input('cuanto deasea aumentar'))
        viejo=self.capacidad
        self.capacidad=viejo+aumentar
        
        
    
    
def main():
 computadora1=computadora(2,'20','40','30','20')  
 computadora2=computadora() 
 computadora3=computadora(3,'motorola','C500','2001','900')
 
 computadora.setter_modelo(computadora1,'D500')
 print(computadora.getter_marca(computadora1))

def main2():
    A=RAM(500)
    RAM.aumentar_capacidad(A)
    print(A.capacidad)
    
    
main()
main2()
        
        
    




