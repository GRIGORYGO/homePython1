"""
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).
*Пример:*
3 2 4 -> yes
3 2 1 -> no
"""

n = int(input("Введите число n:"))
m = int(input("Введите число m:"))
k = int(input("Введите число k:"))
s = m * n

if(k <= s  and 
   (s-k) % n == 0 or 
   (s-k) % m == 0 ):
    print('yes')
else: 
    print('no')