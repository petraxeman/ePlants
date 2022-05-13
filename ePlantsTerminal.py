import asyncio, random
from settings import *

class Plant:
    def __init__(self, cords, code=None):
        self.root_cords = vec2(cords[0])
        self.cells = [(0, 0, self, vec2(0, 0))]
        self.gen = Genom(code)
    def growth(self, area):
        pass

class Genom:
    def __init__(self, code = None):
        if code != None:
            self.code = code
        else:
            self.code = Genom.generate_code()
        self.g = self.code_interpritate(self.code)
    def code_interpritate(self, code):
        g = {}
        for i in range(CHAIN_COUNT):
            g[i] = code[:CHAIN_LEN]
            code = code[CHAIN_LEN:]
        return g
    def mutate_and_return(self):
        pass
    @staticmethod
    def generate_code():
        code = []
        for i in range(CHAIN_COUNT * CHAIN_LEN):
            code.append(random.randint(CHAIN_MIN, CHAIN_MAX))
        return code

class Area:
    def __init__(self, ):
        self.area = [[(-1, -1, -1) for i in range(AREA_WIDTH)] for i in range(AREA_HEIGTH)]

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, value):
        if type(self) == type(value):
            return Vector2(self.x + value.x, self.y + value.y)
    def __sub__(self, value):
        if type(self) == type(value):
            return Vector2(self.x - value.x, self.y - value.y)
    def __iadd__(self, value):
        if type(self) == type(value):
            self.x += value.x
            self.y += value.y
            return self
        return self
    def __isub__(self, value):
        if type(self) == type(value):
            self.x -= value.x
            self.y -= value.y
            return self
        return self
    def __repr__(self):
        return f'<x:{self.x}-y:{self.y}>'
def vec2(x, y):
    return Vector2(x, y)

async def mainloop():
    pass


if __name__ == '__main__':
    v = Vector2(1, 1)
    v2 =  Vector2(1, 2)
    v3 = v + v2
    print(v, v2, v3)
    v += v3
    print(v, v3)
    asyncio.run(mainloop())
