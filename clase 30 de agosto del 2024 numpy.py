import numpy as np

import statistics as st

#los 20 primeros numeros 1 a 20

#array = np.arange(1,21);

#print(array);

#operaciones Suma, Resta, Multiplicacion, Division crear dos matrices 3x3

#rray1 = np.random.randint(1,20,size=(3,3));
#rray2 = np.random.randint(1,20,size=(3,4));

#print("Matriz 1: \n",rray1);
#print("Matriz 2: \n",rray2);

#print("Suma: \n",rray1+rray2);

#ajustar = np.pad(rray1,((0, 0), (0, 1)), mode = 'constant',constant_values=0);

#print("Matriz 1 ajustada: \n",ajustar);

#print("Suma: \n",ajustar+rray2);

#print("Multipliacion: \n",ajustar*rray2);

#print("Division: \n",ajustar/rray2);

#print("Restar: \n",rray2-ajustar);

'''
array = np.arange(1,21);

array5 = np.random.rand(10);

media = np.mean(array);
print("Media: ",media);

mediana = np.median(array);
print("Mediana: ",mediana);

# display the mode
print(st.mode(array))

#desviacion estandar

desviacion = np.std(array5);

print(desviacion);

'''

#mascaras numpy.
# seleccionar y operar diferentes elementos de un array.
#true y false
'''
array5 = np.random.rand(10);

print(array5);

mascara = array5 >0.59;

print(mascara)

resul = array5[mascara];

print(resul);

#mayor y menor
'''
array5 = np.random.rand(10);
maximo = np.max(array5);
print(maximo);
#minimo
minimo = np.min(array5);
print(minimo);

re = np.random.randint(1,6, size=10);
print(re);

#lo = np.arange()

#print(lo);
