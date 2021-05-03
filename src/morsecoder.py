# Morsecoder
# By Lemonix
# Version: 0.4

from sys import argv
from getopt import getopt

class MorsecodeError(Exception):
    # 自定义异常
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class morsecoder:
    VERSION = 0.4
    AUTHOR = 'Lemonix'  
    __en_list = {'A': '.-',
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
    __de_list = {v:k for k,v in __en_list.items()}
    # en_list: 加密表, de_list: 解密表

    def __init__(self, option):
        self.code = option['code'].upper()
        self.sep = option['sep']
        self.en_list = morsecoder.__en_list
        self.de_list = morsecoder.__de_list
        if self.sep == " ":
            self.en_list.update({' ': '/'})
        else:
            self.en_list.update({' ': ' '})
        # 避免重复, 更改空格的样式

    def __str__(self):
        # 如果print该实例就返回code
        return repr(self.code)

    def __len__(self):
        # 返回code的长度
        return len(self.code)

    def __bool__(self):
        # 检测该实例的code是否为空
        if self.code:
            return True
        else:
            return False
 #---------------------------------

    def morse_en(self):
        # En - 摩斯密码加密
        try:
            for i in self.code:
                yield f'{self.en_list[i]}{self.sep}'

        except:
            raise MorsecodeError('含有特殊字符')


    def morse_de(self):
        # De - 摩斯密码解密
        try:
            self.code = self.code.split(self.sep)
            # 用sep把code分割为列表

        except:
            raise MorsecodeError('分隔符错误')

        else:
            if self.code[-1] == '':
                # 去除尾部的空元素
                self.code = self.code[0:-1]

            try:
                for i in self.code:
                    yield self.de_list[i]

            except:
                raise MorsecodeError('非法摩斯密码')
 
       
    



if __name__ == '__main__':
    if len(argv) == 1:
        option1 = {
                'code': 'Lemonix',
                'sep': '/'
                }
        morse1 = morsecoder(option1)
        print(f"Text of morse1: {morse1}")
        for i in morse1.morse_en():
            print(i, end='')
        print() # 输出空行
       
        option2 = {
                'code': '.-.././--/---/-./../-..-/',
                'sep': '/'
                }
        morse2 = morsecoder(option2)
        print(f"Text of morse2: {morse2}")
        for i in morse2.morse_de():
            print(i, end='')
        print() # 输出空行


    elif len(argv) == 4:
        arg, opt = getopt(argv[1:], '-d-e', ['sep='])
        arg_option = {
                'code': opt[0],
                'sep': arg[1][1]
                }
        arg_morse = morsecoder(arg_option)
        # opt[0]: code, arg[1][1]: sep

        if '-d' in arg[0]:
            # 解密
            for i in arg_morse.morse_de():
                print(i, end='')
            print()

        elif '-e' in arg[0]:
            # 加密
            for i in arg_morse.morse_en():
                print(i, end='')
            print() 

'''
My Bilibili channel: https://b23.tv/wxyFrS
Thank u 4 using my work
'''

