#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def type_transform(selected_type):
    """
    Функция принимает строковое значение. Рекомендуется
    использовать значения 'tuple' или 'list'
    """

    def transform(numbers):
        """
        Функция принимает числовые значения и, в зависимости от
        указанного строкового значения внешней функции, преобразует
        введённые значения в кортеж или список. Возвращает преобразованный
        результат
        """

        collection = [int(value) for value in numbers]

        if selected_type == 'tuple':
            return tuple(collection)
        elif selected_type == 'list':
            return list(collection)
        
    return transform
