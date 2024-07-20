#Edad: >=60 and t<25   "Jubilacion por edad"

#antigüedad joven edad: <60  and t>=25

#jubilación por antigüedad adulta: >=60 and >=25

edad = int(input("Digite edad: "))

while(edad <=0 or edad >=105):
   print("Edad no valida");
   edad = int(input("Digite edad: "))


antiguedad = int(input("Digite antiguedad: "));

while(antiguedad <=0 or antiguedad >=105):
   print("Antiguedad no valida");
   antiguedad = int(input("Digite antiguedad: "));


if (edad >= 60 and antiguedad < 25):
    print("Jubilacion por edad");

if(edad <60 and antiguedad >=25):
    print("Antigüedad joven");

if(edad >=60 and antiguedad>=25):
 print("Jubilación por antigüedad adulta");
