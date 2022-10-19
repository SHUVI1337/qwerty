def main():
    i=int(input('чисел во первом множестве'))
    list1=set()
    l=0
    while l<i:
        print('число номер',(l+1))
        list1.add(input())
        l+=1
    i=int(input('чисел во втором множестве'))
    list2=set()
    l=0
    list3=set()
    while l<i:
        print('число номер',(l+1))
        list2.add(input())
        l+=1
    list3=list1.intersection(list2)
    print(len(list3))
if __name__=='__main__':
    main()
