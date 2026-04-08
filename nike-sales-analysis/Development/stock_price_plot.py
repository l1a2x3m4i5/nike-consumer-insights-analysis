import matplotlib.pyplot as plt

plt.plot(df['Date'], df['Close'])
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.title("Nike Stock Price Over Time")
plt.show()