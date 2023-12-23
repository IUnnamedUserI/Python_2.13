#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def find_member(surname, member_list):
    """
    Функция для вывода на экран всех записей, чьи фамилии совпадают
    с введённой (не возвращает никаких значений)
    """
    
    count = 0

    for member in member_list:
        if member['surname'] == surname:
            print(f"{member['surname']} {member['name']}, "
                f"{member['phone']}, {member['date']}")
            count += 1
        
        if count == 0:
            print("Записи не найдены")
