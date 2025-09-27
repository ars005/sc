# Getting the weights and the threshold value
print("Enter weights:")

w11 = int(input("weight w11 = "))
w12 = int(input("weight w12 = "))
w21 = int(input("weight w21 = "))
w22 = int(input("weight w22 = "))
v1 = int(input("weight v1 = "))
v2 = int(input("weight v2 = "))

print("Enter threshold value:")
theta = int(input("theta = "))

# Input and expected output for XOR
x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]
z = [0, 1, 1, 0]  # expected output for XOR

# Initialize variables
con = 1
zin1 = [0, 0, 0, 0]
zin2 = [0, 0, 0, 0]
y1 = [0, 0, 0, 0]
y2 = [0, 0, 0, 0]
yin = [0, 0, 0, 0]
y = [0, 0, 0, 0]

# Main loop
while con:
    for i in range(4):
        zin1[i] = x1[i]*w11 + x2[i]*w21
        zin2[i] = x1[i]*w12 + x2[i]*w22

    for i in range(4):
        if zin1[i] >= theta:
            y1[i] = 1
        else:
            y1[i] = 0

        if zin2[i] >= theta:
            y2[i] = 1
        else:
            y2[i] = 0

    for i in range(4):
        yin[i] = y1[i]*v1 + y2[i]*v2
        if yin[i] >= theta:
            y[i] = 1
        else:
            y[i] = 0

    print("Output of net:")
    print(y)

    if y == z:
        con = 0
    else:
        print("Net is not learning. Enter another set of weights and threshold value.")
        w11 = int(input("weight w11 = "))
        w12 = int(input("weight w12 = "))
        w21 = int(input("weight w21 = "))
        w22 = int(input("weight w22 = "))
        v1 = int(input("weight v1 = "))
        v2 = int(input("weight v2 = "))
        theta = int(input("theta = "))

# Print final result
print("\nMcCulloch-Pitts Net for XOR Function")
print("Weights of neuron z1:")
print("w11 =", w11)
print("w21 =", w21)
print("Weights of neuron z2:")
print("w12 =", w12)
print("w22 =", w22)
print("Weights of output neuron y:")
print("v1 =", v1)
print("v2 =", v2)
print("Threshold value =", theta)
print("Final Output:", y)
