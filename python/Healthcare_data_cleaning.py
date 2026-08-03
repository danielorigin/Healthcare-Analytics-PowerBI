import pandas as pd
import numpy as np
import os


excel_path = "C:/Users/Daniel/Downloads/healthcare_dataset.csv"
df = pd.read_csv(excel_path)


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

df["date_of_admission"] = pd.to_datetime(df["date_of_admission"], errors="coerce")
# Format however you want
df["date_of_admission"] = df["date_of_admission"].dt.strftime("%d/%m/%Y")

#Display the first row:
#print(df.iloc[0])
#add US dollars $ sign
df["billing_amount"] = df["billing_amount"].map("${:,.2f}".format)


print(df)