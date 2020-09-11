'''      QUESTION:

Door No.90:

You have been kidnapped and locked behind a door.The door has a door number. The key to the door is a number which is a combination 0’s and 9’s. 
Find the smallest number with 0 and 9 combinations so that number is divisible by the door number.

Input Format : Single Integer N

Input Constraints : 1<=N<=500

Output Format : Single line integer output

Sample Input :
1

Sample Output :
9




















HINTS:

1 - Base 2.

2 - Binary.

3 - *10 + 9

'''




















































# ANSWER:

n = int(input())
k = 1
while(int(bin(k)[2:])*9%n!=0):
    k+=1
print(int(bin(k)[2:])*9)

