#!/usr/bin/env python3
# coding: utf-8 -*-

cnt = 0

if __name__ == "__main__":
    word = input("Введите слово для поиска: ")

    with open("is1.txt", "r", encoding="utf-8") as f:
        text = f.read()
    sentences = text.split('. ')

    # Вывод предложений с запятыми.
    for sentence in sentences:
        cnt = 0
        if word in sentence:
            cnt += 1
        print(sentence, "Искомое слово встретилось:", cnt, "раз(а).")
