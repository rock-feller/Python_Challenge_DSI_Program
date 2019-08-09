"""author = Rockefeller"""


#the answer is x = 36 , y = 1 ,  z =1

#here is the explanation

First of all, I wrote a code giving me all the possible "3 integers multiplications" leading to 36 which is  33.  
With the goal of extracting the right three numbers, I  based myself on Victoria's assumptions  to  eliminate couple of them. 
Using the third assumption, we can remove ( 6,6 ,1) , (1,6,6) , (6,1,6). 
We are left with 30 of them.

All the possible addition of numbers with the remaining list of multiplications are either 21  or 13  or  11  or 10  or 14  or 38.

For simplicity and era sake, I took the naive assumption that the person is born in the 90's (Since even someone born on 11 / 11 / 1234 will get us to the point, this making  the triplet (9 , 4 , 1) one of the right shots.) 
This naive assumptions makes  21 and 38 the two only reachable additions.

I randomly picked one of tons of possiblities I left with which is my birthday date (for uniqueness sake) and  I assigned to Victoria which is  09 / 03 / 1997.
 which gave me the triplet ( 36 , 1 , 1 ) and the addition is 38.
