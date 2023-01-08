# import pandas library
import pandas as pd

# create data structure in nested array
df = pd.DataFrame({
        "first_name": ["joe", "richard", "thomas"],
        "last_name": ["smock", "jones", "richards"],
        "gender": ["male", "non-binary", "male"],
})

# loc method implemented to access columns names or labels
x = df.loc[1, "gender"]
print(x) # print non-binary

# replace value of jones with julius
y = df["first_name", "last_name", "gender"]
print(y)