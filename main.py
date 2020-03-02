import threading 
from filosofo import Filosofo
import sys
lock = threading.RLock()
Filosofos = [Filosofo(lock) for i in range(5)]
i=0
thrds = []
states = []

def showStates():
    global states
    while(True):
        for fil in Filosofos:
            states.append(fil.status)
        sys.stdout.write("\r"+str(states))
        sys.stdout.flush()
        states = []

for fil in Filosofos:
    if (i == 4):
        fil.setRight(Filosofos[0])
    else:
        fil.setRight(Filosofos[i+1])
    fil.setLeft(Filosofos[i-1])
    i += 1
    
print("Dining Philosophers")
print("H=Hungry, E=Eating, T=Thinking")
log = threading.Thread(target=showStates)
log.start()
for fil in Filosofos:
    fil.start()
