import re

a = "192.168.1.1"
flag = 0
x = re.split(r'\.',a)
if(str(x[0]) == "192"):
    for i in x:
        if(int(i) < 256):
            flag = 1
        else:
            break
            
if(flag == 1):    
    print(f'{a}  vaild ip')
else:
    print("invalid")
