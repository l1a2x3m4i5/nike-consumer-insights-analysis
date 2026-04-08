df['Change'] = df['Close'] - df['Open']
print(df[['Date', 'Change']].head())