import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv("house_price.csv")   

print("Preview of dataset:")
print(df.head())
print("\nDataset Info:")
print(df.info())

print("\nMissing values:\n", df.isnull().sum())

X = df[["area", "rooms"]]  
y = df["price"]            

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nModel Coefficients:", model.coef_)
print("Model Intercept:", model.intercept_)

print("R² Score:", r2_score(y_test, y_pred))
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("RMSE:", rmse)


plt.scatter(df["area"], df["price"], color="blue", alpha=0.6)
plt.xlabel("Area (sq ft)")
plt.ylabel("Price")
plt.title("Area vs Price")
plt.show()

sns.boxplot(x=df["rooms"], y=df["price"], palette="Set2")
plt.title("Rooms vs Price")
plt.show()

plt.scatter(y_test, y_pred, color="green", alpha=0.6)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices")
plt.show()
