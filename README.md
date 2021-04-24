# Morsecoder
## By Lemonix

***
### 介绍
一个关于摩斯密码解密与加密的库模块

 _Warning:_ 本项目基于 **Python3.6+** 开发，低版本会出现Bug

### v0.22更新内容
- 更新命令行参数，使用更方便
- 更新调用方式，更快速
- 添加空格的对照表

***
### 函数使用教程
- 实例化
> morse = morsecoder(code, sign=sign)

> code为要加密或要解密的内容，sign为分隔符
- 加密(返回迭代器，需要通过for循环获取内容)
> test.en()
- 解密(返回迭代器，需要通过for循环获取内容)
> test.de()
- 查看文本内容
> print(test)
- 查看文本长度
> len(test)

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

morse1 = morsecoder("Lemonix", sign="/")
for i in morse1.en():
    print(i, end="")
print() # 输出空行
```

解密摩斯密码".-/"

```python
import morsecoder

morse1 = morsecoder(".-/", sign="/")
for i in morse1.de():
    print(i, end="")
print() # 输出空行
```

命令行参数加密字符串"Lemonix"

```python
python morsecoder.py -e --sign=/ Lemonix
```

命令行参数解密摩斯密码".-/"

```python
python morsecoder.py -d --sign=/ .-/
```




### 参与贡献
Lemonix(开发与测试), CXK-53(测试)