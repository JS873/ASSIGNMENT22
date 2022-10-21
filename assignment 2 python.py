#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# que:1 Write a Python program to check if a number is positive, negative or zero


n = int(input("Enter The Number : "))
if n>0 :
    print("This Value is Positive")
elif n<0 :
    print("This Number is Negative")
else :
    print("it is zero")


# In[1]:


#que 2 : Write a Python program to get the Factorial number of given number.


b = int(input("Enter the value : "))
g=1

if b < 0:
    print("Factorial does not exist for negative numbers")

elif b == 0:
    print(b ,"`s factorial is 1")
else :
    for t in range (1,b + 1):
        g = g*t
    print("The factorial of",b,"is",g)


# In[2]:


#Write a Python program to get the Fibonacci series of given range.
# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")

elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)

else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1


# ### que: 4 How memory is managed in Python?
# Memory management in Python involves a private heap containing all Python objects and data structures. The management of this private heap is ensured internally by the Python memory manager. The Python memory manager has different components which deal with various dynamic storage management aspects, like sharing, segmentation, preallocation or caching.
# 

# ### que 5: What is the purpose continue statement in python?
# The continue statement in Python returns the control to the beginning of the while loop. The continue statement rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop. The continue statement can be used in both while and for loops.

# In[26]:


#que 6 : Write python program that swap two number with temp variable and without temp variable.

x = 7
y = 9

temp = x
x = y
y = temp
print("swapped values are :{}".format(x))
print("swapped values are :{}".format(y))


# In[24]:


#que 7: Write a Python program to find whether a given number is even or odd,
#print out an appropriate message to the user

j = int(input("enter the value : "))

if (j % 2) == 0:
    print("{0} is even".format(j))
else :
    print("{0} is odd".format(j))


# In[42]:


#que 8 : Write a Python program to test whether a passed letter is a vowel or not. 

y = str(input("enter the letter : "))

if y.lower() in ['a' , 'e' , 'i' ,'o' ,'u']:
    print("vowel")
elif y.upper() in ['A' , 'E' , 'I' , 'O' , 'U']:
    print("vowel")
else :
    print("constant")

    


# In[52]:


#que 9: Write a Python program to sum of three given integers. However, if
#two values are equal sum will be zero. 

""""n1 = int(input("enter the number : "))
n2 = int(input("enter the number : "))
n3 = int(input("enter the number : "))

sum = n1+n2+n3
print("given sum of three number is : ",sum)"""

def sum(a,b,c):
    if a==b or b==c or c==a :
        sum = 0
    else :
        sum = a+b+c
    return sum
        
print(sum(2,1,2))
print(sum(1,2,3))
print(sum(2,2,1))
print(sum(2,2,3))



# In[3]:


#que 10: Write a Python program that will return true if the two given integer
#values are equal or their sum or difference is 5. 

def t2(x, y):
   if x == y or abs(x-y) == 5 or (x+y) == 5:
       return True
   else:
       return False
print(t2(7, 2))
print(t2(3, 2))
print(t2(2, 2))
print(t2(7, 3))
print(t2(27, 53))


# In[ ]:


#que 11 :Write a python program to sum of the first n positive integers. 

n = int(input("Input a number: "))
x1 = (n * (n + 1)) / 2
print("Sum of the first", n ,"positive integers:", x1)


# In[ ]:


#que 12: Write a Python program to calculate the length of a string

def sl(str1):
    count = 0
    for char in str1:
        count += 1
    return count
print(sl('this assignment is so long'))


# In[1]:


#que 13:Write a Python program to count the number of characters (character
##frequency) in a string 

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com'))


# ### que 14: What are negative indexes and why are they used?
# 
# Negative Indexing is used to in Python to begin slicing from the end of the string i.e. the last. Slicing in Python gets a sub-string from a string.
# 
# 
# 

# In[2]:


#que 15 : Write a Python program to count occurrences of a substring in a string. 

str1 = 'Today is the Best day for citizens'
print()
print(str1.count("citizens"))
print()


# In[ ]:


#que 16: Write a Python program to count the occurrences of each word in a given sentence 

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))


# In[ ]:


#que 17 : Write a Python program to get a single string from two given strings,
#separated by a space and swap the first two characters of each string.

def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))


# In[7]:


""""que 18 : Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add
'ly' instead if the string length of the given string is less than 3, leave it
unchanged."""

def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'

  return str1
print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))


# In[13]:


#que 19: Write a Python program to find the first appearance of the substring
#'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
#whole 'not'...'poor' substring with 'good'. Return the resulting string. 

def not_poor(str1):
  snot = str1.find('not')
  spoor = str1.find('poor')
    
if spoor > snot and snot>0 and spoor>0:
    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
    return str1
else :
    return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))




# In[ ]:


#que 20: Write a Python function that takes a list of words and returns the length
#of the longest one. 

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["PHP", "Exercises", "Backend"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])


# In[14]:


#que 21: Write a Python function to reverses a string if its length is a multiple of
4. 

def reverse_string(str1):
    if len(str1) % 4 == 0:
       return ''.join(reversed(str1))
    return str1

print(reverse_string('abcd'))
print(reverse_string('python'))


# In[15]:


#que 22: Write a Python program to get a string made of the first 2 and the last
#2 chars from a given a string. If the string length is less than 2, return
#instead of the empty string. 


def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))


# In[16]:


#que 23: Write a Python function to insert a string in the middle of a string. 

def insert_sting_middle(str, word):
    return str[:2] + word + str[2:]

print(insert_sting_middle('[[]]', 'Python'))
print(insert_sting_middle('{{}}', 'PHP'))
print(insert_sting_middle('<<>>', 'HTML'))


# In[ ]:




