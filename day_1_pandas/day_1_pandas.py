import pandas as pd

data = '''
Id,Name,Age,Salary,City
0,Alice,30,70000,
1,Bob,25,50000,New York
2,Charlie,35,80000,
3,David,40,90000,
4,Eve,28,60000,Los Angeles
5,Frank,33,75000,
6,Grace,29,72000,San Francisco
7,Hannah,31,68000,Irvine
8,Ian,27,52000,Seattle
9,Jack,34,85000,Fort Worth
10,Kate,26,54000,Chicago
11,Liam,32,77000,Miami
12,Mia,30,71000,Denver
13,Noah,38,95000,Atlanta
14,Olivia,24,48000,Boston
15,Paul,36,82000,Washington
16,Quinn,29,73000,Phoenix
17,Rachel,35,80000,San Diego
18,Sam,28,60000,Portland
19,Tina,31,69000,Orlando
20,Uma,33,76000,Philadelphia
'''

with open("data.csv", "w") as file:
    file.write(data)
print(type(data))

df = pd.read_csv("data.csv", sep=",")

#Print first 5rows
print(df.head())
print(type(df))

#Clean: Drop any rows with missing values
df_clean = df.dropna()

print(df_clean)

#Transform: filter people over age 30
df_over_30 = df_clean[df_clean["Age"] > 30]

print(df_over_30)

#Save the result to a new CSV file
df_over_30.to_csv("filtered_data.csv")

print("Filtered data saved to 'filtered_data.csv'.")
# Read the filtered data to verify
df_filtered = pd.read_csv("filtered_data.csv")      

print("Filtered Data:")
print(df_filtered)


