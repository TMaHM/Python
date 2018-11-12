# **Learning Python**

## **1. Python对文件操作**

1. file = open("filename", "method")
2. cont = file.read()
3. print(cont)
4. file.close()

> **file.read()**
    > 1. file.read(4) --> 读取4byte
    > 2. file.read() == file.read(-1) --> 读取全部内容
    > 3. 如果在读取全部内容后再次读取，会返回一个空string
    >
> **file.readlines()**
    > 1. 按行读取文件并返回每行内容
    > 2. 两种写法（输出方式不同）

```python
Code1:
    file = open("test.txt", "r", encoding='UTF-8')
    print(file.readlines())
    file.close()

    >>>
    ['Line 1 text \n', 'Line 2 text \n', 'Line 3 text']
    >>>

Code2:
    file = open("test.txt", "r", encoding='UTF-8')
    for line in file:
        print(line)
    file.close()

    >>>
    Line 1 text

    Line 2 text

    Line 3 text
    >>>
```

> **file.write()**

## **2. Python基本概念**

### **2.1 Dictionary**

Like `list` ---- `dictionary` keys can be assigned to different values.

Unlike `list` ---- a new `dictionary` key can be assigned a value, not just ones that already exist.

```python
Code:
    squares = {1:1, 2:4, 3:"error", 4:16}
    squares[8] = 64
    squares[3] = 9
    print(squares)

    >>>
    {1:1, 2:4, 3:9, 4:16, 8:64}
    >>>
```

----
To determine whether a key is in a dictionary, `in` and `not in` can be used.

```python
nums = {1:"one", 2:"two", 3:"three"}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

>>>
True
False   #`three` is the value, but `3` is the key
True
>>>
```

----
Method

1. get

    This method does the same thing as indexing, but if the key is not found in the dictionary, it returns a specify value `None` by default rather than an error.

    > dictionary.get(key, default)
    >> return the value for key if key is in the dictionary, else default.

----

## **2.2 tuple**

`tuple` is very similar to `list`, except that it is immutable(it cannot be changed).

```python
words = ("spam", "eggs", "sausages",)
print(words[0])
words[1] = "cheese"

>>>
spam
TypeError:'tuple' object does not support item assignment
```

----

## **2.3 list**

### **2.3.2 list slice**

`List slice` provides a more advanced way to retrieving values from a list.

```python
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[:3])
print(squares[7:])

>>>
[4, 9, 16, 25]
[0, 1, 4]
[49, 64, 81]
>>>
```

>If a negative value is used for the step, the slice is done backwards.
>
>Using [::-1] as a slice is a common and idiomatic way to reverse a list.

----

### **2.3.3 list comprehension**

`List comprehension` is a useful way of quickly creating lists whose contents obey a simple rule.

```python
cubes = [i**3 for i in range(5)]
evens=[i**2 for i in range(10) if i**2 % 2 == 0]
print(cubes)
print(evens)

>>>
[0, 1, 8, 27, 64]
[0, 4, 16, 36, 64]
>>>
```

----

## **2.4 string format**

`String format` provides a more powerful way to embed non-string within strings.

```python
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)

>>>
Numbers: 4 5 6
>>>
```

```python
a = "{x}, {y}".format(x=5, y=12)
print(a)

>>>
5, 12
>>>
```

----

## 3. Function

### String

> **3.1 join**
>> joins a list of strings with another string as a separator.
> ```python
> print(",".join(["spam", "eggs", "ham"]))
> >>>
> spam, eggs, ham
> >>>

> **3.2 replace**
>> replaces one substring in a string with another.
> ```python
> print("Hello, Me".replace("Me", "world"))
> >>>
> Hello, world
> >>>

> **3.3 startswith & endswith**
>> determine if there is a substring at the start or end of a string.
> ```python
> print("This is a sentence.".startswith("This"))
> print("This is a sentence.".endswith("sentence."))
> >>>
> True
> True
> >>>

> **3.4 upper & lower**
>> to change the case of a string.
> ```python
> print("This is a sentence.".upper())
> print("THIS IS A SENTENCE.".lower())
> >>>
> THIS IS A SENTENCE.
> this is a sentence.
> >>>

> **3.5 split**
>> the opposite of join, turning a string with a certain separator into a list.
> ```python
> print("spam, eggs, ham".split(","))
> >>>
> ['spam', 'eggs', 'ham']
> >>>

> **3.6 Numberic Function**
>
>print(min(1, 2, 3, 4, 0, 2, 1))
>
>print(max([1, 4, 9, 2, 5, 6, 8]))
>
>print(abs(-99))
>
>print(abs(42))
>
<<<<<<< HEAD
>print(sum([1, 2, 3, 4, 5]))

### Functional

> **3.7 lambda**
>> `lambda` functions aren't as powful as named functions.
>> They can only do things that require a single expression - usually equivalent to a single line of code.
> ```python
> #named function
> def polynomial(x):
>   return x**2 + 5*x + 4
> print(polynomial(-4))
>
> #lambda
> print((lambda x:x**2 + 5*x + 4)(-4))

> **3.8 map & filter**
>> oprate on lists(or similar objects called iterables)
>
>> `map` takes a function and an iterable as arguments, and returns a new iterable with the function applied to each argument.
> ```python
> def add_five(x):
> return x + 5
> nums = [11, 22, 33, 44, 55]
> result = list(map(add_five, nums))
> print(result)
> ```
> we can achieve the same result more easily by using `lambda` syntax.
> ```python
> nums = [11, 22, 33, 44, 55]
> result = list(map(lambda x:x+5, nums))
> >>>
> [16, 27, 38, 49, 60]
> >>>
> ```
>
>> `filter` filters an iterable by removing items that don't match a predicate(a function that returns a Boolean).
> ```python
> nums = [11, 22, 33, 44, 55]
> res = list(filter(lambda x:x%2==0, nums))
> print(res)
> ```
