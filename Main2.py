#!/usr/bin/env python3
# coding: utf-8 -*-

import sys


cnt = 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Ошибка: не указан файл.")
    else:
        filename = sys.argv[1]
        try:
            with open(sys.argv[1], "r", encoding="utf-8") as file:
                lines = file.readlines()[:10]
                for line in lines:
                    print(line.strip())
        except FileNotFoundError:
            print(f"Ошибка: файл '{filename}' не найден.")
        except:
            print("Произошла ошибка при чтении файла.")
