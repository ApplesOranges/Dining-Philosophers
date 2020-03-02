#H=hungry, E=eating, T=thinking
import threading
import time
import random
class Filosofo(threading.Thread):
    def __init__(self, lock):
        threading.Thread.__init__(self)
        self.lock=lock
        self.left=None
        self.right=None
        self.status="T"
    def setLeft(self,fil):
        self.left=fil
    def setRight(self,fil):
        self.right=fil
    def spendTime(self):
        time.sleep(random.randint(0, 5))
    def taste(self):
        if(self.status== "H" and self.left.status!="E" and self.right.status!="E"):
            self.lock.acquire()
            self.status="E"
            self.lock.release()
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
    def eat(self):        
        self.spendTime()
    def think(self):
        self.spendTime()
    def run(self):
        while True:
            self.think()
            self.takeFork()
            self.eat()
            self.leaveFork()
