```python
Задается количество элементов в списке ( >4). Задается целочисленный список длины N. Задается цель.
Необходимо найти сумму 4 чисел, которые равны цели или находятся близко к ней и вывести их.
```


```python
def main():
    s = int(input(" Введите колличество цифр в списке"))
    c = int(input("Цель"))
    a=[]
    b=[]
    g=1
    for i in range(s):
        print("Цифра номер",g, "в списке")
        a.append(int(input()))
        g+=1
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            for k in range(j+1, len(a)):
                for l in range(k+1, len(a)):
                    z = [a[i],a[j],a[k],a[l]]
                    b.append(z)
    otv = []
    for i in range(len(b)):
        n=0
        for j in range(len(b[i])):
            n+=b[i][j]
        otv.append(n)
    otkl = 10
    h = 0
    for i in range(len(otv)):
        if abs(c - otv[i]) < otkl:
            otkl=abs(c - otv[i])
            h = i
    print("Нужные цифры", b[h],"Ближайшая сумма = ", otv[h])
if __name__ == "__main__":
    main()
```


```python
Input:  
N = 5
[1, 2, 4, -5,-2] 
C = 1
Output:
[1,2,4,-5]
2
```


```python
Задается список целых чисел. Вывести список разделенный списками со всеми
возможными уникальными перестановками целых чисел из заданного списка.
```


```python
from itertools import *
def main():
    s=input()
    s=s.strip()
    s=s.replace('[','')
    s=s.replace(',', '')
    s=s.replace(']', '')
    s = s.replace(' ', '')
    b = list(s)
    c = list(permutations(b, len(s)))
    z = []
    for i in range(len(s)):
        c1 = list(c[i])
        z.append(c1)
    print(z)
if __name__ == "__main__":
    main()
```


```python
Input:
[1,2,3]
Output:
[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```


```python

```


```python

```
