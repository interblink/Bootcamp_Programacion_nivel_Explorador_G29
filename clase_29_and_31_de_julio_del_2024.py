lista_usuario=[];
lista_contrasena=[];
lista_total_vehiculo=[];
lista_numero_de_carros=[];
lista_numero_de_motos=[];
lista_numero_de_camiones=[];
lista_total_de_dinero_recolectado=[];
carro = 0;
moto = 0;
camion = 0;
total_precio_camion = 0;
total_dinero_recolectado = 0;

def registrar_usuarios():
    contar = 0;
    while contar < 3:
     nombre_usuario = str(input("Ingrese su nombre de usuario: "));
     contrasena_usuario = str(input("Ingrese su contraseña: "));
     lista_usuario.append(nombre_usuario);
     lista_contrasena.append(contrasena_usuario);
     lista_total_vehiculo.append(0);
     lista_numero_de_carros.append(0);
     lista_numero_de_motos.append(0);
     lista_numero_de_camiones.append(0);
     lista_total_de_dinero_recolectado.append(0);
     contar += 1;


def operacion_peaje(usuario):
   global carro;
   global moto;
   global camion;
   global total_precio_camion;
   global total_dinero_recolectado;
   carro =0;
   moto = 0;
   camion = 0;
   total_precio_camion = 0;
   total_dinero_recolectado = 0;
   
   print(f"Bienvenido(a): {usuario}");
   Carro = 8700;
   Motos = 2000;
   Camiones = 22000;
   numero_ejes_opcionales = 1000;
   control = -50;
   
   while(control != -1):
      print("**********************************\n");
      print("Menu");
      print("1. Ingreso Carro");
      print("2. Ingreso Motos");
      print("3. Ingreso Camiones");
      print("4. Salir");
      print("**********************************\n");
      try: 
       vehiculo = int(input("Ingrese vehiculo: "));
       match vehiculo:
         case 1: carro = carro + 1;
         case 2: moto = moto + 1;
         case 3:
            try: 
             cantidad_ejes = int(input("Digite cantidad de ejes: "));
             if (cantidad_ejes >0 and cantidad_ejes <=4):
               total_precio_camion = total_precio_camion + Camiones;
             else: 
              if(cantidad_ejes >4):
               restar_ejes = cantidad_ejes - 4;
               total_precio_camion = total_precio_camion + (Camiones + (restar_ejes * numero_ejes_opcionales));
             camion = camion + 1;
            except ValueError:
              print("**********************************\n");
              print("Error, cantidad de ejes debe ser un número");
            
         case 4: control = -1;
         case _: print("**********************************\n"); print("Opcion no valida");
      except ValueError:
        print("**********************************\n");
        print("Solo se pueden digitar numeros");
   

   total_vehiculos =  carro + moto +  camion;
   total_carro = carro * Carro;
   #print("Carros: ",total_carro);
   total_moto = moto * Motos;
   #print("Motos: ",total_moto);
   total_camion = total_precio_camion;
   #print("Camiones: ",total_camion);
   total_dinero_recolectado = total_carro + total_moto + total_camion;
   print(f"Total recolectado de todos los vehiculos: {total_dinero_recolectado}");
   print(f"Total de vehiculos que pasaron por el peaje: {total_vehiculos}");
   
   posi = lista_usuario.index(usuario);
   lista_total_vehiculo[posi] = total_vehiculos;
   lista_numero_de_carros[posi] = carro;
   lista_numero_de_motos[posi] = moto;
   lista_numero_de_camiones[posi] = camion;
   lista_total_de_dinero_recolectado[posi] = total_dinero_recolectado;
 

def login():
    usuario = str(input("Ingrese su usuario: "));
    contrasena = str(input("Ingrese su contraseña: "));
    if usuario in lista_usuario and contrasena in lista_contrasena:
       print("Bienvenido");
       operacion_peaje(usuario);
    else:
       print("**********************************\n");
       print("Usuario o contraseña incorrectos");


def person_recoger_maxi_dinero():
    
  maximo = max(lista_total_de_dinero_recolectado);
  #print("aaa",maximo);

  posi = lista_total_de_dinero_recolectado.index(maximo);
  #print("bbb",posi);
  
  
  username = lista_usuario[posi];
  print(f"¡Felicidades {username} por ser la persona que recaudo mas dinero ");

  
def menu():
   op = True;
   while(op == True):
    print("**********************************\n");
    print("Menu");
    print("1. Registrar usuarios");
    print("2. Iniciar sesión");
    print("3. Persona de mayor recaudo");
    print("4. Salir");
    print("**********************************\n");
    try:
     opcion = int(input("Ingrese su opción: "));
     match opcion:
      case 1: registrar_usuarios();
      case 2: login();
      case 3: person_recoger_maxi_dinero();
      case 4: print("Gracias por utilizar el sistema");op = False;
      case _: print("**********************************\n"); print("Opcion no valida");
    except ValueError:
      print("**********************************\n");
      print("Solo se pueden digitar numeros");

menu();

