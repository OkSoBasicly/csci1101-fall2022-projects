import pandas as pd
import matplotlib.pylab as plt

df = pd.read_csv("game-ratings-by-top-10-platforms.csv")

#group by metrics
df_follow = df.groupby(["platform_name"])["follow_count"].sum().reset_index()

df_follow = df_follow.rename(columns = {"follow_count": "total follows"})

df_hype = df.groupby(["platform_name"])["hype_count"].sum().reset_index()

df_hype = df_hype.rename(columns = {"hype_count": "total hype"})

#analyze data w visual
Bar_width = 0.4

plt.bar(df_follow.index - Bar_width/2, df_follow["total follows"], color = "blue", label ="number of follows",width=Bar_width)

plt.bar(df_hype.index + Bar_width/2, df_hype["total hype"], color = "red", label ="number of hypes",width=Bar_width)

plt.xticks(df_follow.index, df_follow["platform_name"])

plt.legend(loc = "upper left")

plt.show()
