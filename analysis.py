import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_books_dataset.csv")

# Basic statistics
print("===== BOOK PRICE ANALYSIS =====")

print(f"Average Price: £{df['Price'].mean():.2f}")
print(f"Minimum Price: £{df['Price'].min():.2f}")
print(f"Maximum Price: £{df['Price'].max():.2f}")

# Rating analysis
print("\n===== RATING ANALYSIS =====")

rating_counts = df["Rating"].value_counts()

print(rating_counts)

print("\nMost Common Rating:")
print(rating_counts.idxmax())

# Top 5 most expensive books
print("\n===== TOP 5 MOST EXPENSIVE BOOKS =====")

top_books = df.sort_values("Price", ascending=False)

print(top_books[["Title", "Price", "Rating"]].head())