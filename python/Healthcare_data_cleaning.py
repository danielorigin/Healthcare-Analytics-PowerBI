import pandas as pd
import numpy as np
import os

#load orignal data
excel_path = "D:/ALL PROJECT/Data Analysics Projects/Healthcare-Analytics-PowerBI/data/raw data/healthcare_dataset.csv"
df = pd.read_csv(excel_path)

# -------------------------
# DATA CLEANING
# -------------------------

# Remove duplicates
df = df.drop_duplicates()
# Clean column names
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
)

# Clean text
text_cols = df.select_dtypes(include='object').columns
# Convert names to proper case
df["name"] = df["name"].str.title()

# Convert dates correctly
df["date_of_admission"] = pd.to_datetime(df["date_of_admission"], errors="coerce")
df["date_of_admission"] = df["date_of_admission"].dt.strftime("%d/%m/%Y")

#Display the first row:
#print(df.iloc[0])
#add US dollars $ sign
df["billing_amount"] = df["billing_amount"].map("${:,.2f}".format)


#print(df)

# Save cleaned data
df.to_csv("hospital_Dataset_cleaned.csv", index=False)
print("Cleaned dataset saved successfully.")