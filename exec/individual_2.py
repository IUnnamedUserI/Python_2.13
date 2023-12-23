#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from notes import *

if __name__ == "__main__":
    """
    Основная программа
    """
    
    member_list = []

    while True:
        cmd = input(">>> ")

        if cmd == "help":
            help.print_help()

        elif cmd == "add":
            member_list.append(add.add())
            member_list.sort(key=lambda item: item.get('phone')[:3])

        elif cmd == "list":
            print_list.print_list(member_list)
                
        elif cmd == "find":
            find.find_member(input("Введите фамилию: "), member_list)

        elif cmd == "exit":
            print("Завершение работы программы...")
            break

        else:
            print(f"Команды {cmd} не существует")
