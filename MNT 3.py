Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nums=[22,33,44,55,66]
>>> nums
[22, 33, 44, 55, 66]
>>> nums[0]
22
>>> nums[3]
55
>>> nums[0:4]
[22, 33, 44, 55]
>>> nums[2:]
[44, 55, 66]
>>> nums[:2]
[22, 33]
>>> nums[-3]
44
>>> nums[-4]
33
>>> names=['kiran','kashim','kelvin']
>>> names
['kiran', 'kashim', 'kelvin']
>>> values=[9.5,'navin',25]
>>> mil=[nums,names]
>>> mil
[[22, 33, 44, 55, 66], ['kiran', 'kashim', 'kelvin']]
>>> nums.append(44)
>>> nums
[22, 33, 44, 55, 66, 44]
>>> nums.clear(55)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    nums.clear(55)
TypeError: clear() takes no arguments (1 given)
>>> nums.insert(3,77)
>>> nums
[22, 33, 44, 77, 55, 66, 44]
>>> nums.remove(77)
>>> nums
[22, 33, 44, 55, 66, 44]
>>> nums.remove(44)
>>> nums
[22, 33, 55, 66, 44]
>>> nums.remove(44)
>>> nums
[22, 33, 55, 66]
>>> nums.copy(44)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    nums.copy(44)
TypeError: copy() takes no arguments (1 given)
>>> nums.pop(1)
33
>>> nums
[22, 55, 66]
>>>  nums.pop()
 
SyntaxError: unexpected indent
>>> nums.pop()
66
>>> del nums(1:)
SyntaxError: invalid syntax
>>> del nums(1:)
SyntaxError: invalid syntax
>>> nums.extend(11,34,33,32,31)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    nums.extend(11,34,33,32,31)
TypeError: extend() takes exactly one argument (5 given)
>>> nums.extend([12,24,36,48])
>>> nums
[22, 55, 12, 24, 36, 48]
>>> min(nums)
12
>>> max(nums)
55
>>> sum(nums)
197
>>> nums.pop()
48
>>> nums.pop(2:)
SyntaxError: invalid syntax
>>> del nums[2:]
>>> nums
[22, 55]
>>> nums.sort()
>>> nums
[22, 55]
>>> name="Telusko"
>>> print(name[-3])
s
>>> nums.extend([14,28,27,13])
>>> nums
[22, 55, 14, 28, 27, 13]
>>> nums.copy(14)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    nums.copy(14)
TypeError: copy() takes no arguments (1 given)
>>> nums.copy(2)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    nums.copy(2)
TypeError: copy() takes no arguments (1 given)
>>> nums.copy()
[22, 55, 14, 28, 27, 13]
>>> nums.copy()
[22, 55, 14, 28, 27, 13]
>>> nums.count()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    nums.count()
TypeError: count() takes exactly one argument (0 given)
>>> nums.count(1,2,3)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    nums.count(1,2,3)
TypeError: count() takes exactly one argument (3 given)
>>> nums.count(3:)
SyntaxError: invalid syntax
>>> nums.index()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    nums.index()
TypeError: index expected at least 1 argument, got 0
>>> nums.index(2)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    nums.index(2)
ValueError: 2 is not in list
>>> nums.index(14)
2
>>> 