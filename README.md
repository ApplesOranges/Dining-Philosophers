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
Here we have initialized all variables and structures, as well as importing both the "filosofo" module and the threading library.
```python
import threading 
from filosofo import Filosofo
lock = threading.RLock()
Filosofos = [Filosofo(lock) for i in range(5)]
i=0
thrds = []
states = []
```
The function "showStates()" fills a list with the current state of each philosopher and prints it.

```python
def showStates():
    j = 0
    if states.length < 5:
        for fil in Filosofos:
            states.append(fil.status)
    print(states)
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
for fil in Filosofos:
    thrds.append(threading.Thread(fil.run()))
    thrds[i].start()
    i += 1
    showStates()
```
