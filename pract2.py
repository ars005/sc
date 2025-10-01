A=dict()
B=dict()
Y=dict()

A={"a":0.2,"b":0.3,"c":0.6,"d":0.6}
B={"a":0.9,"b":0.9,"c":0.4,"d":0.5}
print('the fisrt fuzzy set is:',A)
print("the second fuzzy set is",B)

# UNION degree_of_memebership(Y)= max(degree_of_memberhship(A),degree_of_membership(B))
#print('\n A union B') 
for A_KEY, B_KEY in zip(A,B):
    A_VALUE= A[A_KEY]
    B_VALUE=B[B_KEY]
    if A_VALUE>B_VALUE:
     Y[A_KEY]=A_VALUE
    else:
     Y[B_KEY]=B_VALUE
    print("fuzzy union:",Y)


for A_KEY,B_KEY in zip(A,B):
    A_VALUE=A[A_KEY]
    B_VALUE=B[B_KEY]

    if A_VALUE<B_VALUE:
        Y[A_KEY]=A_VALUE
    else:
        Y[B_KEY]=B_VALUE

        print("fuzzy set intersection",Y)
