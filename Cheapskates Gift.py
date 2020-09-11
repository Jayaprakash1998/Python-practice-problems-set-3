'''      QUESTION:

Cheapskates Gift :

What coin will he gift?

Rohit is a stingy person, he does not like spending money. He had a friend by the name Kamal, and he invited Rohit for his daughter's birthday party. 
He was happy to go to the party but a sad that he had to spend some money to buy a gift for her. He didn't want to spend much in buying the gift. 
He knew that Kamal's daughter had a coin collection, so he thought he can give a coin which she didn't have and that too a least possible value coin as possible. 
But he didn't wanna look that much obviously stingy, so he decided not to give a coin of any denomination that she has already and 
also the coin value must not be equal to sum of any coins she has already, but also least value coin as possible. So can you help Rohit to find the least value coin as possible.

Note: Lets assume there are coins of all denominations

Input Format

First line of input has one single integer N denoting the various denominations of coins Kamal's daughter has

The second line of input has N spaced integer denoting each domination.

Constraints

1<=N<=10^9

1<=a[i]<=10^9

N - number of denominations

a[i] - Value of denomination

Output Format

Least possible Value of the coin

Input Format : The first line of input has one single integer N denoting the various denominations of coins Kamal's daughter has the second line of input has 
N spaced integer denoting each domination.

Input Constraints : 1<=N<=10^3
1<=a[i]<=10^9
N - numebr of denominations
a[i] - Value of denomination

Output Format : The least possible value of the coin

Sample Input :
3
1 2 5

Sample Output :
4















HINTS:

1 - Take an array, calculate sum of each subset. Find a pattern.

2 - Sort the array and use a greedy approach to solve.

3 - Start with 0. traverse through the array. When the sum of array (arr[0]+arr[1]+...+arr[i])+1 is less than arr[[i+1], 
    the answer is (arr[0]+arr[1]+...+arr[i])+1.

'''
























# ANSWER:

n = int(input())
l = list(map(int,input().split()))
g = 1
l.sort()
for i in l:
    if(g>=i):
        g+=i
    else:
        break
print(g)
