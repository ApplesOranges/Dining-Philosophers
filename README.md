# Dining-Philosophers
Repo for concurrent and parallel programming assingment.

## Introduction
In computer science, the dining philosophers problem is an example problem often used in concurrent algorithm design to illustrate synchronization issues and techniques for resolving them.
It was originally formulated in 1965 by Edsger Dijkstra as a student exam exercise, presented in terms of computers competing for access to tape drive peripherals. Soon after, Tony Hoare gave the problem its present formulation.

## Goal
The main goal of this exercise is to come up with solutions to avoid <b>DeadLock</b>

## Technologies
For this project our team will use python, adding the threading library.

## Contributors
* David Rafael Arancibia Escobar as ApplesOranges
* Emmanuel Cortés Rosas as emmcors
* Alejandro Escalante Hernández as EskerOn
* Kevin Germán Suárez Carbajal as NyvekFearless 
* Abdiel Vladimir Romero Velázquez as Vencigetorix

## Documentation

### main.py
Here we have initialized all variables and structures, as well as importing both the <i>"filosofo"</i> module and the threading library.
```python
import threading 
from filosofo import Filosofo
lock = threading.RLock()
Filosofos = [Filosofo(lock) for i in range(5)]
i=0
thrds = []
states = []
```
The function <i>"showStates()"</i> fills a list with the current state of each philosopher and prints it.

```python
def showStates():
    global states
    while(True):
        for fil in Filosofos:
            states.append(fil.status)
        sys.stdout.write("\r"+str(states))
        sys.stdout.flush()
        states = []
```
Here we are simply defining the left and right philosopher sitting at each side.

```python
for fil in Filosofos:
    if (i == 4):
        fil.setRight(Filosofos[0])
    else:
        fil.setRight(Filosofos[i+1])
    fil.setLeft(Filosofos[i-1])
    i += 1
i = 0
```
Then we start each thread and we print the state in each case.

```python
log = threading.Thread(target=showStates)
log.start()
for fil in Filosofos:
    fil.start()
```
### filosofo.py

First we define the constructor, it includes a lock, wich functions as a semaphore, left and right philosopher and the current state (eating, thinking or hungry).

```python
class Filosofo(threading.Thread):
    def __init__(self, lock):
        threading.Thread.__init__(self)
        self.lock=lock
        self.left=None
        self.right=None
        self.status="T"
```
We create setters or access functions with the purpose of setting the left and right philosopher
We also add the function <i>"spendTime()"</i> wich lets time pass without doing anything.
```python    
    def setLeft(self,fil):
        self.left=fil
    def setRight(self,fil):
        self.right=fil
    def spendTime(self):
        time.sleep(5)
```
The taste function verifies that none of the adjacent philosophers is eating and, if possible, changes state from 'H' (hungry) to 'E' (eating).

```python
    def taste(self):
        if(self.status== "H" and self.left.status!="E" and self.right.status!="E"):
            self.lock.acquire()
            self.status="E"
            self.lock.release()
```
<i>"takeFork()"</i> changes the state from 'T' to 'H' and calls the function <i>"taste()".
<i>"leaveFork()"</i> changes the state from 'E' to 'T and calls the function <i>"taste()"</i> for the adjacent philosophers.
```python
    def takeFork(self):
        self.lock.acquire()
        self.status="H"
        self.taste()
        self.lock.release()
    def leaveFork(self):
        self.lock.acquire()
        self.status="T"
        self.left.taste()
        self.right.taste()
        self.lock.release()
```
Both of the next functions call <i>"spendTime()"</i> therefore they lose time without taking any action.

```python
    def eat(self):        
        self.spendTime()
    def think(self):
        self.spendTime()
```
The <i>"run()"</i> function calls each function in propper order.
```python
    def run(self):
        while True:
            self.think()
            self.takeFork()
            self.eat()
            self.leaveFork()
```        
