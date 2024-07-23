#Diccionarios
#Datos se guardan desordenados.
#Los datos se guardan en pares clave-valor.
#Las claves son unicas.

#ejemplos
'''diccionario = {"azul": "blue", "azul":"blue1"}

print(diccionario);

for i in diccionario:
 print(i);

for i in diccionario:
  print(diccionario[i]);

diccionario["rojo"] = "red";
print(diccionario["rojo"]);


print(diccionario);

diccionario["Amarrillo"] = "Yellow";

print(diccionario);

clave = str(input("Digite color español: "));
valor = str(input("Digite color ingles: "));
diccionario[clave] = valor;

persona = ["Johann","Av1","Banco agrario"];
cedula = 1094240;
diccionario[cedula]=persona;

print(diccionario);

#imprimir una clave en especial

print(diccionario[cedula][0]);

#un programa que me guarde los numeros de cedula en conjunto con su direccion, email y nombre
#diccionarios
'''
diccionario ={};
list_informacion =[];

cedula = int(input("digite cedula: "));
direccion = str(input("Digite direccion: "));
email = str(input("Digite email: "));
nombre = str(input("Digite nombre: "));
list_informacion = [direccion,email,nombre];
diccionario[cedula] = list_informacion;

control =0;
while(control <2):
 cedula = int(input("digite cedula: "));
 if (cedula in diccionario):
  print("Cedula ya existe");
 else:
  direccion = str(input("Digite direccion: "));
  email = str(input("Digite email: "));
  nombre = str(input("Digite nombre: "));
  list_informacion = [direccion,email,nombre];
  diccionario[cedula] = list_informacion;
  control = control + 1;

print(diccionario);

print("Numero de personas: ",len(diccionario));

#buscar por cedula
cedula = int(input("digite cedula: "));
print("*****************************************")
print("La informacion de la persona que busca es: ")
print(diccionario[cedula][0]," ",end="");
print(diccionario[cedula][1]," ",end="");
print(diccionario[cedula][2]," ",end="");
print("*****************************************")