import pandas as pd
from ydata_profiling import ProfileReport

# Step 1: Load data
df = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/imdb_1000.csv')

# Step 2: Create profile report
profile = ProfileReport(df, title="IMDB 1000 Dataset Profile Report", explorative=True)
profile.to_file("day_2_etl/imdb_1000_profile_report.html")

# Step 3: Clean data
df_clean = df.dropna()

print(df_clean.head())

# Step 4: Export cleaned data
df.to_csv("day_2_etl/imdb_1000_cleaned.csv", index=False)

print("ETL + Profiling completed successfully.")