a = int(input("Ingrese numero A"));
b = int(input("Ingrese numero B"));
c = int(input("Ingrese numero C"));

if (a==b):
   if(b==c):
      print("triangulo equilatero");
   else:
      print("triangulo isosceles");
else:
   if(a==c):
      print("triangulo isosceles");
   else:
     if(b==c):
       print("Triangulo isosceles");
     else:
        print("triangulo escaleno");
