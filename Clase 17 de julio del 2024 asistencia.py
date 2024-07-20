
lista_cedula = [];
lista_nombre = [];
cedula = int(input("Digite numero cedula: "));
nombre = str(input("Digite Nombre: "));
contar = 0;
while(cedula !=-20):
   lista_cedula.append(cedula);
   lista_nombre.append(nombre);
   contar = contar + 1;
   cedula = int(input("Digite numero cedula: "));
   if(cedula == -20):
      break;
   else: 
      nombre = str(input("Digite Nombre: ")); 

print("Numero de campistas que asistieron es: ",contar);

incre = 1;
cantidad_de_cedulas = len(lista_cedula);
can =0;
while can < cantidad_de_cedulas:
   print("Persona: ",incre);
   print("Cedula persona  ", lista_cedula[can]);
   print("Nombre persona ", lista_nombre[can] );
   incre = incre +1;
   can = can +1;
