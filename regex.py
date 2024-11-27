import re
from abc import ABC,abstractmethod
class main(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def impli(self):
        pass
class display(main):
    def __init__(self):
        super().__init__()
        super().impli()
    def impli(self):
        try:
           with open('ip.txt',mode='r') as file:
            #             file.writelines("""192.168.1.1,
            # 192.168.1.2,
            # 192.168.1.3,
            # 192.168.1.4,
            # 10.0.0.1,
            # 10.0.0.2,
            # 172.16.0.1,
            # 172.16.0.2,
            # 8.8.8.8,
            # 8.8.4.4""")
            file.seek(0)
            y =  file.readlines()
            for i in y:
                x = re.compile(r'\b192\.(?:[0-9]{1,3}\.){2}[0-9]{1,3}\b')
                result = x.findall(i)
                for j in result:
                    print(j)  
                    
        except Exception as e:
            print("pattern failed", e)
            

obj = display()
obj.impli()
    
