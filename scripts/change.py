import pandas as pd


input_file = "MLR.txt"  
output_file = "MLR.csv"  

data = pd.read_csv(input_file, delimiter='|') # Delimeter


data.to_csv(output_file, index=False)

print(f"File successfully converted and saved as {output_file}")