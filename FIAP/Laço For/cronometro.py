import os
import time
os.system("cls")

input("Em 5 segundos o computador explodirá!")
for i in range(5, -1, -1):
    print(i)
    
    time.sleep(1)
    
else:
    print("Bummmm!!!")
