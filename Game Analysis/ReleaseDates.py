import pandas as pd
import matplotlib.pylab as plt

df = pd.read_csv("game-ratings-by-release-dates.csv")


df["first_release_date"] = pd.to_datetime(df["first_release_date"])


plt.scatter(df["first_release_date"], df["critic_rating_value"],color ="blue", label="critic ratings")
plt.scatter(df["first_release_date"], df["user_rating_value"], color = "red", label = "user rating")

plt.legend(loc = "upper left")

plt.show()
