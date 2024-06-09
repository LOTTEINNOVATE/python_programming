# 계산 더하기 기능

result = 0
def adder(num):
     global result
     result += num
     return result
print(adder(3))
print(adder(4))
print(adder(4))
print(adder(7))

#------------------------------------------
# 만약 계산기가 두 개 필요하다면?
result_1 = 0
result_2 = 0
def adder_1(num):
    global result_1
    result_1 += num
    return result_1

def adder_2(num):
    global result_2
    result_2 += num
    return result_2

print(adder_1(3))
print(adder_1(4))
print(adder_2(3))
print(adder_2(7))

#---------------------------
# 계산기가 여러 개가 필요하다면?

class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result

cal_1 = Calculator()
cal_2 = Calculator()

print(cal_1.adder(3))
print(cal_1.adder(4))
print(cal_2.adder(3))
print(cal_2.adder(7))

#----------------------------------------
#클래스 변수

class Service:
    secret = "지구는 4006년에 멸망한다."
an = Service()
an.secret
'지구는 4006년에 멸망한다.'
print(an.secret)

#----------------------------------------
#클래스 변수 공유

Service.secret
'지구는 4006년에 멸망한다.'
Service.secret = '지구가 4006년에 멸망한다는 사실은 뻥이다.'
print(an.secret)
#----------------------------------------
#클래스 내부의 함수(메서드:method)

class Service:
    secret = "지구는 4006년에 멸망한다."
    def sum(self, a, b):
        result =  a+b
        print("%s + %s = %s이다. "% (a, b, result))

an = Service()
an.sum(1,1)
#----------------------------------------
#객체 변수
class Service:
    secret = "지구는 4006년에 멸망한다."
    def setname(self, name):
        self.name = name
    def sum(self, a, b):
        result = a+b
        print("%s님, %s + %s = %s입니다. " %(self.name, a, b, result))
an = Service()
an.setname("박달도사")
an.sum(1,1)
#----------------------------------------
#클래스 변수와 객체 변수
kim = Service()
park = Service()
kim.name = "김정보"
park.name = "박융합"

print(kim.name)
print(park.name)

kim.secret = "비밀은 없다."
print(park.secret)
print(kim.secret)
Service.secret
#----------------------------------------
#__init__은 무엇?
#lee = Service()
#lee.sum(1,1)
#Traceback (most recent call last):
#    File "<stdin>", line 1, in <module>
#    File "<stdin>", line 7, in sum
#AttributeError : 'Service' object has no attribute 'name'

class Service:
    secret = "지구는 4006년에 멸망한다."

    def __init__(self, name):
        self.name = name

    def sum(self, a, b):
        result3 = a + b
        print("%s님, %s + %s = %s입니다." % (self.name, a, b, result3))

an = Service("박달도사")
an.sum(1,1)
#---------------------------------
#-------
#사칙연산 클래스
 class FourCal:
     pass

 a = FourCal()
 type(a)

 class FourCal:
     def setdata(self, first, second):
         self.first = first
         self.second = second

a = FourCal()
a.setdata(4,2)

print(a.first)
print(a.second)

#------------------
#사칙연산 클래스 - 더하기
class FourCal:
    def setdata(selfself, first, second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second
        return result

a = Fourcal()
a.setdata(4,2)

print(a.sum())

#----------------------------------------
class FourCal_2:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        result_3 = self.first + first.second
        return result_3
    def mul(self):
        result_3 = self.first * self.second
        return result_3
    def sub(self):
        result_3 = self.first - self.second
        return result_3
    def div(self):
        result_3 = self.first / self.second
        return result_3

a = FourCal_2()
b = FourCal_2()
a.setdata(4,2)
b.setdata(3,7)
print(a.sum())
print(a.mul())
print(a.sub())
print(a.div())
print(b.sub())
#--------------------------
#간단한 주사위 게임
import random

player1_dice = []
player2_dice = []

for i in range(3):
    player1_dice.append(random.randint(1, 6))
    player2_dice.append(random.randint(1, 6))

print("Player 1 rolled" + str(player1_dice))
print("Player 2 rolled" + str(player2_dice))

if sum(player1_dice) == sum(plyer2_dice):
    print("Draw")
elif sum(plyer1_dice) > sum(player2_dice):
    print("Player 1 wins")
else:
    print("Player 2 wins")
#----------------------
from random import randint

class Player:
    def __init__(self):
        self.dice = []

    def roll(self):
        self.dice = []  # Clears current dice
        for _ in range(3):
            self.dice.append(randint(1, 6))

    def get_dice(self):
        return self.dice

player1 = Player()
player2 = Player()

player1.roll()
player2.roll()

print("Player 1 rolled " + str(player1.get_dice()))
print("Player 2 rolled " + str(player2.get_dice()))

if sum(player1.get_dice()) == sum(player2.get_dice()):
    print("Draw!")
elif sum(player1.get_dice()) > sum(player2.get_dice()):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
#------------------------
class Customer:
    """
    A customer of ABC Bank with a checking account.
    Attributes:
        name (str): A string representing the customer's name.
        balance (float): A float tracking the current balance of the customer's account.
    """

    def __init__(self, name):
        """
        Initialize a Customer object whose name is `name`.
        Args:
            name (str): The name of the customer.
        """
        self.name = name
        self.balance = 0.0

    def set_balance(self, balance=0.0):
        """
        Set the customer's starting balance.
        Args:
            balance (float): The starting balance. Defaults to 0.0.
        """
        self.balance = balance

    def withdraw(self, amount):
        """
        Withdraw an amount from the customer's account.
        Args:
            amount (float): The amount to withdraw.
        Returns:
            float: The new balance after withdrawal.
        Raises:
            RuntimeError: If the withdrawal amount is greater than the available balance.
        """
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """
        Deposit an amount into the customer's account.
        Args:
            amount (float): The amount to deposit.
        Returns:
            float: The new balance after deposit.
        """
        self.balance += amount
        return self.balance







#----------------------------------------








#----------------------------------------


