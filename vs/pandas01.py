import pandas as pd
import datetime
rsr = [[datetime.date(2021, 1, 1), 1, 30],
          [datetime.date(2021, 1, 1), 2, 20],
          [datetime.date(2021, 1, 1), 1, 50],
          [datetime.date(2021, 1, 1), 2, 45],
          [datetime.date(2021, 1, 1), 1, 20],
          [datetime.date(2021, 1, 1), 2, 15],
          [datetime.date(2021, 1, 2), 1, 29],
          [datetime.date(2021, 1, 2), 2, 29],
          [datetime.date(2021, 1, 2), 1, 29],
          [datetime.date(2021, 1, 2), 2, 29],
          [datetime.date(2021, 1, 2), 1, 0],
          [datetime.date(2021, 1, 2), 2, 12],
          [datetime.date(2021, 1, 3), 1, 17],
          [datetime.date(2021, 1, 3), 2, 17],
          [datetime.date(2021, 1, 3), 1, 17],
          [datetime.date(2021, 1, 3), 2, 22],
          [datetime.date(2021, 1, 3), 1, 0],
          [datetime.date(2021, 1, 3), 2, 0]
]

df = pd.DataFrame(rsr, columns=['fecha', 'item', 'cantidad'])
print(df)
df = df.loc[df['item'] == 1]
df = df.groupby(['fecha', 'item']).sum()
print(df)
print(df['cantidad'].to_list())
