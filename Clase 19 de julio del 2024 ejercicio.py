#list = [1,2,3,4,5,6]

list =[];

poe =1;

def fill():

    for i in range(7):
    #print("Digite posicion: ",i);
        num = int(input(f"Digite posicion {i} : ")); 
        list.append(num);


def print1():
    i = 0;
    print("[", end="");
    while i < len(list):
         if(i < 5):
          print(list[i],",", end="");
         else:
          print(list[i], end="");
         i = i + 1;
    print("]");


def menu():
 lo =1;
 while (lo != 3):
  op = int(input("1.Llenar \n 2.Imprimir \n 3.Salir \n"));
  match op:
    case 1: fill();
    case 2: print1();
    case 3: print("Gracias por utilizar el programa"); lo=3; poe=3;

if(poe !=3 ):

  menu();

