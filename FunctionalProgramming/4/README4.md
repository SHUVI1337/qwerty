```python
На вход поступает целое число, вернуть true, если число является целым палиндромом.
```


```python
def main():
    numb = list(map(str, input()))
    buf = []

    for i in range(len(numb) - 1, -1, -1):
        buf.append(numb[i])

    if (numb == buf):
        print(True)
    else:
        print(False)

if __name__ == '__main__':
    main()
```


```python
На вход подаётся 8-битное целое число со знаком(проверить нужно), на выходе вы должны вернуть перевернутое значение. Если значение выходит за пределы диапозона 8-битных целых чисел со знаком, тогда возвращаем "no solution".
```


```python
def main():
    numb =  int(input())
    if (numb > 127) or (numb < -128):
        print("no solution")
    else:
        numb = str(numb)
        if numb[0] == "-":
            numb = numb[1:]
            if numb[-1] == "0":
                numb = numb[1::-1]
            else:
                numb = numb[::-1]
            if int(numb) > 128:
                print("no solution")
            else:
                print("-" + numb)
        else:
            if numb[-1] == "0":
                numb = numb[1::-1]
            else:
                numb = numb[::-1]
            if int(numb) > 127:
                print("no solution")
            else:
                print(numb)



if __name__ == '__main__':
    main()
```


```python
На вход поступает строка и целое значение. Необходимо вывести строку в зигзагообразном виде, где целое значение обозначает количество строк.

```


```python
def main():
    stroka, kolvo = str(input()).split(",")
    kolvo = int(kolvo)

    fe = kolvo

    fstroka = ""

    for i in range(2, kolvo):
        fe += 1
    #print("fe: ", fe)

    for f in range(0, kolvo):
        stp = fe - f * 2
        if (stp == 0):
            stp = fe
        j = f
        while (j < len(stroka)):
            if kolvo % 2 == 0:
                fstroka += stroka[j]
                if (j + stp < len(stroka)) and (stp != fe):
                    fstroka += stroka[j + stp]
                j += fe
            else:
                fstroka += stroka[j]
                j += stp
                print("j", j)

    print(fstroka)

if __name__ == "__main__":
    main()
```
