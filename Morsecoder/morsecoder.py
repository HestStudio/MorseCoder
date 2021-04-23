# Morsecoder 0.2
import sys

class MorsecodeError(Exception): # 自定义异常
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class morsecoder:
    '''
    小型摩斯密码库 Morsecoder  v0.2
    By Lemonix   2021/04/23
    更新内容: 增加命令行解密和加密的操作
    '''

    __en_list = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--.", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----", '.': '.-.-.-', ':': '---...', ',': '--..--', ';': '-.-.-.', '?': '..--..', '=': '-...-', "'": '.----.', '/': '-..-.', '!': '-.-.--', '-': '-....-', '_': '..--.-', '"': '.-..-.', '(': '-.--.', ')': '-.--.-', '$': '...-..-', '&': '....', '@': '.--.-.', '+': '.-.-.'}
    __de_list = {v:k for k,v in __en_list.items()}

    def __init__(self, code, *, ptype=list):
        '''
        实例化一个摩斯密码文本
        test = morsecoder(".-/" [, ptype='list'('str') ])
        ptype为返回结果的类型, list返回list, str返回string
        '''
        self.code = code.upper()
        self.ptype = ptype

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

    def en(self): # encrypt加密
        '''
        encrypt 加密文本
	code.en()

        例子:
            test = morsecoder("Lemonix")
            print(test.en())
        输出:
             .-.././--/---/-./../-..-/
        '''
        try:
            res_list = []
            res_str = ""
            for i in self.code:
                res_list.append(morsecoder.__en_list[i])
                res_str += f"{morsecoder.__en_list[i]}/"

        except:
            raise MorsecodeError("Contains special characters")

        else:
            if self.ptype == "list":
                return res_list

            elif self.ptype == "str":
                return res_str



    def de(self): # decode解密
        '''
        decode 解密文本
        code.de()

        例子:
            test = morsecoder(".-.././--/---/-./../-..-/")
            print(test.de())
        输出:
            LEMONIX
        '''
        try:
            res_list = []
            res_str = ""
            type_code = self.code.split("/")

        except:
            raise MorsecodeError("Error sign")

        else:
            if type_code[-1] == "":
                type_code = type_code[0:-1]

            try:
                for i in type_code:
                    res_list.append(morsecoder.__de_list[i])
                    res_str += morsecoder.__de_list[i]

            except:
                raise MorsecodeError("Error morsecode")

            else:
                if self.ptype == "list":
                    return res_list

                elif self.ptype == "str":
                    return res_str
        

 
if __name__ == "__main__":
    if len(sys.argv) == 1:
        test1 = morsecoder("ABCD", ptype="str")
        print(test1)
        print(test1.en())
        test2 = morsecoder(".-/-.../", ptype="str")
        print(test2.de())
        print(len(test2))

    elif len(sys.argv) == 4:
        arg = sys.argv[1:]
        if arg[0] == "-de":
            test = morsecoder(arg[1], ptype=arg[2])
            print(test.de())

        elif arg[0] == "-en":
            test = morsecoder(arg[1], ptype=arg[2])
            print(test.en())


'''
Bilibili channel: https://b23.tv/wxyFrS
Thank u 4 using my work
'''

