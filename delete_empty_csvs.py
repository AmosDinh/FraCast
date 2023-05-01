import pandas as pd
import os
# delete empty csvs in folder
def delete_empty_csvs(folder):
    for file in os.listdir(folder):
        if file.endswith(".csv"):
            df = pd.read_csv(folder + file)
            if df.empty:
                os.remove(folder + file)
                print("Deleted empty csv: " + file)

delete_empty_csvs("xetrworker2/")