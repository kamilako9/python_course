import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn.utils
# seaborn.utils.set_hls_values(verify = False)
# import requests
# requests.packages.urllib.disable_warnings()


# #
# df = pd.DataFrame({'category': ['a', 'b', 'a', 'b'],
#                   'reiksme': [1, 2, 3, 4]})

#juostine diagrama
# sns.barplot(data = df, x = 'category', y = 'reiksme')
# plt.show()

#linijine diagrama
# sns.lineplot(data = df, x = 'category', y = 'reiksme')
# plt.show()

#stulpeline diagrama
# sns.countplot(data = df, x = 'category')
# plt.show()

#juostine diagrama
# sns.boxplot(data = df, x = 'category', y = 'reiksme')
# plt.show()

#diaugialype diagrama
# sns.pairplot(df)
# plt.show()

#regresijos modelis
# df = pd.DataFrame({'category': [2, 4, 6, 8],
#                   'reiksme': [1, 2, 3, 4]})
# sns.lmplot(data = df, x = 'category', y = 'reiksme')
# plt.show()
#
# silumine diagrama (pvz. temperaturoms)
# df2 = np.random.rand(5, 5)
# sns.heatmap(df2, annot = True, cmap = 'coolwarm')
# plt.show()
# # #
# data = sns.load_dataset('tips')
# sns.histplot(data = data, x = 'total_bill', kde = True)
# columns = data.columns
# print(columns)
# plt.show()
# #
# data2 = sns.load_dataset('car_crashes')
# plt.show()
# vid_avariju_sk = data2['total'].mean()
# print(vid_avariju_sk)
# plt.figure(figsize = (8,6))
# sns.boxplot(data2, x = 'total')
# plt.show()

# sns.pairplot(data = data3, hue = 'id')


