#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from type_transform_module import type_transform

if __name__ == "__main__":
    selected_type = type_transform(input("Введите тип (tuple/list): "))
    collection = selected_type(input("Введите числа через пробел: ").split())
    print(f"Результат: {collection}")
    print(f"Выбранный тип - {type(collection)}")
