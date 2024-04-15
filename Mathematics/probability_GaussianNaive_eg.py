from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix

# Load Iris dataset
iris = load_iris()
X = iris.data    #contains the features of datasets
y = iris.target     ##contains the label of datasets

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Gaussian Naive Bayes classifier
gnb = GaussianNB()  #this is the model

# Train the classifier
gnb.fit(X_train, y_train)   #Fitting means training the model with features(X_train) and labels(Y_train)

# Predict on the test set
y_pred = gnb.predict(X_test)    #after training, X_test is used for predictions on features and predicted labels are stored

# Generate classification report
print("Classification Report:")
print(classification_report(y_test, y_pred)) #graph between predicted labels and actual labels of testing dataset 

# Generate confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred)) #And there confusion matrix
