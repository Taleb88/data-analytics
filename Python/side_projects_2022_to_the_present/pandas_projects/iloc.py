# import pandas library
import pandas as pd

# create data structure in nested array
df = pd.DataFrame({
        "first_name": ["joe", "richard", "thomas"],
        "last_name": ["smock", "jones", "richards"],
        "gender": ["male", "non-binary", "male"],
})

# iloc method to access row by indexing a dataframe through integer position-based indexing
x = df.iloc[1]
print(x) # print out data of richard

# iloc method used to access row and column
y = df.iloc[2,2]
print(y) # print out male