```python
Первое задание:
1. С клавиатуры поступает строка. Необходимо вывести самую
длинную подстроку без повторных символов.
```


```python
def main():
    l=''
    s=''
    f=input()
    b=1
    m=0
    k=''
    n=''
    for j in range (len(f)):
        a=f
        a=a[j:]
        for i in range(len(a)):
            if a[i] in s:
                m=max(m,len(s))
                if len(a)>len(l):
                    l=s
                s=''
            s = s + str(a[i])
        if len(l)>len(k):
            k=l
    print(k)
if __name__=='__main__':
    main()
```


```python
In:qweasdfdqw
Out:qweasd
```


```python
2. С клавиатуры поступает строка. Необходимо вывести строку, где
порядок слов в противоположном направлении. Первое слово с
заглавной буквы, остальные с маленькой. МЕЖДУ словами только
ОДИН пробел.
```


```python
def main():
    a=input()
    a=a.lower()
    a=a.lstrip()
    a = a.rstrip()
    a=a.replace('    ', ' ')
    a=a.replace('   ',' ')
    a=a.replace('  ', ' ')
    a=a+' '
    s=''
    w=''
    for i in a:
        if i!=' ':
            w=w+i
        else:
            s=w+' '+s
            w=''
    if s=='':
        print(w.capitalize())
    s=s.capitalize()
    print(s)
if __name__=='__main__':
    main()
```


```python
In:пРивет мИР
Out:Мир привет
```


```python
3. С клавиатуры поступает строка, которая имеет только символы: '(', ')', '{', '}', '[' и ‘]’.
Необходимо проверить правильно ли сформированы скобки. Если ВСЕ скобки сформированы правильно, то вывести True,
если нет, то вывести самую длинную правильно сформированную подстроку скобок, если такой подстроки нету,
то вывести False. (Сначала лучше сделать True и False, а потом работать с подстроками).
```


```python
def main():
    s=input()
    p1=0
    p2=0
    p3=0
    a1=s.replace('[','')
    a1=a1.replace(']','')
    a1=a1.replace('{','')
    a1=a1.replace('}','')
    while '()' in a1:
        a1=a1.replace('()','')
    if len(a1)==0:
        p1=1
    a2=s.replace('(','')
    a2=a2.replace(')','')
    a2=a2.replace('{','')
    a2=a2.replace('}','')
    while '[]' in a2:
        a2=a2.replace('[]','')
    if len(a2)==0:
        p2=1
    a3=s.replace('(','')
    a3=a3.replace(')','')
    a3=a3.replace('[','')
    a3=a3.replace(']','')
    while '{}' in a3:
        a3=a3.replace('{}','')
    if len(a3)==0:
           p3=1
    if p1==1 and p2==1 and p3==1:
        print('True')
    else:
        print('False')
if __name__=='__main__':
    main()
```


```python
In:()[]{}
Out:True
```
