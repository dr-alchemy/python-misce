import pandas as pd

filenames = ['101.csv', '102.csv', '103.csv']

combined_csv = pd.concat( [ pd.read_csv(f) for f in filenames ] )

# And if you want to export it to a single csv file, use this:
combined_csv.to_csv( "combined_csv.csv", index=False )