# Morsecoder
> By Lemonix

![Python 图标](https://img.shields.io/badge/Python-3.6%2B-brightgreen?style=for-the-badge&logo=appveyor)
![Build 图标](https://img.shields.io/badge/Build-Passing-orange?style=for-the-badge&logo=appveyor)
![License 图标](https://img.shields.io/badge/License-Apache-brightgreen?style=for-the-badge&logo=appveyor)

***
### 介绍
一个关于摩斯密码解密与加密的库

 **注** : 本库在设置选项上借鉴了https://gitee.com/hustcc/xmorse ，其他如有雷同纯属巧合

 _Warning:_ 本项目基于 **Python3.6+** 开发，低版本会出现Bug


### v0.5更新内容
- 移除命令行参数
- 优化性能，去除冗余代码
- 添加 *modify* 函数

***
### 使用教程
- 实例化与设置
```python
morse = Morsecoder(text=文本, sep=分隔符)
# 或者
option = {
    text: 文本,
    sep: 分隔符
}
morse = Morsecoder(**option)
```

- 加密与解密
```python
# 加密
for i in morse.morse_en():
    print(i, end='')
print()

# 解密
for i in morse.morse_de():
    print(i, end='')
print()
```

- 查看文本与分隔符
```python
# 文本
morse.text

# 分隔符
morse.sep
```

- 修改或添加摩斯密码对照表的内容
```python
Morsecoder.modify(key, value)
```
***

### 使用实例 (此导入方式仅针对同文件夹导入)

用分隔符"/"加密字符串"你好世界"
```python
from morsecoder import Morsecoder

morse1 = Morsecoder(text='你好世界', sep='/')
for i in morse1.morse_en():
    print(i, end="")
print() # 输出空行
```

解密摩斯密码".-.././--/---/-./../-..-/"

```python
from morsecoder import Morsecoder

morse1 = Morsecoder(text='.-.././--/---/-./../-..-/', sep='/')
for i in morse1.morse_de():
    print(i, end="")
print() # 输出空行
```

向摩斯密码对照表中添加"①"，对应摩斯密码为".-.-.-"
```python
from morsecoder import Morsecoder

Morsecoder.modify('①', '.-.-.-')
```

****
### 参与贡献
Lemonix(开发与测试), CXK-53(优化与测试)
