```python
Вы санта. Вы попросили эльфа вернуть вам список пользователей, где каждый пользователь представляет собой еще один список, который содержит один или два элемента: строка (имя пользователя) и его почтовый индекс. Пример:

[["name1 surname1", 12345], ["name2 surname2"], ["name3 surname3", 12354], ["name4 surname4", 12435]]
! У одного пользователя есть имя, но нет индекса.

Напишите функцию santa_users(), которая принимает двумерный список, и возвращает словарь с элементом для каждого пользователя, где ключ - это имя пользователя, а значение - почтовый индекс пользователя. Если нет индекса, тогда значение должно быть None.
```


```python
def main():
    def spisok(a):
        s = []
        for i in range(a):
            s.append([])
            print('Имя ')
            s[i].append(str(input()))
            print('Фамилия ')
            s[i][0] += " " + str(input())
            print('Почтовый индекс ')
            s[i].append(str(input()))
        return s
    def santa_users(spisok):
        slovar = dict()
        for i in spisok:
            if i[1] != "":
                slovar[i[0]] = i[1]
            else:
                slovar[i[0]] = None
        return slovar
    list = spisok(int(input("Колличество пользователей ")))
    otv = santa_users(list)
    print(otv)
if __name__ == "__main__":
    main()
```


```python
Input:[["name1 surname1", 12345], ["name2 surname2"], ["name3 surname3", 12354], ["name4 surname4", 12435]]
Out: {"name1 surname1": 12345,
    "name2 surname2": None,
    "name3 surname3": 12354,
    "name4 surname4": 12435,}   
```


```python
Реализуйте функцию, принимающую один аргумент (римское число) и возвращающее арабское.
```


```python
def main():
    def perevod(rim):
        print("Из римского %s" % (rim))
        arab = 0
        znacheniya = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90,
                  "CD": 400, "CM": 900}
        a = 1
        while a <= len(rim):
            if a != len(rim):
                s = rim[a - 1] + rim[a]
            else:
                s = rim[a - 1]
            if s in znacheniya.keys():
                arab += znacheniya[s]
                a += 2
            else:
                s = rim[a - 1]
                arab += znacheniya[s]
                a += 1
        return "Получили арабское %i" % arab
    print(perevod(str(input())))
if __name__ == "__main__":
    print('Введите римское число ')
    main()
```


```python
Input:II
Out: 2
```
