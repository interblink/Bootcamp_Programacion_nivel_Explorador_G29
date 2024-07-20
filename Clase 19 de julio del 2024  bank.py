 
from datetime import datetime;

list_cedula=[];
list_nombre=[];
list_inversion=[];
list_ROI=[];
list_time=[];

poe =1;
person = 3;


def fill():
  conta = 0;
  while(conta<person):
    print("Persona: ",conta + 1 );
    cedula = int(input("Ingrese la cedula: "));
    nombre = str(input("Ingrese el nombre: "));
    inversion = float(input("Ingrese la inversion: "));
    Roi = inversion *0.088;
    list_cedula.append(cedula);
    list_nombre.append(nombre);
    list_inversion.append(inversion);
    list_ROI.append(Roi);
    conta = conta + 1;
    ahora = datetime.now().strftime("%d/%m/%Y,%H:%M:%S");
    list_time.append(ahora);
    
   

def search():
  cedula = int(input("Ingrese la cedula: "));
  
  try: 
    posi = list_cedula.index(cedula);
    print("*********************************");
    print("Info of the person");
    print("Cedula: ",list_cedula[posi]);
    print("Nombre: ", list_nombre[posi]);
    print("Inversion: ",list_inversion[posi]);
    print("ROI ", list_ROI[posi]);
    print("Time: ", list_time[posi]);
    print("*********************************");
  except:
    print("*********************************");
    print("Cedula no encontrada");
    print("*********************************");
    menu();

def menu():
 lo =1;
 while (lo != 3):
  op = int(input("Menu \n 1.Fill \n 2.Search \n 3.Exit \n"));
  match op:
    case 1: fill();
    case 2: search();
    case 3: print("Gracias por utilizar el programa"); lo=3; poe=3;

if(poe !=3 ):

  menu();

