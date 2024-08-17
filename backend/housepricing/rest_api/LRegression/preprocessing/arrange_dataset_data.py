import pandas as pd
  
file_path = "/Users/duartemiranda/Desktop/side_projects/house_pricing/backend/housepricing/rest_api/LRegression/datasets/"
filename = "Housing.csv"
new_df_name = "Cleaned_Housing.csv"

df = pd.read_csv(file_path+filename)
print("[%]Pre-processing Dataset...")
# Convert bool values to int
# Since the values are yes/no we can search for every value that equals yes, this will return True.
# So we can just assume all the other values are false
cols_to_convert = ["mainroad", "guestroom", "basement", "hotwaterheating", "airconditioning", "prefarea"]
for col in cols_to_convert:
  df[col] = (df[col] == 'yes').astype(int)

#Convert furnished series
furnished_col = "furnishingstatus"
df[furnished_col] = df[furnished_col].apply(lambda x: 0 if x == 'unfurnished' else 1 if x == 'semi-furnished' else 2)
print("[+]Dataset processed[+]")

#Update Dataset
df.to_csv(file_path+new_df_name, index=False)
print(f"[+]New Dataset Created[+]\n\nName: {new_df_name}")