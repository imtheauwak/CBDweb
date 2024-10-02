import pandas as pd

path = 'C:\\CBD\\symptoms.csv'
data = pd.read_csv(path, encoding='utf-8')

output_dict = {}

for i, v in enumerate(data.columns): 
    output_dict[f"id_{i}"] = 0

print(output_dict)
