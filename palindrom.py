#!/usr/bin/python
# -*- coding: utf-8 -*-

import re


def palindrom(raw_str):

    """
    Функция, реализующая палиндром -
    определение симметричности двух
    половин строки относительно середины.

    """
    # Очистка входной строки от пунктуации
    # и пробельных символов.
    my_str = re.sub("[\s.,!-?]", '', raw_str.decode('utf-8'))

    for ch_left, ch_right in zip(list(my_str[:len(my_str) / 2]),
                                 list(my_str[::-1][:len(my_str) / 2])):
        if ch_left == ch_right:
            continue
        else:
            return False
    return True                                        
    

if __name__ == '__main__':
    import sys

    try:
        arg_str = sys.argv[1]
        if not isinstance(arg_str, str):
            print 'Ошибка типа входных данных! Поддерживаемый тип - строка'
            sys.exit()
        print palindrom(arg_str)
    except:
        print 'Ошибка: ', sys.exc_info()[0] 

