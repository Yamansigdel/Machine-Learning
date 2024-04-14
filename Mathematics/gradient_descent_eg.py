import numpy as np

# Define the function to minimize (example: y = 2x^2 + 3x + 1)
def f(x):
    return 2 * x**2 + 3 * x + 1

# Define the derivative of the function (gradient)
def df(x):
    return 4 * x + 3

# Gradient Descent function
def gradient_descent(initial_x, learning_rate, num_iterations):
    x = initial_x
    for _ in range(num_iterations):
        gradient = df(x)
        # Update x using gradient descent rule
        x = x - learning_rate * gradient
    return x

# Parameters
initial_x = 0  # Initial guess for x
learning_rate = 0.1  # Step size for each iteration
num_iterations = 100  # Number of iterations

# Run gradient descent
optimized_x = gradient_descent(initial_x, learning_rate, num_iterations)
print("Optimized x:", optimized_x)
print("Minimum value of f(x):", f(optimized_x))
