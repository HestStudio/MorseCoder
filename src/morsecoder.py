# Morsecoder 0.22
from sys import argv
from getopt import getopt


class MorsecodeError(Exception):
    # 自定义异常
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class morsecoder:
    '''
    小型摩斯密码库 Morsecoder  v0.22
    By Lemonix   2021/04/24
    '''
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

    def __init__(self, code, *, sign="/"):
        self.code = code.upper()
        self.sign = sign 
        if self.sign == " ":
            morsecoder.__en_list.update({" ": "/"})
        else:
            morsecoder.__en_list.update({" ": " "})

    def __str__(self):
        return repr(self.code)

    def __len__(self):
        return len(self.code)

    def __bool__(self):
        if self.code:
            return True

        else:
            return False
 #---------------------------------

    def en(self):
        # En - 摩斯密码加密
        try:
            for i in self.code:
                yield f'{morsecoder.__en_list[i]}{self.sign}'

        except:
            raise MorsecodeError("含有特殊字符")

    

    def de(self):
        # De - 摩斯密码解密
        try:
            self.code = self.code.split(self.sign)

        except:
            raise MorsecodeError("分隔符错误")

        else:
            if self.code[-1] == "":
                self.code = self.code[0:-1]

            try:
                for i in self.code:
                    yield morsecoder.__de_list[i]

            except:
                raise MorsecodeError("非法摩斯密码")
        
    



if __name__ == "__main__":
    if len(argv) == 1:
        morse1 = morsecoder('Lemon ix', sign='/')
        for i in morse1.en():
            print(i, end='')
        print()
        
        morse2 = morsecoder('.-.././--/---/-./../-..-/', sign='/')
        for i in morse2.de():
            print(i, end='')
        print()


    elif len(argv) == 4:
        arg, opt = getopt(argv[1:], '-d-e', ['sign='])
        arg_morse = morsecoder(opt[0], sign=arg[1][1])
        if '-d' in arg[0]:
            for i in arg_morse.de():
                print(i, end='')
            print()

        if '-e' in arg[0]:
            for i in arg_morse.en():
                print(i, end='')
            print()
        


'''
Bilibili channel: https://b23.tv/wxyFrS
Thank u 4 using my work
'''

