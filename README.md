# Morsecoder
## By Lemonix

***
### 介绍
一个关于摩斯密码解密与加密的库模块
 _Warning:_ 基于 **Python3.6+** 开发，低版本会出现Bug

### v0.22更新内容
- 更新命令行参数，使用更方便
- 更新调用方式，更快速
- 添加空格的对照表

***
#### 函数使用教程
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
 **更多例子在代码的最后部分** 
#### 命令行参数使用教程
python morsecoder.py -d(-e) --sign=sign code
-d(-e) 为解密(加密)
sign为分隔符
code为文本内容

如果文本内容与格式正确会把结果print出来
***

### 参与贡献
Lemonix, CXK-53