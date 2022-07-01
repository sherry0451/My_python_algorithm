# -*- coding: utf-8 -*-
# author：S.Yao time:20-05-28

import numpy as np
import random
import matplotlib.pyplot as plt
# import torch
# print("PyTorch Version: ", torch.__version__)
# print('GPU is available:', torch.cuda.is_available())


def for_not():
    for i in range(6):
        for j in range(6):
            print(i, j)
            if j == 3 and i == 3:
                break
        if not (j == 3 and i == 3):
            continue
        break


def for_else():
    for i in range(6):
        for j in range(6):
            print(i, j)
            if i == 3 and j == 3:
                break
        else:
            continue
        break


def bubble_sort(data):
    for i in range(len(data)-1):
        # print('i:', i)
        exchange = False
        for j in range(len(data)-i-1):
            # print('j:', j)
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                exchange = True
        print('bubble sorted li:', data)
        if not exchange:
            return


def select_sort():
    pass


def main():
    # li = [3, 5, 3, 7, 8, 29, 45, 33, 2]
    # print('origin li:', li)
    li = [random.randint(0, 100) for i in range(10)]
    print('origin li:', li)
    bubble_sort(li)


if __name__ == '__main__':
    main()