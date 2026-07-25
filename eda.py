import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_books_dataset.csv")

print("===== DATASET OVERVIEW =====")

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\n===== PRICE ANALYSIS =====")

print("Average Price: £", round(df["Price"].mean(), 2))
print("Minimum Price: £", df["Price"].min())
print("Maximum Price: £", df["Price"].max())

print("\n===== RATING ANALYSIS =====")

print("Rating counts:")
print(df["Rating"].value_counts())

print("\nMost Common Rating:")
print(df["Rating"].mode()[0])

print("\n===== AVAILABILITY ANALYSIS =====")

print(df["Availability"].value_counts())

print("\n===== TOP 5 MOST EXPENSIVE BOOKS =====")

top_books = df.sort_values("Price", ascending=False).head(5)

print(top_books[["Title", "Price", "Rating"]])

print("\n===== EDA INSIGHTS =====")

print("1. The dataset contains 100 books with no missing values.")
print("2. Book prices range from £10.16 to £58.11.")
print("3. The average book price is £34.56.")
print("4. The most common rating is One.")
print("5. All books in the dataset are currently in stock.")
print("6. The dataset shows variation in book prices and ratings.")