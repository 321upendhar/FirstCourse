Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nums=[12,23,34,45,56,67,78]
>>> nums
[12, 23, 34, 45, 56, 67, 78]
>>> names=['kiran','vikram','rajesh']
>>> names
['kiran', 'vikram', 'rajesh']
>>> values=[9.5,'navin',25]
>>> values
[9.5, 'navin', 25]
>>> mil=[nums,values]
>>> mil
[[12, 23, 34, 45, 56, 67, 78], [9.5, 'navin', 25]]
>>> nums[0]
12
>>> nums[4]
56
>>> nums[6]
78
>>> nums[-3]
56
>>> nums[-6]
23
>>> nums[3:]
[45, 56, 67, 78]
>>> nums[2:5]
[34, 45, 56]
>>> nums[:2]
[12, 23]
>>> nums.append(87)
>>> nums
[12, 23, 34, 45, 56, 67, 78, 87]
>>> nums.copy()
[12, 23, 34, 45, 56, 67, 78, 87]
>>> nums.insert(3,55)
>>> nums
[12, 23, 34, 55, 45, 56, 67, 78, 87]
>>> nums.pop(2)
34
>>> nums
[12, 23, 55, 45, 56, 67, 78, 87]
>>> nums.pop()
87
>>> nums.remove(56)
>>> nums
[12, 23, 55, 45, 67, 78]
>>> nums.reverse()
>>> nums
[78, 67, 45, 55, 23, 12]
>>> nums.count()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    nums.count()
TypeError: count() takes exactly one argument (0 given)
>>> nums.count[1:4]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    nums.count[1:4]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> nums.count(sum)
0
>>> nums
[78, 67, 45, 55, 23, 12]
>>> nums(min)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    nums(min)
TypeError: 'list' object is not callable
>>> min(nums)
12
>>> max(nums)
78
>>> sum(nums)
280
>>> nums.extend(34)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    nums.extend(34)
TypeError: 'int' object is not iterable
>>> nums.extend([22,34])
>>> nums
[78, 67, 45, 55, 23, 12, 22, 34]
>>> del nums.()
SyntaxError: invalid syntax
>>> del nums(45)
SyntaxError: cannot delete function call
>>> nums.remove(45)
>>> nums
[78, 67, 55, 23, 12, 22, 34]
>>> nums.sort()
>>> nums
[12, 22, 23, 34, 55, 67, 78]
>>> nums.reverse()
>>> nums
[78, 67, 55, 34, 23, 22, 12]
>>> nums.remove(34)
>>> nums
[78, 67, 55, 23, 22, 12]
>>> nums.pop(12)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    nums.pop(12)
IndexError: pop index out of range
>>> nums.pop(3)
23
>>> nums
[78, 67, 55, 22, 12]
>>> nums.pop()
12
>>> nums
[78, 67, 55, 22]
>>> nums.insert(3,44,45)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    nums.insert(3,44,45)
TypeError: insert expected 2 arguments, got 3
>>> nums.insert(3,44)
>>> nums
[78, 67, 55, 44, 22]
>>> nums.index()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    nums.index()
TypeError: index expected at least 1 argument, got 0
>>> nums.index(2)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    nums.index(2)
ValueError: 2 is not in list
>>> nums.index(55)
2
>>> 