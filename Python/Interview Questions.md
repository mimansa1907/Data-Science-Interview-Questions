Mention different cases of mentioning variables with python.
1. Camel case - Second and subsequent words are capatialized
2. Pascal case - Identical to camel case but first word is also capatialized
3. Snake case - All words in lower case separated by '_'

Everything in python is object.
This means all the elements in python are objects and they have their few methods and attributes associated to them.

## Functions in Python

- What is overloading? Does python support overloading?
When two or more methods with same name are given different number of parameters this process is called overloading. Python does not support overloading, so consider if we declare two methods with distinct number of agruments, the latest method will be execeuted. Although there can be certain ways in which we can achieve overloading.

1) Use *args as parameter
```
```
2) Passing 'None'
```
```

3) Using Multiple Dispatch Decorator
```
```

- What are __call__() methods?
Creates callable instance. 
In python callable object is one which can be called with a pair of parantheses and optionally a series of arguments. To produce callable instance of a class we use *.__call__().



EXAMPLE

- How does __init__() and __call__() differ?
- List built-in functions in python

## Vairables in Python

- What is a variable?
A symbolic name to Memory container that stores any data. When ever any value is meant to be stored in memory a corresponding object is created. We use variable to refer to this object.

Variables hold references to objects.
Objects live in concrete memory positions.

- How to see all the methods associated with a variable?
With use of **dir()** function.
- What are 3 core properties of an object?
1. Type
2. Identity
3. Value
We can confirm object type with __class__,type() as well as isinstance(). type() gives exact class to which the object belong whereas instance returns true or false if the object belongs to any particular instance passed as arg in the function.



- List datatypes available in python.
1. Numeric types - integer , floating-point, complex numbers
2. Boolean types - 
3. Iterator types - 
4. Sequence types - 
a.Mutable
b.Immuatable
5.Text Sequence type
6. Binary sequence type
7. Set types
8. Mapping types

- What happens when you assign one variable to other variable in python?
Both the variables  point to same object.

- Why n=30, m=30 has same id() values where are n = 300, m = 300 does not? 
Default objects for range [-5,256] are available in python, where as object for number greater than 256 created as declared. Therefore, n=30 and m=30 points to same object of default objects, whereas n=300 and m=300 creates two different objects.

- List number of reserved keywords in python.
33

- What ar rules of naming a variable?
1. can have uppercase, lowercase,0-9(not at beginning),_
2. Case sensitive
3. Follow snake case 


- What is id() function?
This is a identifier function. It stores identity of the object, which is an integer value,it remains unique and constant throughtout the lifetime of an object.


- What is meaning of dynamic typing?
This means that the data type of variable is only determined at runtime.

- What is purpose of locals() and globals()  functions in python?

