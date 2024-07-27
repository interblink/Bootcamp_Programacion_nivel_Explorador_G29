#Conjuntos set
#Son un tipo de coleccion donde los elementos se agregan de forma desordenada
#Principal caracteristica es que no pueden haber duplicados

#crear conjunto set()

#conjunto = set()#set() conjunto vacio
#conjunto ={} #set conjunto vacio
#conjunto ={2,5,4.7,"johann"} #print(conjunto) imprime la informacion

#conjunto ={2,5,[1,2,3],"johann"} #no puedo agregarle una lista dentro del set pues porque pierde la teoria de conjuntos
#conjunto ={2,2,4.7,"johann"} print(conjunto) #{2,4.7,"johann"} #borra el segundo dos porque esta duplicado por la caracteristica de arriba al principio de set

#agregar datos

#conjunto.add("hola") #el me lo agrega donde quiera puesto que el set la caracteristica es que son desordenados
#conjunto.add(5)#el me lo agrega donde quiera puesto que el set la caracteristica es que son desordenados
#conjunto.add(3.2)  #el me lo agrega donde quiera puesto que el set la caracteristica es que son desordenados
#print(conjunto)

#eliminar un dato del conjunto set()

#conjunto = set()#set() conjunto vacio
#conjunto ={} #set conjunto vacio
#conjunto ={2,5,4.7,"johann"} #print(conjunto) imprime la informacion
#conjunto.discard(5) print(conjunto) #{2,4.7,"johann"}

#vaciar el conjunto creado para que queden en blanco

#conjunto = set()#set() conjunto vacio
#conjunto ={} #set conjunto vacio
#conjunto ={2,5,4.7,"johann"} #print(conjunto) imprime la informacion
#conjunto.clear() print(conjunto) #{}

#Operaciones con conjuntos set().

#Comprobar si dos conjuntos son iguales.

conjunto = set()#set() conjunto vacio
conjunto ={} #set conjunto vacio
conjunto ={1,2,3}
conjunto1 ={3,4,5}
#print(conjunto == conjunto1) #false los dos conjuntos no son iguales porque tienen valores diferentes

#if(conjunto==conjunto1):
# print("Son iguales")
#else:
# print("No SOn iguales")

#union de conjuntos (Elementos de a mas elementos de b)
c=conjunto | conjunto1
print(c)

#intercepcion de conjunto. (Elementos de a que estan tambien en b)

c=conjunto & conjunto1
print(c)

#diferencia entre conjuntos (elementos de a que no estan en b)

c=conjunto - conjunto1  
print(c)

#diferencia simetrica (elementos que estan en a y b pero que no estan en ambos)

c=conjunto ^ conjunto1  
print(c)

#crear otro conjunto

conjunto = set()#set() conjunto vacio
conjunto ={} #set conjunto vacio
conjunto ={1,2,3}
conjunto1 ={3,4,5}
conjunto2={1,2,3,4,5}

#determinar si un conjunto es subconjunto de otro. osea un conjunto esta dentro del
print(conjunto1.issubset(conjunto2))

#determinar si un conjunto no comparte los datos en otro. (Si los datos de un cojunto estan en el otro conjunto)

print(conjunto.isdisjoint(conjunto1))

#conjuntos inmutables que no pueden cambiar.

conjunto = set()#set() conjunto vacio
conjunto ={} #set conjunto vacio
conjunto =frozenset({1,2,3}) #conjunto se vuelve como tupla queda inmodificable
conjunto1 ={3,4,5}
conjunto2={1,2,3,4,5}

conjunto.discard(3)#
