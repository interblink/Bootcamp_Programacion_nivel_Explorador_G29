'''En la fábrica de juguetes del Polo Norte, cada juguete 
tiene un número de identificación único.
Sin embargo, debido a un error en la máquina de juguetes, 
algunos números se han asignado a más de un juguete.
¡Encuentra el primer número de identificación que se 
ha repetido, donde la segunda ocurrencia tenga el índice más pequeño!
En otras palabras, si hay más de un número repetido, 
debes devolver el número cuya segunda ocurrencia aparezca 
primero en la lista. Si no hay números repetidos, devuelve -1.'''

def primer_repetido(numeros):
 vistos = set();
 segundo_numero_encontrado = len(numeros);
 resultado = -1;
 primero_numero_encontrado = {};
 for i, num in enumerate (numeros):
  if num in vistos:
    if i < segundo_numero_encontrado:
     segundo_numero_encontrado = i;
     resultado = num;
  else:
   vistos.add(num);
   primero_numero_encontrado[num] = i;
 return resultado;

numeros = [2,7,2,5,9,7,1];
print(primer_repetido(numeros));