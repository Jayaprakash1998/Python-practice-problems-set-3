'''       QUESTION:

Gun Massacre:

There are several gangs, In mideastern countries there prevails a gang called "CRUEL". 
Several cops have attempted to disintegrate the gang but always failed. But there is one cop called Sai, 
somehow managed to breach through the tight security of the gang, and started working under cover in the head of operations. 
There are N people in the head of operations building, and the head did smell something suspicious. So he decided to kill most of them.

The N people were offered N tshirts, each numbered from 1 to N. 
Each person will wear the tshirt and stand in a circle in the position corresponding to the number on his tshirt.
A person will be chosen at random "I" and will be handed a gun. 
He is supposed to shoot the person to his immediate left and pass on the gun to the further left person. 
As they are standing in a circle, this will continue till only one person is left alive. 
So which number should Sai choose so that he is the last person to be alive after the shoot out.

Input Format : Two spaced integers N and I
N – Number of people standing in the circle
I – The position of the person who has the gun at the beginning

Input Constraints : 1<=N,I<=100000000000000

Output Format : One single integer denoting the index of the person who will be left alive after all this.

Sample Input :
3224 60315

Sample Output :
1411















HINTS:

1 - Consider always the gun is given to the first person and find the pattern for different values for N, where N is the number of people.

2 - n & (n+1) == 0

3 - 2 power of N

'''














































# ANSWER:

#include <stdio.h>

int main()
{
    long long int n,k;
   scanf("%lld",&n);
   scanf("%lld",&k);
	long long int m=1;
		long long int ans=0;
		while(m<=n){
			m*=2;}
			m=m/2;
			ans=(n-m)*2 + k;
		if(ans>n){
			printf("%lld",ans%n);
		}
		else
			printf("%lld",ans);

    return 0;
}
