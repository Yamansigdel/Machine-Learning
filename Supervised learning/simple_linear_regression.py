#Linear Regression with one variable

import numpy as np
import matplotlib.pyplot as plt
#plt.style.use('./deeplearning.mplstyle')

x_train=np.array([1.0,2.0])
y_train=np.array([300.0,500.0])


w=200; b=100    #Parameters

def  model(x,w,b):
    m=x.shape[0] #m=len(x_train)
    f_wb= np.zeros(m)
    for i in range(m):
        f_wb[i]= w * x[i] + b

    return f_wb

y_pred= model(x_train,w,b)
plt.plot(x_train, y_pred, c='b', label='Prediction')

plt.scatter (x_train,y_train, marker='x', c='r', label=' Actual Values')

# Set the title
plt.title("Housing Prices")
# Set the y-axis label
plt.ylabel('Price (in 1000s of dollars)')
# Set the x-axis label
plt.xlabel('Size (1000 sqft)')
plt.legend()
plt.show()
    
    
