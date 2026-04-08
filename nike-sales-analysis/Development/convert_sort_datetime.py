import pandas as pd
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')