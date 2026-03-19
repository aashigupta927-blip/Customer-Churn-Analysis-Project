import pandas as pd

# Load CSV file
file_path = r"C:/Users/hp/Downloads/Telco_customer_churn_Analysis.csv"
df = pd.read_csv(file_path)

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Remove duplicate rows
df = df.drop_duplicates()

# Remove completely blank rows
df = df.dropna(how="all")

# Clean TotalCharges column
df["TotalCharges"] = df["TotalCharges"].astype(str).str.strip()
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Clean MonthlyCharges column
df["MonthlyCharges"] = pd.to_numeric(df["MonthlyCharges"], errors="coerce")

# Remove rows where these columns have errors
df = df.dropna(subset=["TotalCharges", "MonthlyCharges"])

# Reset index
df = df.reset_index(drop=True)

# Save cleaned file (download)
output_path = r"C:/Users/hp/Downloads/Clean_Telco_customer_churn_Analysis.csv"
df.to_csv(output_path, index=False)

print("✅ Data cleaning completed!")
print("📁 Clean file saved at:", output_path)