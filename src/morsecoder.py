#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class MorsecodeError(Exception):
    # 自定义异常
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Morsecoder:
    VERSION = 0.5
    AUTHOR = 'Lemonix'
    _en_list = {'A': '.-',
             'B': '-...',
             'C': '-.-.',
             'D': '-..',
             'E': '.',
             'F': '..-.',
             'G': '--.',
             'H': '....',
             'I': '..',
             'J': '.---',
             'K': '-.-',
             'L': '.-..',
             'M': '--',
             'N': '-.',
             'O': '---',
             'P': '.--.',
             'Q': '--.-',
             'R': '.-.',
             'S': '...',
             'T': '-',
             'U': '..-',
             'V': '...-',
             'W': '.--',
             'X': '-..-',
             'Y': '-.--',
             'Z': '--.',
             '1': '.----',
             '2': '..---',
             '3': '...--',
             '4': '....-',
             '5': '.....',
             '6': '-....',
             '7': '--...',
             '8': '---..',
             '9': '----.',
             '0': '-----',
             '.': '.-.-.-',
             ':': '---...',
             ',': '--..--',
             ';': '-.-.-.',
             '?': '..--..',
             '=': '-...-',
             "'": '.----.',
             '/': '-..-.',
             '!': '-.-.--',
             '-': '-....-',
             '_': '..--.-',
             '"': '.-..-.',
             '(': '-.--.',
             ')': '-.--.-',
             '$': '...-..-',
             '&': '....',
             '@': '.--.-.',
             '+': '.-.-.'}
    _de_list = {v:k for k,v in _en_list.items()}
    # en_list: 加密表, de_list: 解密表


    def __init__(self, **option):
        self.text = option['text'].upper()
        self.sep = option['sep']
        if self.sep == ' ':
            Morsecoder._en_list.update({' ': '/'})
            Morsecoder._de_list.update({'/': ' '})
        else:
            Morsecoder._en_list.update({' ': ' '})
            Morsecoder._de_list.update({' ': ' '})
        # 避免重复, 更改空格的样式

        for i in self.text:
            if i not in Morsecoder._en_list:
                uni_char = bin(ord(i))[2:].replace('1', '-').replace('0', '.')
                Morsecoder._en_list.update({i: uni_char})
                Morsecoder._de_list.update({uni_char: i})
 #---------------------------------

    def morse_en(self):
        # En - 摩斯密码加密
        try:
            for i in self.text:
                yield f'{Morsecoder._en_list[i]}{self.sep}'

        except:
            raise MorsecodeError('含有特殊字符')


    def morse_de(self):
        # De - 摩斯密码解密
        try:
            self.text = self.text.split(self.sep)
            # 用sep把code分割为列表

        except:
            raise MorsecodeError('分隔符错误')

        else:
            if self.text[-1] == '':
                # 去除尾部的空元素
                self.text = self.text[0:-1]

            try:
                for i in self.text:
                    yield Morsecoder._de_list[i]

            except:
                raise MorsecodeError('非法摩斯密码')


    def modify(key, value):
        try:
            Morsecoder._en_list.update({key: value})
            Morsecoder._de_list.update({value: key})

        except:
            raise MorsecoderError('修改失败')


    

'''
My Bilibili channel: https://b23.tv/wxyFrS
Thank u 4 using my program
'''

