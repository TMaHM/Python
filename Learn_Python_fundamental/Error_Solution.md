# **The error with Python**

1.编码问题

> **Error:** 'gbk' codec can't decode byte 0x88 in position 8: illegal multibyte sequence
>
> **Solution1:** FILE_OBJECT= open('order.log','r', encoding='UTF-8')
> **Solution2:** 在文件开头加注释：# -*- coding: utf-8 -*- （TODO：周一到公司看看能不能用）

2.格式问题

> **Warning:** pep8格式检测要求
> 1. 在文件首部增加`帮助`
> 2. 首句结尾加句号`.`
