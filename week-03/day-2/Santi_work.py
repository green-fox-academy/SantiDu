import random

##### Apples
class Apple:
    def get_apple(self):
        return "rasin"


##### Sum
class Sum: 
    def sum(self, intlist):
        try:
            return sum(intlist)
        except TypeError:
            return "Wrong type."


##### Anagram
def isAnagram(s: str, t: str) -> bool:
    dic = {}
    L = []
    for c in s:
        dic.setdefault(c, 0)
        dic[c] += 1
    for c in t:
        if dic.get(c):
            dic[c] -= 1
        else:
            L.append(c)          
    return not any(L) and not any(dic.values())


##### Count Letters
def countLetters(s: str) -> dict:
    dic = {}
    for c in s:
        dic.setdefault(c, 0)
        dic[c] += 1
    return dic


##### Fibonacci
def fibonacci(index: int) -> int:
    dic = {1:1, 2:1}
    while index > len(dic):
        dic[len(dic) + 1] = dic[len(dic)] + dic[len(dic) - 1]
    return dic[index]


##### Extension
def add(a, b):
    return a + b

def max_of_three(a, b, c):
    maxn = a
    if b > maxn:
        maxn = b
    if c > maxn:
        maxn = c
    return maxn

def median(pool):
    pool = sorted(pool)
    l = len(pool)
    mid = l // 2
    if l % 2 == 0 and l != 0:
        return (pool[mid - 1] + pool[mid]) / 2
    elif l % 2 == 1:
        return pool[mid]
    else:
        return None

def is_vovel(char):
    return char in ['a', 'e', 'i', 'o', 'ö', 'u', 'ü', \
                    'á', 'é', 'í', 'ó', 'ő', 'ú', 'ű']

def translate(hungarian):
    teve = hungarian
    i = 0
    while i < len(teve):
        if is_vovel(teve[i]):
            teve = teve[:i] + teve[i] + "v" + teve[i] + teve[i+1:]
            i += 2
        i += 1
    return teve


##### Sharpie
class Sharpie:
    def __init__(self, color, width, ink_amount = 100):
        self.color = color
        self.width = width
        self.ink_amount = ink_amount

    def use(self, amount = 2):
        self.ink_amount -= amount


##### Animal
class Animal:
    def __init__(self):
        self.hunger = 50
        self.thirst = 50
        
    def eat(self):
        self.hunger -= 1
    
    def drink(self):
        self.thirst -= 1
        
    def play(self):
        self.hunger += 1
        self.thirst += 1


##### Cows and Bulls
class CAB:
    def __init__(self):
        self.count = 0
        self.ncow = 0
        self.nbull = 0
        self.num = str(random.randint(1000, 9999))
        self.status = "playing"

    def get_input(self):
        return input("Please enter a number between 1000 and 9999.")

    def guess(self):
        self.ncow = 0
        self.nbull = 0
        guess = self.get_input()
        for i in range(4):
            if guess[i] == self.num[i]:
                self.ncow += 1
            elif guess[i] in (self.num[:i] + self.num[i+1:]):
                self.nbull += 1
        self.status = "finished" if self.ncow == 4 else "playing"
        self.count += 1
        return f"{self.ncow} cow, {self.nbull} bull"

            

    