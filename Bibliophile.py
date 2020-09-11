'''     QUESTION:

Bibliophile:

Victor has a great love for books. He has a huge collection of books at his garage. Victor has a weird way of organizing the books. 
He stores them in order or the number of pages he has remaining to complete the books. 
He has arranged the books in the above order such that it will be easy for him to decide which book he has to read in a given amount of time. But one day, 
Victor's niece came to his garage and took a few books out of the rack and put it randomly in. 
So victor now wants to check whether the books are still remaining in the same order as he desires.

Input Format : The first line of input has one single integer input N, where N is the number of books that Victor has and the second line of input has N spaced integers 
denoting the number of pages that victor has in completing a particular book

Input Constraints : 1<=N<=10^4
1<=a[i]<=10^17

Output Format : Yes or No

Sample Input :
5
1 2 3 4 5

Sample Output :
Yes
























HINTS:

1 - Check the list is arranged in order or not.

2 - if it is in order, print Yes.

3 - Otherwise print No.

'''












































# ANSWER:

x=int(input())
lst=list(map(int,input().split()))

flag = 0
i=1
while i < len(lst):
    if lst[i] < lst[i-1]:
        flag = 1 
        break
    i=i+1 
    
if flag==0:
    print("Yes")
else:
    print("No")
