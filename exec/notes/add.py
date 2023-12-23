#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add():
    """
    Функция добавления новой записи, возвращает запись
    """
    
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    date = tuple(map(int, input("Введите дату рождения: ").split('.')))
    
    new_member = {'surname': surname,
                    'name': name,
                    'phone': phone,
                    'date': date
                }
    
    return new_member
