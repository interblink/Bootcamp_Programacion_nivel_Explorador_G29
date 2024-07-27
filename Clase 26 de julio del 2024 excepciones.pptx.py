def division():
 try: 
  n =  int(input("Digite numero: "));
  n1 = int(input("Digite numero: "));
  divi = n / n1;
 except ValueError:
  print("Error: El valor no es un número");
  division();
 except Exception as e:
  print(f"Exception {e}");
  division();
 else:
  print(divi);
  rta = n + 10;
  print(rta);

#main
division();