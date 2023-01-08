# import pandas library
import pandas as pd

# create data structure in nested array
df = pd.DataFrame({
        "first_name": ["joe", "richard", "thomas"],
        "last_name": ["smock", "jones", "richards"],
        "gender": ["male", "non-binary", "male"],
})

# print entire data structure
print(df)

# access data in index 2 of first_name
x = df["first_name"][2]
print(x) # thomas

# access data under last_name and gender
y = df[["last_name", "gender"]]
print(y)

