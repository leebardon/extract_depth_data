import xarray as xr
import pandas as pd
import sys
import os

nc_filename = os.environ["nc_filename"]
month = sys.argv[1]
depth = int(os.environ["depth"])
out_filename = "month{}.csv".format(month)
depth = depth-1
root = os.environ["root"]

ds = xr.open_dataset(f'{nc_filename}')
df = ds.to_dataframe()

def get_depth(data, month, depth):
    surface = []
    for i in range(0, 2200):
        if df.iloc[i].name[3] == depth:
            df["X"] = df.iloc[i].name[1]
            df["Y"] = df.iloc[i].name[2]
            df["Z"] = depth+1
            df["Month"] = month
            surface.append(df.iloc[i])

    surface = pd.DataFrame(surface, columns=df.columns)
    surface.to_csv(f'{root}/{out_filename}', index=False)
    print("------------------------- FILE COMPLETED -------------------------- ")

get_depth(df, month, depth)