- Explain variable unpacking in python.[https://medium.com/geekculture/python-variable-unpacking-a5d0ed284011]
Variable unpacking allows one to assign all elements of an iterable object to multiple variables at once.
```
# Simple Unpacking
>>> users = ['John','Selena','Justin']
>>> user1, user2, user3 = users
>>> user1, user2, user3
('John','Selena','Justin')
>>> user1
John

# Multiple level unpacking
>>> attrs = [1,['Catlina',56],['Hanks',44]]
>>> user_id,(user1,score),(user2,score)
>>> user1
Catlina

# Extended Unpacking


```


- What is reference counting is python?
It is one of the memory management technique, which keeps track of the number of variable references assigned to any object. Once the  count of variables attached to any object becomes 0, that object is cosidered dead and the memory associated to that object is deallocated.

- ":=" explain. (Present from python3.8 onwards)
This is known as Walrus operator


- What is PEP8 convention to write mutli-word variable name?
Write each word separated by underscore. Eg: step_count, start_index,

- What is meaning of 'nonlocal keyword' in python?


- How to add or delete values to lists and dicts? List and explain all the function operations avaialble associated with them.
*Lists Methods*
|-----------------------------|-----------------------------------------------------|
| Function                    | Operation                                           |
|-----------------------------|-----------------------------------------------------|
| a_list.append(item)         | Appends item to the end of a_list.                  |
| a_list.clear()              | Removes all items from a_list.                      |
| a_list.extend(iterable)     | Extends a_list with the contents of iterable.       |
| a_list.insert(index, item)  | Inserts item into a_list at index.                  |
| a_list.pop(index)           | a_list.pop(index)                                   |
| a_list.remove(item)         | Removes the first occurrence of item from a_list.   |
| a_list.reverse()            | Reverses the items of a_list in place.              |
| is not                      | a_list.sort(key=None, reverse=False)                |
|-----------------------------|------ ----------------------------------------------|

*Operator functions*
1. Concatenate (+) can also be use as '+='
2. Repetition (*) can also be use as '*='

*Dict Methods*
|-------------------------------------|------------------------------------------------------------------------------------------------|
|a_dict.clear()	                      |  Removes all key-value pairs from a_dict.                                                      |
|a_dict.pop(key[, default])	          |  Removes the key-value pair under key and returns the value, or default if the key doesn’t     |
|                                     |  exist                                                                                         |
|a_dict.popitem()	                  |  Removes and returns the most recently added key-value pair as a tuple like (key, value).      |
|a_dict.setdefault(key[, default])	  |  Inserts a new key-value pair with default as its value.                                       |
|a_dict.update([other])	              |  Updates the dictionary with the key-value pairs, overwriting existing keys and creating       |
|                                     |  newkeysfor missing ones.                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------|
Keys are always hashable objects, this means they can be, bytes, strings, tuples, nums, float. But not lists, dicts or sets.
NOTE: Tuples are only hashable is they have all hashable items in them.


*Union Operator support*
1. |, and it augmented form '|='
>>> inventory = {"apples": 42} | {"bananas": 24}
>>> inventory
{'apples': 42, 'bananas': 24}


- Explain Sets.
1. They are mutable.
2. Always store unique value.
3. Don't store value in any order hence they don't support indexed access to it's elements.
4. They are a special case of dictionary, wherein, the values in set act as keys like in dict but don't have any values.
5. They store only hashable objects.

*Set Methods*
|-------------------------------------|------------------------------------------------------------------------------------------------|
|a_set.add(element)                   |  
|a_set.update(*others)    	          |  Updates a_set, adding elements from one or more sets unpacked from others. Equivalent to      |
|                                     |  a_set |= other_1 | other_2 ... | other_n                                                      |
|a_set.remove(element)	              |  Removes element from a_set, raising a KeyError if element doesn’t exist.                      |
|a_set.discard(element)	         	  |  Removes element from a_set, skipping the KeyError if element doesn’t exist.                   |
|                                     |  empty.                                                                                        |
|a_set.c;ear()           	          |  Removes all the elements from the set                                                         |
| Set operations                      |                                                                                                |
| a_set.intersection_update(*others)  |  Updates a_set in place, keeping only elements found in it and all others                      |
| a_set.difference_update(*others)    |  Updates a_set in place, removing elements found in others                                     |
| a_set.difference_update(*others)    |  Updates a_set in place, keeping only elements found in either set but not in both             |
|-------------------------------------|------------------------------------------------------------------------------------------------|

*Operator based operations*
1. | Union
>>> {"apple", "orange"} | {"banana"}
{'orange', 'apple', 'banana'}

2. & Intersection
>>> {"apple", "orange"} & {"apple"}
{'apple'}

3. - Difference
>>> {"apple", "orange"} - {"apple", "banana"}
{'orange'}

4. ^ Symmetric difference
>>> {"apple", "orange"} ^ {"apple", "banana"}
{'banana', 'orange'}

5. |= Augumented union
>>> fruits = {"apple", "orange"}
>>> fruits |= {"banana"}  # Augmented union
>>> fruits

6. &= Augumented intersection
>>> fruits &= {"apple"}  # Augmented intersection
>>> fruits
{'apple'}


- How to create immutable sets?
We can use 'Frozen Set' datatype. They only support operations like union,intersection, .isdisjoint(), .issubset(), .issuperset()difference and symmetric difference. Does not support add(), remove() and pop().

- How to create mutable bytes?
We can use 'bytearray'.

```
>>> greeting = bytearray(b"Hello, World!")

>>> greeting[1] = 69
>>> greeting
bytearray(b'HEllo, World!')

>>> greeting[2] = "L"
Traceback (most recent call last):
    ...
TypeError: 'str' object cannot be interpreted as an integer

>>> greeting[2] = b"L"
Traceback (most recent call last):
    ...
TypeError: 'bytes' object cannot be interpreted as an integer

>>> greeting[2] = bytearray(b"L")
Traceback (most recent call last):
    ...
TypeError: 'bytearray' object cannot be interpreted as an integer
```




- List and explain all the functions associated with string

- How to check if a variable belongs to a particular datatype?
1. type()
2. isintance()
3. object_name.__call__ # not preferred method

- What are hashable datatypes in python? Immutable datatypes are hashable

Immutable - int, float, decimal, complex, bool, string, tuple, range, frozenset, bytes

Mutable - list, dict, set, bytearray, user-defined classes
These types allow you to change the value of specific items without affecting the identity of the container object.
Basic operations on can perform on mutation:
1. Item assignment
2. Slice assignment
3. Item Deletion
4. Slice Deletio

- List of some discrete behaviours in Mutable objects.
1. Aliasing Variables
```
>>> number = 42
>>> another_number = number
>>> number += 1
>>> number
43
>>> another_number
42

>>> fruits = ["apple"]
>>> another_fruits = fruits
>>> fruits += ["banana"]
>>> fruits
['apple', 'banana']
>>> another_fruits
['apple', 'banana']
```
Creating aliases for  immutable objects is safe, but not for mutable.

2. Mutating agruments -  Changes values of global mutable variables as well when those variables are passed from a function.

```
>>> def squares_of(numbers):
...     for i, number in enumerate(numbers):
...         numbers[i] = number ** 2
...     return numbers
...

>>> sample = [2, 3, 4]
>>> squares_of(sample)
[4, 9, 16]
>>> sample
[4, 9, 16]
```
If you want to change value a on immutable varaible in a function u can use 'global' keyword.

3. Using Mutable Default Values
There can be two kind of function defintions and each produces different result with mutable objects.

Scenario: We want to pass a list as an argument to a functions with default value.

Case 1: we assign an empty list to a parameter variable.
```
def append_to(item,target=[]):
    target.append(item)
    return target

Step 1:
append_to(1)

Step 2:
append_to(2)

Step 3:
append_to(3)

# Output Step 1:
[1]

# Output Step 2:
[1,2]

# Output Step 3:
[1,2,3]   ########### STRANGE
```

Is my function remembering the list? This because python defines the default argument value when it first parses the function and doesn’t overwrite it in every call, you’ll be working with the same instance every time.

Case 2(Correct way): We assign varaibles to None.
```
def append_to(item,target=None):
    if target is None:
        target = []
    target.append(item)
    return target

Step 1:
append_to(1)

Step 2:
append_to(2)

Step 3:
append_to(3)

# Output Step 1:
[1]

# Output Step 2:
[2]

# Output Step 3:
[3]   ########### Ahhh, I want this.
```

4. Making copies of mutable objects
a. Shallow (copy.copy())
b. Deep (copy.deepcopy())

When you make a shallow copy of an existing list, you create a new list of objects with a different identity. However, the internal components or data items in the new list are just aliases of those in the original list. On the other hand, if you make a deep copy, then you create a completely new copy of the original list.

- string = 'Hello' + 'world' + 'everyone' + 'has' + 'to' + 'die' or string = "".join(['Hello','world','everyone','has','to','die'])
which one is memory optimized?
1. Creates new string objects on each +
2. Using one object and an iterator, performing operations on one object only.


- What are distinct keys that can be stored in  a dictionary?

- What are mutable and immutable objects?  What is difference between them.

```
Both mutable and immutable sequences support the += and *= augmented assignment operators, but they do so differently. Mutable sequences like lists support the += operator through the .__iadd__() method, which performs an in-place addition.

Similarly, mutable sequences support the *= operator through the .__imul__() method, which also performs the operation in place, modifying the underlying sequence.

In contrast, immutable sequences, such as tuples and strings, don’t have the .__iadd__() and .__imul__() methods. Instead, augmented concatenations and repetitions fall back to calling .__add__() and .__mul__(), respectively. These two methods don’t modify the underlying sequence in place but return new sequences.
```

- Is this valid?
letters = "a","b","c","d","e"
This stores the aplhabets as tuple. Using "(",")" is not necessary.

- List all the methods associated with tuple.


- What happens if immutable tuple stores mutable values like list?

- What is the difference between list and array?

- How to update a key value in dictionary?

- How to remove key from dict?

- Combine two dicts, dict1 and dict2, such that the for common keys between dict1 and dict2, the values from dict 2 override, values from dict 1.

- 

- Explain variable __name__ in python.
In Python, the special variable __name__ serves an important role in determining how a script or module is executed. When Python runs a script directly, it sets the __name__ variable for that script to '__main__'. This indicates that the script is being executed as the main program or application.

On the other hand, when a script is imported as a module by another script, the __name__ variable is set to the name of the script/module being imported. This signifies that the script is being executed as part of another program, not as the main program itself.

The distinction is crucial for organizing code effectively. If there are certain instructions within a script that should only run when the script is executed directly as the main program, they can be placed inside a conditional block like if __name__ == '__main__':. This condition ensures that the enclosed code will execute only when the script is invoked directly, not when it's imported as a module by another script.

This approach allows us to include both reusable components (like classes and function definitions) and executable statements within a single script or module, making our Python code more modular and versatile.


- Explain __init__ in python.

- Explain local, universal, global and built-in scopes of variable.

- Explain shallow and deep copy of variable in python.

- Do you know what is the difference between list.sort() and sorted(list)?

- What is List Comprehension? Is it better than a typical loop? Why? Can you demonstrate how to use it?

- What is an iterator?

- What is yield? When do you use it

- Explain zip(), map() and filter().

- Slicing operation

- Relevance of hashing in python.

- How can yo create mutable strings in python?
Use bytearray data type to store string, this helps in mutatiing one particular value at one index in python.




## Operators

List all comparision operators in python.
|--------------|--------------------------|
| Operation    | Meaning                  |
|--------------|--------------------------|
| >            | strictly greater than    |
| <            | strictlt less than       |
| <=           | less than or equal to    |
| >=           | greater than or equal to |
| ==           | equal                    |
| !=           | not equal                |
| is           | object identify          |
| is not       | negated objecct identify |
|--------------|--------------------------|

- What is difference between use of '==' or *is*?[https://stackoverflow.com/questions/132988/is-there-a-difference-between-and-is]
*is* return true if two variables point same object, this implies existence of unique object, whereas '==' returns True if the objects pointed by two variables have same values, implies there can be two different objects. 

We use *is* to check idenity and '==' to check equality.

PEP8 tip:
1. Comparisons to singletons like None should always be done with is or is not, never the equality operators.
2. *is not* is equivalent to *not ... is*. Prior is readable



## Classes

- Are there private variables in classes? How to make attribute of class private.

- What are abstract classes and abstract base classes?

- Special attributes in classes

- What is use of issubclass()? It is used to check child-parent relation between two classes exists or not?

- Why a classes mutable?

- How to control mutabilty of class?
- How to create a class with read-only attributes?

## Exceptions




## Python descriptors




## References

- https://realpython.com/
- https://github.com/bregman-arie/python-exercises
- https://www.analyticsvidhya.com/blog/2024/02/mcqs-on-python-variable/
- https://www.datacamp.com/blog/top-python-interview-questions-and-answers
- https://anywhere.epam.com/en/blog/senior-python-developer-interview-questions
- https://www.geeksforgeeks.org/operator-overloading-in-python/?ref=ml_lbp
- https://hackr.io/blog/python-interview-questions
- https://community.aws/content/2eEahNZZ1tobTtQ7t6JWp7hPpJf/what-s-with-the-__name__-variable-in-python
- https://www.indiabix.com/technical/python/variables/


