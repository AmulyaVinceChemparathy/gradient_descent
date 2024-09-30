#program to calculate the line paramters - theta1 and theta2 using gradient descent

import numpy as np
x = [60.0, 63.0, 65.0, 70.0, 70.0, 70.0, 80.0, 90.0, 80.0, 80.0, 85.0, 89.0,
90.0, 90.0, 90.0, 90.0, 94.0, 100.0, 100.0, 100.0]
y = [1.0, 0.0, 1.0, 2.0, 5.0, 1.0, 4.0, 6.0, 2.0, 3.0, 5.0, 4.0, 6.0, 8.0, 4.0,
5.0, 7.0, 9.0, 7.0, 6.0]
X = np.array(x, dtype=np.float64)
Y = np.array(y, dtype=np.float64)
m=0.1
b=-10
lr=0.0001
epochs=1000000
n=float(len(x))
for i in range(epochs):
    y_new=m*X+b
    Dm=(-2/n)*sum((Y-y_new)*X)
    Db=(-2/n)*sum(Y-y_new)
    m=m-lr*Dm
    b=b-lr*Db
print("Value of Theta0 (intercept): {}\nValue of Theta1 (slope): {}".format(b,
m))
print("Prediction for x=97:",m*97+b)