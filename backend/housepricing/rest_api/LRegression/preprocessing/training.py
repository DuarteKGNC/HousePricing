import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from joblib import dump



file_path = "/Users/duartemiranda/Desktop/side_projects/house_pricing/backend/housepricing/rest_api/LRegression/datasets/"
filename = "Cleaned_Housing.csv"

df = pd.read_csv(file_path+filename)

def split_data():
    Xcols = list(df.columns)[1:]
    Ycols = ['price']
    y = df.loc[:, Ycols]
    X = df.loc[:, Xcols]
    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True, random_state=1, train_size=.75)
    return X_train, X_test, y_train, y_test

X_train, X_test, y_train, y_test = split_data()


model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)


def plot_pred(X_test, y_test, y_pred):
    # Sort the test data for plotting the line correctly
    sorted_indices = np.argsort(X_test.iloc[:, 1].values)
    X_test_sorted = X_test.iloc[sorted_indices, 0]
    y_test_sorted = y_test.iloc[sorted_indices]
    y_pred_sorted = y_pred[sorted_indices]

        # Scatter plot of actual values
    plt.scatter(X_test_sorted, y_test_sorted, color='b', label='Actual')

        # Plot the predicted values as a line
    plt.plot(X_test_sorted, y_pred_sorted, color='k', label='Predicted')

    plt.xlabel(f"Feature: {X_test.columns[0]}")  # Example: Area, or another feature name
    plt.ylabel("Price")
    plt.legend()
    plt.show()

# Uncomment to plot
#plot_pred(X_test, y_test, y_pred)

#Save model
print('Saving Model...')
model_name = '/Users/duartemiranda/Desktop/side_projects/house_pricing/backend/housepricing/rest_api/LRegression/models/Linear_Regression_housing.joblib'
dump(model, model_name)
print('Model Saved!!')