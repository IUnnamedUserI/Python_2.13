#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print_list(list):
    """
    Функция выводит на экран список всех существующих записей
    """
    
    for member in list:
        print(f"{member['surname']} {member['name']}, "
                f"{member['phone']}, {member['date']}")
    