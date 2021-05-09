# Morsecoder
> By Lemonix

![Python 图标](https://img.shields.io/badge/Python-3.6%2B-brightgreen?style=for-the-badge&logo=appveyor)
![Size 图标](https://img.shields.io/badge/Size-4.6k-red?style=for-the-badge&logo=appveyor)
![Build 图标](https://img.shields.io/badge/Build-Passing-orange?style=for-the-badge&logo=appveyor)
![License 图标](https://img.shields.io/badge/License-Apache-brightgreen?style=for-the-badge&logo=appveyor)

***
### 介绍
一个关于摩斯密码解密与加密的库

 **注** : 本库在设置选项上，借鉴了https://gitee.com/hustcc/xmorse，其他如有雷同纯属巧合

 _Warning:_ 本项目基于 **Python3.6+** 开发，低版本会出现Bug

### v0.4更新内容
- 更新设置方式

- 自定义摩斯密码

***
### 函数使用教程
- 实例化
> morse = morsecoder(code, sign=sign)

> code为要加密或要解密的内容，sign为分隔符
- 加密(返回迭代器，需要通过for循环获取内容)
> test.morse_en()
- 解密(返回迭代器，需要通过for循环获取内容)
> test.morse_de()
- 查看文本内容
> print(test)
- 查看文本长度
> len(test)
- 查看是否为空code
> bool(test)
- 自定义摩斯密码
> 实例.en_code.update({k: v})

***
### 命令行参数使用教程
python morsecoder.py -d(-e) --sign=sign code

> -d(-e) 为解密(加密)

> sign为分隔符

> code为文本内容

如果文本内容与格式正确会把结果print出来
***

### 使用实例

加密字符串"Lemonix"
```python
import morsecoder

option = {
    'code': 'Lemonix', 
    'sep': '/'
}

morse1 = morsecoder(option)
for i in morse1.morse_en():
    print(i, end="")
print() # 输出空行
```

解密摩斯密码".-.././--/---/-./../-..-/"

```python
import morsecoder

option = {
    'code': '.-.././--/---/-./../-..-/', 
    'sep': '/'
}

morse1 = morsecoder(option)
for i in morse1.morse_de():
    print(i, end="")
print() # 输出空行
```

命令行参数加密字符串"Lemonix"

```bash
python morsecoder.py -e --sep=/ Lemonix
```

命令行参数解密摩斯密码".-/"

```bash
python morsecoder.py -d --sep=/ .-/
```




### 参与贡献
Lemonix(开发与测试), CXK-53(测试)
