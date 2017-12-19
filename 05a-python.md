# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>>  
Feature | Tuple | List
------- | ----- | -----
Definition | Collection of values | Collection of values
Denoted by | () | []
Creating new | t = () or t = tuple() | l = [] or l = list()
Mutable? | No (can not be changed) | Yes (can be changed)
Hashable? (has a hash value that can't be changed during lifetime) | Yes | No
Values have to be same type | Yes | No
Can be nested | Yes | Yes
Can be key for dictionary? | Yes, because immutable | No, because mutable
Indexing | Starts at 0, can index from the end | Starts at 0, can be indexed from the end
Can be sliced? | Yes | Yes
Iterable? | Yes | Yes

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>>  
Feature | Set | List
------- | ----- | -----
Definition | Collection of immutable objects | Collection of objects
Denoted by | {} | []
Creating new | s = set() | l = [] or l = list()
Ordered? | No | Yes
Mutable? | Yes (if not frozen) | Yes
Can be key for dictionary? | No (yes, if frozen) | No
Duplicate values allowed? | No | Yes
Values have to be same type | No | No
Can be nested | Yes | Yes
Iterable? | Yes | Yes  

>> It is faster and more efficient to find an element in a set because an algorithm is more efficient. The algorithm used for searching sets is the same as one for searching keys of dictionaries.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> 'lambda' is a keyword that is commonly used to create a small nameless function for doing simple tasks. These functions are limited to a single expression and can be used wherever function objects are needed.
>>
**Using `lambda` to add 2 numbers:**   
```{python}
g = lambda x, y: x + y
```
>>
**Using `lambda` as `key` argument to `sorted`:**   
```{python}
tuples = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
print(sorted(tuples, key=lambda t: t[-1]))
```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> Comprehension is a compact way for creating such data types as lists, sets and dictionaries. They are commonly used to apply some operation or to identify elements that satisfy a certain condition.  

>> **List comprehension examples:**
```{python}
numbers = [x for x in range(1, 9)]
squares = [x ** 2 for x in numbers]
even = [x for x in numbers if x % 2 == 0]
```

>> **Set comprehension examples:**
```{python}
nums_set = set(range(1, 9))
sqrs_set = {x ** 2 for x in numbers}
even_set = {x for x in numbers if x % 2 == 0}
```

>> **Dictionary comprehension examples:**
```{python}
nums_sqrs = {str(x):x ** 2 for x in range(1, 19)}
even_dic = {k:nums_sqrs[k] for k in nums_sqrs if int(k) % 2 == 0}
```

>> `map` applies a given function to a given itterable object and returns the result. `map` can accept multiple itterables and would finish executing when the end of the shortest itterable is reached.

>> **`map` example:**   
```{python}
nums_map = [x for x in range(1, 21)]
sqrs_map = list(map(lambda x: x ** 2, nums_map))
```

>> `filter` applies a given function to a given itterable object and returns only those elements for which function is true. `filter` can accept only one itterable.

>> **`filter` example:**   
```{python}
nums_filter = [x for x in range(1, 21)]
even_filter = list(filter(lambda x : x % 2 == 0, nums_filter))
```

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)
