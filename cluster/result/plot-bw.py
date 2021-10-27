import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('./data.csv')
markers = ['X', 'D', 'o', 'x']

'''
lpc = data[data["type"]=="LP"]
rndc = data[data["type"]=="Random"]

print(np.percentile(lpc["hamming distance"], 90))
print(np.percentile(rndc["hamming distance"], 90))
'''



data["hamming distance"] = data["hamming distance"] / 10

fig, ax = plt.subplots(1, 1, figsize=(4,2))

variance = sns.lineplot(data=data, x="centralized percentage", y="hamming distance", hue="type", palette="colorblind", ax=ax)
for i, line in enumerate(ax.get_lines()):
  if i >= len(markers):
    break
  line.set_marker(markers[i])

# ax.set_ylabel("load variance")
ax.yaxis.set_ticks(np.arange(10, 80, 20))
ax.set_ylabel("Extra MCast Target(%)", fontsize=8)
ax.set_xlabel("Imbalanced Query Flow Space Percentage(%)", fontsize=8)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

legend = plt.legend(prop={'size': 6}, frameon=False, labels=["K-means Clustering", "Random Clustering"])

# Finalize the plot
# sns.despine(bottom=True)
# plt.setp(f.axes, yticks=[])
plt.tight_layout()

fig.savefig("cluster-centralized-v2.png")
# rounds_plot.savefig("./rounds_plot.png")

