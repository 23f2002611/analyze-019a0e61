import pandas as pd
import json
import sys

def process_data(file_path):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(json.dumps({"error": f"File not found: {file_path}"}), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(json.dumps({"error": f"Error reading CSV: {e}"}), file=sys.stderr)
        sys.exit(1)

    # Calculate total sales
    total_sales = df['Sales'].sum()

    # Calculate average order value
    average_order_value = df['Sales'].mean()

    # Identify top 5 products by sales
    top_products = df.groupby('Product')['Sales'].sum().nlargest(5).to_dict()

    # Calculate total revenue by region (fixed typo)
    revenue_by_region = df.groupby('Region')['Sales'].sum().to_dict()

    # Prepare results
    results = {
        "total_sales": total_sales,
        "average_order_value": average_order_value,
        "top_products": top_products,
        "revenue_by_region": revenue_by_region
    }

    print(json.dumps(results, indent=4))

if __name__ == "__main__":
    process_data('data.csv')