import time   
from datetime import datetime

while(True):
    now = datetime.now().strftime("%H:%M:%S");
    print(now, end="\r");