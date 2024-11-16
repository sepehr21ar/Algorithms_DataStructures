def Item1 (n): # O( n )
    for i in range(n):
        print(i)

# Item1(8)



def Item2 (n): # O( 2n )
    for i in range (n):  # YES IT IS  O(2n) BUT WE KNOW THIS AS  drop constants. SO IS ---> O(n)
        print(i)# HTEY ARE SAME IN THIS , SUPPOSE YOU HAVE JUST ONE LOOP
    for j in range(n):
        print(j)
# Item2 (8)


def Item3 (n): # O( n * n)
    for i in range(n):
        for j in range(n):
            print(i , j)

# Item3(8)

def Item4 (n): #  O ( n + n^2 )  ----- > O ( n^2 )
    for i in range(n):# NON dominant
        for j in range(n):
            print(i, j)
    for k in range (n):
        print(k)

# Item4(k)

def add_item(n): # O( 1 )
    return n + n #  i have  one  opration

def add_item2(n):  #  O( 2 ) --> O( 1 )
    return n + n + n    # in real is o( 1 ) becuase it goes to one part


def input_terms(a , b): # if there is two parameter in function we can not say O (2n ) = O(n) becouse htey are different param
    for i in range (a): # in this we have a , b so it is O(a + b)  and if is nasted we have O( a * b)
        print(i)
    for j in range (b):
        print(j)