import random

class dividend():
    def __init__(self, DIV=1,
                 EPS=1,
                 DPR=1,
                 RR=1,
                 ROE=1,
                 DIV0=1,
                 g=1,
                 DIV1=1,
                 rCE=1,
                 PV=1,
                 applied='Yes'):
        self.DIV = DIV
        self.EPS = random.randint(-0, 10)
        self.DPR = random.sample(range(-1 ,5), 10)
