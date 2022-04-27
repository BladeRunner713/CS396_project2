import pandas as pd
import numpy as np

path = "C:/Users/gaolingxiao/Desktop/CS396_project2/data/"
aapl = pd.read_csv(path + "AAPL.csv")
df = pd.DataFrame(aapl["Date"])
df["AAPL"] = aapl["Close/Last"].str[1:].astype(float) / aapl["Open"].str[1:].astype(float)

amd = pd.read_csv(path + "AMD.csv")
df["AMD"] = amd["Close/Last"].str[1:].astype(float) / amd["Open"].str[1:].astype(float)

amzn = pd.read_csv(path + "AMZN.csv")
df["AMZN"] = amzn["Close/Last"].str[1:].astype(float) / amzn["Open"].str[1:].astype(float)

csco = pd.read_csv(path + "CSCO.csv")
df["CSCO"] = csco["Close/Last"].str[1:].astype(float) / csco["Open"].str[1:].astype(float)

facebook = pd.read_csv(path + "FACEBOOK.csv")
df["FACEBOOK"] = facebook["Close/Last"].str[1:].astype(float) / facebook["Open"].str[1:].astype(float)

msft = pd.read_csv(path + "MSFT.csv")
df["MSFT"] = msft["Close/Last"].str[1:].astype(float) / msft["Open"].str[1:].astype(float)

qcom = pd.read_csv(path + "QCOM.csv")
df["QCOM"] = qcom["Close/Last"].str[1:].astype(float) / qcom["Open"].str[1:].astype(float)

sbux = pd.read_csv(path + "SBUX.csv")
df["SBUX"] = sbux["Close/Last"].str[1:].astype(float) / sbux["Open"].str[1:].astype(float)

tsla = pd.read_csv(path + "TSLA.csv")
df["TSLA"] = tsla["Close/Last"].str[1:].astype(float) / tsla["Open"].str[1:].astype(float)

znga = pd.read_csv(path + "ZNGA.csv")
df["ZNGA"] = znga["Close/Last"].str[1:].astype(float) / znga["Open"].str[1:].astype(float)

# Total 253 trading days in one year
df = df[::-1].reset_index(drop=True)
print(df)

# Theoretical optimal learning rate 𝜀 = √(ln k / n)
k = 10
n = 253
epsilon = (np.log(10) / 253) ** 0.5
print(epsilon)
values = [0] * 10
p = [0] * 10
total_payoff = 0
for index, row in df.iterrows():
    if index == 0:
        # First day, random choose a stock
        total_payoff += np.random.choice(row[1:])
    else:
        # Choose stock based on probability
        h = max(row[1:])
        sum_value = 0
        for i in range(10):
            sum_value += (1 + epsilon) ** (values[i] / h)
        for i in range(10):
            # Calculate the probability
            p[i] = (1 + epsilon) ** (values[i] / h) / sum_value
        # Select a stock, sum the total payoff
        total_payoff += np.random.choice(row[1:], p=p)
    values = np.add(values, row[1:].values.tolist())
print("Using theoretical optimal learning rate, the total payoff is", total_payoff)
print(values)
