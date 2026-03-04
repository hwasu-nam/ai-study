import pandas as pd

data = {
    "name" : ["apple","banana","orange"],
    "price" : [1000, 2000, 1500]
}

df = pd.DataFrame(data)

print(df)