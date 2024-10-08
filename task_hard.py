'''
Условие:
В файле содержится последовательность целых чисел. Её элементы могут
принимать целые значения от –100 000 до 100 000 включительно. Определите
количество четверок элементов последовательности, в которых максимальное число
имеет сумму четных цифр больше суммы нечетных, а среднее арифметическое
подпоследовательности меньше суммы максимально возможных делителей
максимального и минимального числа данной четверки, которые не равны ни
единице, ни самому числу, ни нулю. Гарантируется, что такой элемент в
последовательности есть. В ответе запишите количество найденных четверок, затем
максимальную из сумм элементов таких чисел, которая является палиндромом.
Палиндром – число или слово, одинаково читающиеся в обоих направлениях
'''

f = open('cache/17_17558.txt')

lst = [int(i) for i in f]


def dividers(x):
    x = abs(x)
    if abs(x) > 0:
        lst = []
        for i in range(2, int(x**0.5)):
            if x % i == 0:
                lst.append(i)
                lst.append(x//i)
        return sorted(set(lst))
    else:
        return []


cnt = 0
max_cnt = -1 * 10**10
for i in range(len(lst) - 3):
    max_num = max([lst[i], lst[i+1], lst[i+2], lst[i+3]])  # максимальный элемент подпоследовательности
    sum0 = sum([int(i) for i in str(abs(max_num)) if int(i) % 2 == 0])  # сумма четных цифр максимального элемента
    sum1 = sum([int(i) for i in str(abs(max_num)) if int(i) % 2 == 1])  # сумма нечетных цифр максимального элемента
    if sum0 > sum1: # проверка условия 1
        arithmetic_mean = sum([lst[i], lst[i+1], lst[i+2], lst[i+3]])/4  # среднее арифметическое
        min_num = min([lst[i], lst[i+1], lst[i+2], lst[i+3]])  # минимальный элемент подпоследовательности
        if len(dividers(max_num)) * len(dividers(min_num)) > 0:  # проверка на имеющиеся делители
            dividers_max = max(dividers(max_num))  # максимальный делитель максимального числа
            dividers_min = max(dividers(min_num))  # максимальный делитель минимального числа
            if arithmetic_mean < (dividers_max + dividers_min):  # проверка условия 2
                cnt += 1
                sum_list = sum([lst[i], lst[i+1], lst[i+2], lst[i+3]])
                if str(sum_list) == str(sum_list)[::-1]:  # проверка на палиндром
                    max_cnt = max(max_cnt, sum_list)  # обновление максимума
print(cnt, max_cnt)