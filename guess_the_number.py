"""
A program that guesses the number guessed by the computer in the minimum number of attempts.
Программа, которая угадывает загаданное компьютером число за минимальное количество попыток.
"""

from random import randint
import json


def guess_the_number(report_info):
    """
    Function for finding a number (Half division algorithm).
    The average value in the interval is taken and varies depending on the intended number

    Функция для нахождения числа (алгоритм деления пополам).
    Берется среднее значение в интервале и варьируется в зависимости от предполагаемого числа

    :param report_info: information for the report (информация для отчета)
    :return: report_info: information for the report (информация для отчета)
    """

    count_test = int(input('Введите желаемое кол-во испытаний: '))

    count_ls = []  # list for the average number of attempts (для поиска сред. значения кол-ва попыток)

    for test in range(count_test):

        left_point = 0  # the leftmost point (левая точка интервала)
        right_point = 100  # the rightmost point (правая точка интервала)

        hidden_num = randint(left_point, right_point)  # random number on the interval (случайное число на интервале)
        attempt_in_one_test = 0  # number of attempts in this test (количество попыток в этом тесте)

        while True:
            attempt_in_one_test += 1
            # middle value in the interval (среднее значение на интервале)
            midd_num = round((left_point + right_point) / 2)

            if midd_num > hidden_num:
                # changes the right interval (меняем левую часть интервала)
                right_point = midd_num

            elif midd_num < hidden_num:
                # changes the left interval (меняем правую часть интервала)
                left_point = midd_num

            else:
                # add the attempt to the dictionary (заносим кол-во попыток в словарь для отчета)
                if attempt_in_one_test in report_info.keys():
                    report_info[attempt_in_one_test] += 1
                else:
                    report_info[attempt_in_one_test] = 1

                # add the attempt to the list(заносим кол-во попыток в список)
                count_ls.append(attempt_in_one_test)
                break

    # count the average value of attempts and round it up (вычисляем среднее кол-во попыток)
    mean_attempt = round(sum(count_ls) / len(count_ls))
    print(f"За {count_test} испытаний среднее кол-во попыток = {mean_attempt}\n")

    return report_info


def report(report_info=None):
    """
    Function for viewing statistics
    Функция для показа статистики
    :param report_info: information for the report (информация для отчета)
    :return: True
    """

    if report_info:
        for key, num in report_info.items():
            print(f"За {key} попыток угадано {num} испытаний")
    else:
        print('Статистика пуста')
    return 1


def save_report_info_if_file(report_info=None):
    """
    Функция для сохранения отчета в файл
    Function for saving a report to a file

    :param report_info: information for the report (информация для отчета)
    :return: True/False
    """
    if report_info and isinstance(report_info, dict):
        with open('report_info.json', 'w', encoding='utf-8-sig') as rep:
            json.dump(report_info, rep)
        print('Файл сохранен', end='\n\n')
        return True

    else:
        print('Нет смысла сохранять пустой файл)')
        return False


def control_menu():
    """
    Function to control the operation of the program
    Функция для управления работой программы
    :return: report_info: информация с отчетом
    """

    try:
        report_info = {}  # information for the report (информация для отчета)

        print("Добро пожаловать!!!")

        while True:
            print("\nМеню:")
            print("1.Начать тестирование")
            print("2.Показать отчет")
            print("3.Сохранить в файл")
            print("0.Выход", end='\n\n')

            input_command = input('Введите номер комманды: ')

            if input_command == '1': guess_the_number(report_info)
            elif input_command == '2': report(report_info)
            elif input_command == '3': save_report_info_if_file(report_info)
            elif input_command == '0':
                print("Всего доброго))")
                return report_info
            else:
                print("Странно,не могу выполнить. Введите другую команду...")

    except Exception as ex:
        print(f'Ошибка: {ex}')
        return False


if __name__ == '__main__':
    control_menu()
