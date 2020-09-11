'''       QUESTION:

Dating Trouble:

Victor is a 20-year-old Engineering student living in Coimbatore. He is an avid user of the Tinder app, a social dating application. 
At the beginning stage of his dating life i.e. first two months, he swiped right on all the profiles. In the fore coming months, he became a bit choosy in swiping right. 
So the number profiles per each right swipe kept increasing as the sum of the previous two months profiles per right swipe count. 
Given Nth month, your task is to find out how many profiles Victor will look into for each right swipe?

Input Format : One single Integer 'N', where N is the Nth month

Input Constraints : 1<= N <= 30

Output Format : One single integer value of the number of profiles Victor looks for each right swipe

Sample Input :
1

Sample Output :
1




















HINTS:

1 - From the given problem description, try to build the sequence starting with 1 and 1.

2 - The series is 1, 1, 1+1,...

3 - You have to print the N-th Fibonacci number. Here, the series starts from 1, 1.

'''


















































# ANSWER:

n = int(input())
x,y=1,0
for i in range(n):
  z=x+y
  x,y=y,z
print(z)
