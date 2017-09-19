# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 17:42:00 2016

@author: Vsevold Loik
"""
#######################################################
varA = 2
varB = 4
if type(varA) == str or type(varB) == str:
    print('string involved')
elif varA > varB:
    print('bigger')
elif varA == varB:
    print('equal')
else: 
    print('smaller')
#######################################################
count = 2
while count <= 10:
    print(count)
    count += 2
print('Goodbye!')
#######################################################
count = 10
print('Hello!')
while count >= 2:
    print(count)
    count -= 2
#######################################################
end = 6
mysum = 0
count = 1
while count <= end:
    mysum = mysum + count
    print(mysum)    
    count += 1
print(mysum)
####################################################### 
for i in range(2,11,2):
    print(i)
print("Goodbye!")
#######################################################
print("Hello!")
for i in range(10,0,-2):
    print(i)
#######################################################
end = 6
mysum = 0
for i in range(1,end+1):
    mysum = mysum + i
    print(mysum)
print(mysum)







#######################################################

# Problem 1
# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s. 
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl'
s = 'azcbobobegghaklaaoi'
vowel = 0
for char in s:
    if char ==  'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
         vowel += 1
print('Number of vowels: ' + str(vowel))


# find Bob
s = 'azcbobobegghaklaaoibobobob'
bob = 0
for i in range(0, len(s)):
    if s[i:i+3] == 'bob':
        bob += 1
print('Number of times bob occurs is: ' + str(bob))


# longest string in alfabetical order

s = 'azcbobobegghakl'
ws = s[0]
bs = ws

for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        ws += s[i+1]
    else:
        ws = s[i+1]
    if len(ws) > len(bs):
            bs = ws
print('Longest substring in alphabetical order is: ' + bs)