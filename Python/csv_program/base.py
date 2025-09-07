import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("data.csv")


print("Preview of dataset:")
print(df.head())


print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

if "Age" in df.columns:
    avg_age = df["Age"].mean()
    print(f"\nAverage Age: {avg_age:.2f}")


if "Gender" in df.columns:
    df["Gender"].value_counts().plot(kind="bar", color=["skyblue", "salmon"])
    plt.title("Gender Distribution")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.show()

if "Age" in df.columns and "Salary" in df.columns:
    plt.scatter(df["Age"], df["Salary"], alpha=0.6, c="blue")
    plt.title("Age vs Salary")
    plt.xlabel("Age")
    plt.ylabel("Salary")
    plt.show()
    
numeric_df = df.select_dtypes(include='number')

plt.figure(figsize=(8,6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
