import threading 
from filosofo import Filosofo
lock = threading.RLock()
Filosofos = [Filosofo(lock) for i in range(5)]
i=0
for fil in Filosofos:
    fil.setLeft=Filosofos[i-1]
    fil.setRight=Filosofos[i+1]
    i+=1
