```python
Вы хотите ограбить банки вдоль улицы, которые идут подряд. В каждом банке есть сейф,
в котором лежим определенная сумма денег ( в миллионах рублей).
Так же в каждом банке есть система защиты,
которая сработает если были ограблены два ближайших банка.
На вход поступает количество банков на улице.
Далее пользователь вводит (по мере их расположения): название банка и сумма денег в сейфе.
Вам необходимо вернуть максимальную сумму денег, которую вы можете получить
(так чтобы не сработала сигнализация), название банков и их порядковые номера на улице.
```


```python
def main():
    kol = int(input('колличество банков'))
    banki = []
    safe = []
    for i in range(kol):
        naz = str(input('bank'))
        bank = [naz]
        dengi = str(input('dengi'))
        safe.append(dengi)
        bank.append(dengi)
        banki.append(bank)
    if len(safe) > 3:
        m=0
        s = 0
        for i in range(0, len(safe), 2):
            s += int(safe[i])
        m = max(m, s)
        s = 0
        for i in range(1, len(safe), 2):
            s += int(safe[i])
        m = max(m, s)
        print(m)
    if len(safe) == 2:
        if safe[0] > safe[1]:
            print(safe[0])
        else:
            print(safe[1])
    if len(safe) == 3:
        if (safe[0] + safe[2]) > safe[1]:
            print(safe[0] + safe[2])
        else:
            print(safe[1])
    if len(safe) == 1:
        print(safe[0])
if __name__ == "__main__":
    main()
```


```python
Input:[1,6,8,3,1]
Out: 10
```


```python
2.Повернуть матрицу по часовой стрелке
```


```python
def main():
    m = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]
    print(*m, sep="\n")
    for i in range(len(m)):
        for j in range(i, len(m[i])):
            m[i][j], m[j][i] = m[j][i], m[i][j]
    for j in range(len(m)):
        m[j] = m[j][::-1]
    print(' ', *m, sep="\n")
if __name__ == "__main__":
    main()
```


```python
In:[[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]
Out:[13, 9, 5, 1]
    [14, 10, 6, 2]
    [15, 11, 7, 3]
    [16, 12, 8, 4]
```
