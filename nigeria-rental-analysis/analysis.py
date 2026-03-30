import os
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# SETTINGS
# -----------------------------
DATA_PATH = "data/nigeria-rent.csv"
OUTPUT_DIR = "outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv(DATA_PATH)

print("Original shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

print("\nData info:")
print(df.info())

# -----------------------------
# BASIC CLEANING
# -----------------------------

# Convert date
df["DATE_ADDED"] = pd.to_datetime(df["DATE_ADDED"], errors='coerce')

# Remove unrealistic prices
df = df[(df["PRICE"] >= 100000) & (df["PRICE"] <= 100000000)]

# Remove unrealistic values
df = df[(df["BEDROOMS"] >= 1) & (df["BEDROOMS"] <= 10)]
df = df[(df["BATHROOMS"] >= 1) & (df["BATHROOMS"] <= 10)]
df = df[(df["TOILETS"] >= 1) & (df["TOILETS"] <= 15)]

print("\nAfter cleaning:", df.shape)

# Save cleaned data
df.to_csv(f"{OUTPUT_DIR}/cleaned_data.csv", index=False)

# -----------------------------
# ANALYSIS
# -----------------------------

# Top locations (median is better than mean)
top_locations = df.groupby("LOCATION")["PRICE"].median().sort_values(ascending=False).head(10)

# Price by bedrooms
price_by_bedroom = df.groupby("BEDROOMS")["PRICE"].median().sort_index()

# Price by house type
price_by_house = df.groupby("HOUSE_TYPE")["PRICE"].median().sort_values(ascending=False)

print("\nTop 10 most expensive locations:")
print(top_locations)

print("\nMedian price by bedrooms:")
print(price_by_bedroom)

# Save results
top_locations.to_csv(f"{OUTPUT_DIR}/top_locations.csv")
price_by_bedroom.to_csv(f"{OUTPUT_DIR}/price_by_bedrooms.csv")
price_by_house.to_csv(f"{OUTPUT_DIR}/price_by_house_type.csv")

# -----------------------------
# VISUALIZATIONS
# -----------------------------

# Top locations chart
plt.figure()
top_locations.sort_values().plot(kind='barh')
plt.title("Top 10 Most Expensive Locations")
plt.xlabel("Median Price")
plt.ylabel("Location")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/top_locations.png")
plt.close()

# Bedrooms chart
plt.figure()
price_by_bedroom.plot(kind='bar')
plt.title("Price by Number of Bedrooms")
plt.xlabel("Bedrooms")
plt.ylabel("Median Price")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/price_by_bedrooms.png")
plt.close()

# House type chart
plt.figure()
price_by_house.plot(kind='bar')
plt.title("Price by House Type")
plt.xlabel("House Type")
plt.ylabel("Median Price")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/price_by_house_type.png")
plt.close()

print("\nDone. Check your outputs folder.")