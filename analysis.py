import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

pd.set_option('display.max_columns', None)  # Show all columns in the output
pd.set_option('display.width', 1000)  # Set the display width to avoid line breaks

df = pd.read_csv('amazon_ecommerce.csv', low_memory=False)
    
if "category" in df.columns:
    category_counts = df["category"].value_counts()
    print("Product Counts by Category:")
    print(category_counts)
    
if "price" in df.columns and "category" in df.columns:
    average_price_by_category = df.groupby("category")["price"].mean()
    print("\nAverage Price by Category:")
    print(average_price_by_category)

top_products = (
    df.groupby(["category", "product_id"])
    .agg({
        "rating": "mean",
        "review_count": "sum"
    })
    .reset_index()
    .sort_values(["category", "rating", "review_count"], ascending=[True, False, False])
)

print("\nTop Products by Category:")
top_5_each_category = top_products.groupby("category").head(5)
print(top_5_each_category)

avg_price_df = average_price_by_category.reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(x="category", y="price", data=avg_price_df)
plt.title("Average Price by Category")
plt.xlabel("Category")
plt.ylabel("Average Price")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("average_price_by_category.png")
plt.show()
