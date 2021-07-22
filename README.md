# Morsecoder
> By Lemonix

![Python 图标](https://img.shields.io/badge/Python-3.6%2B-brightgreen?style=for-the-badge&logo=appveyor)
![Build 图标](https://img.shields.io/badge/Build-Passing-orange?style=for-the-badge&logo=appveyor)
![License 图标](https://img.shields.io/badge/License-Apache-brightgreen?style=for-the-badge&logo=appveyor)

***
## 介绍
一个关于摩斯密码解密与加密的库

 _Warning:_ 本项目基于 **Python3.6+** 开发，低版本会出现Bug


## v0.51更新内容
- 细节优化，修复已知Bug
- 性能优化，去除冗余代码
- 添加getArgs, setArgs等函数
- morse_en和morse_de函数分别改为getEncode和getDecode
- 美化__str__和__repr__魔术方法的返回值，print出来的结果更明了
- 完善文档

### v0.52预告
- 使用内部调用函数，速度更快
- 更强大的setArgs方法
- __slots__魔术变量的使用
- toString和toList方法让生成结果更方便

***
## 使用教程 (以下[ ]内的内容代表可选参数)
- 实例化与设置
```python
morse = Morsecoder( [文本, 分隔符] )
```

- 加密与解密
```python
# 加密
for i in morse.getEncode():
    print(i, end='')
print()

# 解密
for i in morse.getDecode():
    print(i, end='')
print()
```

- 查看文本与分隔符
```python
# 文本
morse.getArgs()['text']

# 分隔符
morse.getArgs()['sep']
```

- 修改或添加摩斯密码对照表的内容
```python
# key是键，value是值
Morsecoder.modify(key, value)
```

- 初始化后设置参数
```python
morse.setArgs(文本, 分隔符)
```

- 查看对照表内容
```python
# enList为编码表，deList为解码表
Morsecoder.getList(对照表类型)
```

***

## 使用实例 (此导入方式仅针对同文件夹导入)

用分隔符"/"加密字符串"你好世界"
```python
from morsecoder import Morsecoder

morse1 = Morsecoder(text='你好世界', sep='/')
for i in morse1.getEncode():
    print(i, end="")
print() # 输出空行
```

输出:
```
-..----.--...../-.--..-.-----.-/-..---....-.--./---.-.-.-..--../
```


解密摩斯密码".-.././--/---/-./../-..-/"

```python
from morsecoder import Morsecoder

morse1 = Morsecoder(text='.-.././--/---/-./../-..-/', sep='/')
for i in morse1.getDecode():
    print(i, end="")
print() # 输出空行
```

输出:
```
LEMONIX
```


向摩斯密码对照表中添加"①"，对应摩斯密码为".-.-.-"
```python
from morsecoder import Morsecoder

Morsecoder.modify('①', '.-.-.-')
```


部分功能测试
```python
from morsecoder import Morsecoder

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
```

输出:
```
...././.-../.-../---/ /.--/---/.-./.-../-../
HELLO WORLD

Instance -> 'Morsecoder'
Text(11) -> '...././.-../.-../---/ .--/---/.-./.-../-..'
Sep(1) -> '/'
        
Help on class Morsecoder in module __main__:

class Morsecoder(builtins.object)
 |  Morsecoder(text='', sep='')
 |  
 |  基于Python3.6+的摩斯密码库,
 |  支持编码, 译码, 自定义密码
 |  
 |  Methods defined here:
 |  
 |  __init__(self, text='', sep='')
 |      初始化参数,
 |      设置文本, 分隔符以及自动分析空格,
 |      如果当前文本含有不在对照表不包含的字符时,
 |      会通过Unicode进行编码
 |  
 |  __repr__ = __str__(self)
 |  
 |  __str__(self)
 |      Return str(self).
 |  
 |  getArgs(self)
 |      获取当前实例的参数
 |  
 |  getDecode(self)
 |      获取当前实例的译码
 |  
 |  getEncode(self)
 |      获取当前实例的编码
 |  
 |  getList(listType)
 |      获取编码表或译码表
 |  
 |  modify(key, value)
 |      修改编码表或译码表
 |  
 |  setArgs(self, text, sep)
 |      设置当前实例的参数
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  AUTHOR = 'Lemonix'
 |  
 |  VERSION = 0.51

None
```

****
## 参与贡献
Lemonix(开发与测试), Sherlockcxk(优化与测试)

[Lemonix-Gitee](https://gitee.com/lemonix)

[Lemonix-Github](https://github.com/lemonix-xxx)

[Sherlockcxk-Gitee](https://gitee.com/cxk-53)

[Sherlockcxk-Github](https://github.com/sherlockcxk)

## 你知道吗
Morsecoder第一个版本:RtMorsecoder于2021/1/11 17:19发布

Morsecoder的灵感来源于本项目的共同开发者[Sherlockcxk](https://github.com/sherlockcxk)的C#项目Morsecoder
