import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv("AirPassengers.csv")

print("Dataset Preview")
print(df.head())

# Check missing values
print("Missing Values:")
print(df.isnull().sum())

# Create numerical time index
df["Month_Number"] = range(len(df))

X = df[["Month_Number"]]
y = df["#Passengers"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Accuracy
pred = model.predict(X)
print("\nR2 Score:", r2_score(y, pred))

# Predict next 12 months
future = pd.DataFrame({
    "Month_Number": range(len(df), len(df) + 12)
})

future_predictions = model.predict(future)

print("\nFuture Predictions:")
print(future_predictions)

# Visualization
plt.figure(figsize=(10, 5))
plt.plot(df["Month_Number"], y, label="Historical Data")
plt.plot(
    future["Month_Number"],
    future_predictions,
    linestyle="dashed",
    label="Forecast"
)

plt.title("Air Passenger Forecast")
plt.xlabel("Time")
plt.ylabel("Passengers")
plt.legend()
plt.grid(True)

plt.savefig("forecast.png")
print("Graph saved as forecast.png")