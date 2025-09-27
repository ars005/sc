#getting the weights and the threshold value
print("enter weights:")

w11=int(input("weightw11="))
w12=int(input("weightw12="))
w21=int(input("weightw21="))
w22=int(input("weightw22="))
v1=int(input("weightv1="))
v2=int(input("weightv2="))
print("enter threshold value:")
theta=int(input("theta="))
x1=[0,0,1,1];
x2=[0,1,0,1];
z=[0,1,1,0] #expected output for exclusive-OR function
con=1;
zin1=[0,0,0,0]
zin2=[0,0,0,0]
y1=[0,0,0,0]
y2=[0,0,0,0]
yin=[0,0,0,0]
y=[0,0,0,0]
while con:
    for i in range(0,3):
        zin1[i]=x1[i]*w11+x2[i]*w21
        zin2[i]=x1[i]*w21+x2[i]*w22
    for i in range(0,3):
        if zin1[i]>=theta:
            y1[i]=1;
        else:
            y1[i]=0;
        if zin2[i]>=theta:
            y2[i]=1;
        else:
            y2[i]=0;

    for i in range(0,3):
        yin[i]=y1[i]+y2[i]*v2;
        print(yin)

        for i in range(0,3):
            if yin[i]>=theta:
                y[i]=1;
            else:
                y[i]=0;
                print("output of net")
                print(y)
                if y==z:
                    con=0
                else:
                    print("Net is not learning another set of weights and threshold value")
w11=int(input("weightw11="))
w12=int(input("weightw12="))
w21=int(input("weightw21="))
w22=int(input("weightw22="))
v1=int(input("weightv1="))
v2=int(input("weightv2="))
theta=int(input("theta="))
#endwhile
print("McCulloh - pitss Net for XOR Function")
print("weight of neuron z1")
print(w11)
print(w12)
print("weight of neuron z2")
print(w21)
print(w22)
print("weight of neuron y")
print(v1)
print(v2)
print("threshold value")
print(theta)

print(y)