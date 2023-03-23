{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b81db9b3",
   "metadata": {},
   "outputs": [],
   "source": [
    "def main():\n",
    "    f = open('Lab_1.txt', 'r')  # открыли файл\n",
    "    m = list(map(int, f.read().split()))  # список значений\n",
    "    f.close()  # закрыли файл\n",
    "    global sln\n",
    "    sln= False  # пока нет решения\n",
    "    calc(1,'',0,m)#расставляем знаки\n",
    "\n",
    "\n",
    "def calc(idx, st, summ, m):    \n",
    "    global sln\n",
    "    if not sln:  # решение пока не найдено\n",
    "        # если первое число только сложение\n",
    "        for i in range(2 if idx > 1 else 1):\n",
    "            if sln:  # решение найдено\n",
    "                break;  # прекращаем расчет\n",
    "            if i:  # вычитание\n",
    "                sm = summ - m[idx]  # текущая сумма\n",
    "                s = st + '-' + str(m[idx])  # добавили в строку\n",
    "            else:  # сложение\n",
    "                sm = summ + m[idx]  # текущая сумма\n",
    "                s = st + ('+' if idx > 1 else '') + str(m[idx])  # добавили в строку\n",
    "            if idx < m[0]:  # не все числа выбраны\n",
    "                calc(idx + 1, s, sm, m)  # идем к следующему\n",
    "            else:\n",
    "                if sm == m[len(m) - 1]:  # решение устраивает\n",
    "                    f = open('Lab_1_sol.txt', 'w')  # создали файл вывода\n",
    "                    f.write(s + '=' + str(m[len(m) - 1]))  # записали в него строку\n",
    "                    f.close()  # закрыли файл\n",
    "                    sln = True  # решение существует\n",
    "\n",
    "    if idx == 1 and not sln:  # если первое число и решения нет\n",
    "        f = open('Lab_1_sol.txt', 'w')\n",
    "        f.write('no solution')  # записали в файл\n",
    "        f.close()\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
