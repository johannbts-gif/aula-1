import pandas as pd

df = pd.read_csv(
    r"C:\Users\Johann\Desktop\Nova pasta\ven\Pasta1.csv",
    encoding="latin1",
)
print(df.head())