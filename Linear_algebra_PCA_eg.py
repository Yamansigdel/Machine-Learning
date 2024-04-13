import numpy as np
from sklearn.decomposition import PCA

# Sample dataset (2D)
data = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])

# Initialize PCA with 2 components (you can change this based on your needs)
pca = PCA(n_components=2)

# Fit PCA to the data
pca.fit(data)

# Transform the data into the new coordinate system
transformed_data = pca.transform(data)

# Print the transformed data
print("Original data:")
print(data)
print("\nTransformed data:")
print(transformed_data)
