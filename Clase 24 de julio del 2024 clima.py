import requests

def get_weather(city):
    url = "https://wttr.in/" + city + "?format=3";
    answer = requests.get(url);
    if(answer.status_code==200):
     print(answer.text);
    else:
     print("La ciudad no se encuentra");

city = str.lower(input("type city: ")) ;
get_weather(city);

    


