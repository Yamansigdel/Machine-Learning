# with a target value
import numpy as np

# Define the function to minimize (example: y = 2x^2 + 3x + 1)
def f(x):
    return 2 * x**2 + 3 * x + 1

# Define the derivative of the function (gradient)
def df(x):
    return 4 * x + 3

# Define the loss function
def loss_function(x, target_value):
    return (f(x) - target_value) ** 2

# Define the derivative of the loss function
def dloss_function(x, target_value):
    return 2 * (f(x) - target_value) * df(x)

# Gradient Descent function
def gradient_descent(initial_x, learning_rate, num_iterations, target_value):
    x = initial_x
    for i in range(num_iterations):
        gradient = dloss_function(x, target_value)
        # Update x using gradient descent rule
        x = x - learning_rate * gradient
        # Check for invalid values
        if np.isnan(x) or np.isinf(x):
            print(f"Iteration {i}: Invalid value encountered. Terminating optimization.")
            break
    return x

# Parameters
initial_x = 0  # Initial guess for x
learning_rate = 0.01  # Step size for each iteration
num_iterations = 1000 # Number of iterations
target_value = 5  # Example target value

# Run gradient descent
optimized_x = gradient_descent(initial_x, learning_rate, num_iterations, target_value)
print("Optimized x:", optimized_x)
print("Minimum value of f(x):", f(optimized_x))
print("Value of f(x) at target value:", f(target_value))
