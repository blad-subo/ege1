
Name = True
name_2 = False
# не сравниваем разные типы кроме числовых
#print(list((1,2,3) == [1,2,3])
# print("gazan" != "hello")
# == > < >= <= != работает для всех типов данных
# print(11 > 32) #результат сравнения bool



#num_1 = [1,2,3]
#num_2 = [1,2,3]
#print(num_1 is num_2)
#


#str_1 = ('hello')
#оператор принадлежности
#print("ll" in str_1)

#list_1 [1,2,34,45]
#print(2 in list_1)
#not - оператор отрицания



#and or not

#print(True and False) #True
#0 0 0
#1 0 0
#0 1 0
#1 1 1

#хотябы одно истино
#print(True or False) #
#0 0 0
#1 0 1
#0 1 1
#1 1 1

#not
# 0 -> 1
# 1 -> 0


#импликация
# A -> B
# <=
#0 0 1
#0 1 1
#1 0 0
#1 1 1

#a = True
#b = False
#print(a<= b)

# <--> - эквивалентность
# 0 0 1
# 1 0 0
# 0 1 0
# 1 1 1

#исключающее или
# (+)
# ^
#0 0 0
#0 1 1
#1 0 1
#1 1 0
#a = True
#b = False
#print(a ^ b)
#print((a or b) and (a!=b))


#Стрелка пирса
# = True
#b = False
#print(not(a or b))
#0 0 1
#0 1 0
#1 0 0
#1 1 0


#Штрих Фешшера
#A|B
#not(A and B)
#0 0 1
#0 1 1
#1 0 1
#1 1 0



#алгебра логики
# 1 - ()
# 2 - not
# 3 - and
# 4 - or
# 5 - A -> B
# 6 -эквивалентность

#B pyton
# 1 - ()
# 2 - (**)
# 3 - (*, /, %, //)
# 4 - (+, -)
# 5 - (>, <, >=, <=, ==, !=)
# 6 - not
# 7 - and
# 8 - or




#a ="123"
#int(строка,система исчисления)
#print(int(a, 16))

#двоичное представление числа
#a = 5
#print(bin(a))
#format
#o для восьмеричной
#x шестнадцатиричн
#b двоичная
#print(format(20,"b"))
#f - строки
#print(f"{20:x}")
#восьмеричное представление числа
#print(oct(5))

#шестнадцатиричное
# print(hex(29))


#шестнадцатиричное
#print(hex(29))

#импорт названия
import math

#print(math.log10(100)) #в какую степень основания чтобы получить х
#корень
#print(math.sqrt(100))
#print(100**(1/2))

#округление
#a = 10.7
#print(int(a), a // 1,math.floor(a))

#до большего
#print(math.ceil(a))


#помат правилам
#print(round(a))

#x = 1
#y = 0
#z = 0
#w = 1
#print(x == y and z <= w)


#print((x ==y) or (y or z) <= x)

n1 = 10
n2 = 15
n3 = 17
step1 = n1 * (n3 - n2)
step2 = n2 ** n2
step3 = n3 % 3 + step1
result = oct(step3 // step2)
print(oct(step3 // step2))


x = (int("1B", 16) - int("67",8)) / 4
print (x)
