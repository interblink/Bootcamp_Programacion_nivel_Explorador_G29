'''realizar un programa que me pida por teclado
la cantidad de dinero a invertir de una persona
y con esa cantidad, calcular cuanto dinero gano de ROI
si el porcentaje de ganancia por año es 12%.
'''

list_username = [];
list_password = [];
list_roi = [];
op =0;


def calular_roi():
 # Preguntar al usuario por su nombre y contraseña
 username1 = str(input("Ingrese su nombre: "));
 password1 = str(input("Ingrese su contraseña: "));
 
 ini = 0;
 found = False;
 while(ini < len(list_username)):
  if username1 == list_username[ini] and password1 == list_password[ini]:
   print("Bienvenido");
   # Declarar variables
   inversion = float(input("Ingrese la cantidad de dinero a invertir: $"))
   meses_de_inversion = int(input("Digite cuantos meses desea invertir"));
   porcentaje_inversion_por_mes = 0.01;
   # Calcular ROI
   roi = inversion * (meses_de_inversion * porcentaje_inversion_por_mes);
   print(f"Su ganancia en los {meses_de_inversion} meses es: ",roi);
   list_roi[ini] = roi;
   found = True;
  
  ini = ini + 1;

 if(found == False):
  print("Usuario y contraseña no validos o no encontrado en la base de datos");


def llenar_datos():
 person = 1;
 while(person <= 5):
  username = input("Ingrese su nombre: ");
  password = input("Ingrese su contraseña: ");
  list_username.append(username);
  list_password.append(password);
  list_roi.append(0);
  person = person + 1;

def imprimir_usuario_roi():
 tamano = len(list_username);
 if(tamano == 0):
  print("*********************************");
  print("No hay usuarios registrados");
  print("*********************************");
 
 else:
  ini = 0;
  while(ini < len(list_username)):
   print(f"Nombre: {list_username[ini]} - ROI: {list_roi[ini]}");
   ini = ini + 1;

def menu():
  i=2;
  while(i!=1):
    print("Menu");
    print("1. Ingresar datos");
    print("2. Calcular ROI");
    print("3. Imprimir usuario y roi");
    print("4. Salir");
    try:
     op = int(input("Digite opcion: "));
     match (op):
      case 1: llenar_datos();
      case 2: calular_roi();
      case 3: imprimir_usuario_roi();
      case 4: print("Gracias por utilizar programa"); i=1;
      case _: 
       print("*********************************");
       print("Opcion no es valida");
       print("*********************************");
    except ValueError:
     print("*********************************");
     print("Opcion no es valida, porfavor digite el numero de opcion");
     print("*********************************");

#main
menu();
