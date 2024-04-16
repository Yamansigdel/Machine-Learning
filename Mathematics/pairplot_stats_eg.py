import seaborn as sns
import matplotlib.pyplot as plt

# Load the built-in Iris dataset
iris = sns.load_dataset("iris")

# Create a pairplot
sns.pairplot(iris)
plt.show()
