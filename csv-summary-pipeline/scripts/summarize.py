import pandas as pd
from glob import glob

files = glob("data/*.csv")
with open("summary.txt", "w") as out:
    for file in files:
        df = pd.read_csv(file)
        out.write(f"{file}:\n")
        out.write(str(df.describe(include='all')))
        out.write("\n\n")
