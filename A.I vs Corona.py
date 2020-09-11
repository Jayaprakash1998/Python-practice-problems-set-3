'''       QUESTION:

A.I vs Corona:

US Department of Energy’s Oak Ridge National Laboratory(ORNL)  has deployed the world’s most powerful and smartest supercomputer, IBM built Summit, 
in the fight to find a vaccine for the Coronavirus. Researchers from ORNL were granted emergency computation time on Summit, 
using it to perform simulations with unprecedented speed.

In just 2 days Summit identified and studied 77 small-molecule drug potential compounds to fight against the COVID-19 (new Coronavirus). 
However it needs some human knowledge to find the vaccine. Summit will give you n results. You can have as many rats as you want for testing. 
From n results only one works without any side effects. Now your task is to find the minimum number of rats required to find the correct vaccine.

Input Format : Single Integer N

Input Constraints : 1<=N<=10^18

Output Format : Single integer output

Sample Input :
120713504806493995

Sample Output :
57



















HINTS:

1 - Think like a Machine.

2 - Binary.

3 - Bit Length.

'''
















































# ANSWER:

n = int(input())
print(n.bit_length())
