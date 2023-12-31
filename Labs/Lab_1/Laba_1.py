import sys
import math

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры

    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента

    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()
    # Переводим строку в действительное число
    while True:
        if (coef_str.startswith('-') and coef_str[1:].isdigit()) or (coef_str.isdigit()):
            coef = float(coef_str)
            break
        else:
            print("Коэффициент введён неправильно, попробуйте ещё раз")
            try:
                # Пробуем прочитать коэффициент из командной строки
                coef_str = sys.argv[index]
            except:
                # Вводим с клавиатуры
                print(prompt)
                coef_str = input()
    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения

    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C

    Returns:
        list[float]: Список корней
    '''
    first_result = []
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        first_result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0*a)
        root2 = (-b - sqD) / (2.0*a)
        first_result.append(root1)
        first_result.append(root2)
    second_result = []
    for i in range(len(first_result)):
        if first_result[i] < 0:
            first_result.pop(i)
        else:
            first_result[i] = math.sqrt(first_result[i])
    for i in range(len(first_result)):
        if first_result[i] != 0:
            second_result.append(first_result[i])
            second_result.append(-1 * first_result[i])
        else:
            second_result.append(first_result[i])
    return second_result



def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a,b,c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))
    

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# roots_proc.py 1 0 -4