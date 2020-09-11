'''       QUESTION :

Perfect Photographer :

Victor is a professional photographer, he has shot several world class photographs. One fine evening, he was walking in the sidewalk of a park. 
He came across Annie Leibovitz, who is known to be one of the best photographers in the world and she was one of Victor's role model. 
He quickly rushed to Annie and asked her permission to be her assistant. She gave victor a task. There was a twin before them, Chin and Chan. 
They both had an identical square kite of equal dimension. They held the kite up-straight and its base was parallel to the ground. 
You saw that from the distance and you could not differentiate between the two kites, since from your line of sight, both the kites were overlapping each other. 
The begun to rise the kite, and both the kites went up along the x=y line. But both the kites went up at different speeds. 
As the square kites are moving at different speeds, now they could visibly see both the kites. 
Since they are moving up along a same line, the intersection formed visibly between them was also a square. 
Annie told that she will say the area of the intersection X, and Victor had to click the photo exactly when the overlapping area is equal to X. 
Help victor with a time at which he has to click the photograph so that he will be able to click the photo at that exact second and get to be the assistant of his role model.

Input Format : The first line of input has one single integer input N, where N corresponds to the side of the Square kite
The second line of input has two integer inputs S1 and S2, where S1 and S2 are the speeds at which kite 1 and kite 2 rise correspondingly
The last line of input has one single integer input K, where K is the area of intersection between two kites

Input Constraints : 1<=N,S1,S2,K<=10^9

Output Format : Output specifying the time at which the photo has to be clicked. Round off the value to 2 decimal points.

Sample Input :
395
307 232
15

Sample Output :
7.38











HINTS:

1 - Speed = distance / time.

2 - Consider the diagonals of the two squares.

3 - Make use of square root of 2. Be careful with the precision.

'''

















































# ANSWER:

import math
l=int(input())
s1,s2=map(int,input().split())
sa=int(input())
side=math.sqrt(sa)
r2=math.sqrt(2)                         
ans = round(((l*r2)-(side*r2))/(abs(s1-s2)),2)
print(ans)
