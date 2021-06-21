#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Update time: 2021/6/19

class MorsecodeError(Exception):
    '''
    自定义异常,
    更明了的异常信息
    '''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Morsecoder:
    '''
    基于Python3.6+的摩斯密码库,
    支持编码, 译码, 自定义密码
    '''
    VERSION = 0.51
    AUTHOR = 'Lemonix'
    __enList = {'A': '.-',
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
            '/': '-..-.',
            '-': '-....-',
            '(': '-.--.',
            ')': '-.--.-',}
    __deList = {v:k for k,v in __enList.items()}
    # enList: 编码表, deList: 译码表


    def __init__(self, text='', sep=''):
        '''
        初始化参数,
        设置文本, 分隔符以及自动分析空格,
        如果当前文本含有不在对照表不包含的字符时,
        会通过Unicode进行编码
        '''
        self.__text = text.upper()
        self.__sep = sep

        if self.__sep == ' ':
            Morsecoder.__enList.update({' ': '/'})
            Morsecoder.__deList.update({'/': ' '})
        
        else:
            Morsecoder.__enList.update({' ': ' '})
            Morsecoder.__deList.update({' ': ' '})
        # 避免重复, 更改空格的样式

        for i in self.__text:
            if i not in Morsecoder.__enList:
                # 用二进制的Unicode进行编码
                uni_char = bin(ord(i))[2:].replace('1', '-').replace('0', '.')
                Morsecoder.__enList.update({i: uni_char})
                Morsecoder.__deList.update({uni_char: i})
    

    def __str__(self):
        return f'''
Instance -> '{type(self).__name__}'
Text({len(self.__text)}) -> '{''.join(self.__text)}'
Sep({len(self.__sep)}) -> '{self.__sep}'
        '''
    __repr__ = __str__


    def setArgs(self, text, sep):
        '''
        设置当前实例的参数
        '''
        self.__text, self.__sep = text.upper(), sep


    def getArgs(self):
        '''
        获取当前实例的参数
        '''
        return {
            'text': self.__text, 
            'sep': self.__sep
            }


    def getEncode(self):
        # En - 摩斯密码编码
        '''
        获取当前实例的编码
        '''
        try:
            for i in self.__text:
                yield f'{Morsecoder.__enList[i]}{self.__sep}'

        except:
            raise MorsecodeError('含有特殊字符')


    def getDecode(self):
        # De - 摩斯密码译码
        '''
        获取当前实例的译码
        '''
        try:
            self.__text.replace(' ', '')
            # 去除空格
            self.__text = self.__text.split(self.__sep)
            # 用sep把code分割为列表

            if self.__text[-1] == '':
                # 去除尾部的空元素
                self.__text.pop()
            
            for i in self.__text:
                yield Morsecoder.__deList[i]

        except:
            raise MorsecodeError('非法摩斯密码')


    def modify(key, value):
        '''
        修改编码表或译码表
        '''
        try:
            Morsecoder.__enList.update({key: value})
            Morsecoder.__deList.update({value: key})
            # 更新编码表和译码表

        except:
            raise MorsecoderError('修改失败')


    def getList(listType):
        '''
        获取编码表或译码表
        '''
        if listType == 'enList':
            return Morsecoder.__enList

        elif listType == 'deList':
            return Morsecoder.__deList

        else:
            MorsecoderError('不存在此对照表')


    
if __name__ == '__main__':
    # 编码演示
    myCode = Morsecoder(text='Hello World', sep='/')
    for values in myCode.getEncode():
        print(values, end='')
    print()
    
    # 译码演示
    myCode.setArgs(text='...././.-../.-../---/ /.--/---/.-./.-../-../', 
                sep=myCode.getArgs()['sep']
                )
    for values in myCode.getDecode():
        print(values, end='')
    print()

    # __str__
    print(myCode)
    
    # Doc
    print(help(Morsecoder))


'''
My Bilibili channel: https://b23.tv/wxyFrS
Thank u 4 using my program
'''