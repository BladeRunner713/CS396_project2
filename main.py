import pandas as pd

aapl = pd.read_csv("C:/Users/Leona/PycharmProjects/CS396_project2/data/AAPL.csv")
df = pd.DataFrame(aapl["Date"])
df["AAPL"] = aapl["Close/Last"].str[1:].astype(float) - aapl["Open"].str[1:].astype(float)

amd = pd.read_csv("C:/Users/Leona/PycharmProjects/CS396_project2/data/AMD.csv")
df["AMD"] = amd["Close/Last"].str[1:].astype(float) - amd["Open"].str[1:].astype(float)

amzn = pd.read_csv("C:/Users/Leona/PycharmProjects/CS396_project2/data/AMZN.csv")
df["AMZN"] = amzn["Close/Last"].str[1:].astype(float) - amzn["Open"].str[1:].astype(float)

csco = pd.read_csv("C:/Users/Leona/PycharmProjects/CS396_project2/data/CSCO.csv")
df["CSCO"] = csco["Close/Last"].str[1:].astype(float) - csco["Open"].str[1:].astype(float)

facebook = pd.read_csv("C:/Users/Leona/PycharmProjects/CS396_project2/data/FACEBOOK.csv")
df["FACEBOOK"] = facebook["Close/Last"].str[1:].astype(float) - facebook["Open"].str[1:].astype(float)

msft = pd.read_csv("C:/Users/Leona/PycharmProjects/CS396_project2/data/MSFT.csv")
df["MSFT"] = msft["Close/Last"].str[1:].astype(float) - msft["Open"].str[1:].astype(float)

qcom = pd.read_csv("C:/Users/Leona/PycharmProjects/CS396_project2/data/QCOM.csv")
df["QCOM"] = qcom["Close/Last"].str[1:].astype(float) - qcom["Open"].str[1:].astype(float)

sbux = pd.read_csv("C:/Users/Leona/PycharmProjects/CS396_project2/data/SBUX.csv")
df["SBUX"] = sbux["Close/Last"].str[1:].astype(float) - sbux["Open"].str[1:].astype(float)

tsla = pd.read_csv("C:/Users/Leona/PycharmProjects/CS396_project2/data/TSLA.csv")
df["TSLA"] = tsla["Close/Last"].str[1:].astype(float) - tsla["Open"].str[1:].astype(float)

znga = pd.read_csv("C:/Users/Leona/PycharmProjects/CS396_project2/data/ZNGA.csv")
df["ZNGA"] = znga["Close/Last"].str[1:].astype(float) - znga["Open"].str[1:].astype(float)

print(df)
