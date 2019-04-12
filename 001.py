"""
Day 1: 2019-04-12
Title: Your order, please
Link: https://www.codewars.com/kata/your-order-please/python

Description:
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""

"""

# My Solution
def order(sentence):
    wl=[]
    words = sentence.split()
    for word in words:
        for char in word:
            if char.isdigit():
                wl.append((word, char))
    wl = sorted(wl, key=lambda x:x[1])
    return " ".join([i[0] for i in wl])

# Best Solution
def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))
    
    
