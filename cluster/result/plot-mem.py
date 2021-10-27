import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('./control-entry-usage.csv')
'''
woc = data[data["type"]=="W/O Cluster"]
wic = data[data["type"]=="W/I Cluster"]

print(np.percentile(woc["pkt_num"], 90))
print(np.percentile(wic["pkt_num"], 90))
'''
f, ax = plt.subplots(figsize=(6,3))
# fig0,ax0=plt.subplots(figsize=(6,3))

plot = sns.ecdfplot(data, x="pkt_num", hue="type", color=["royalblue", "maroon", "seagreen"], linewidth=2, ax=ax)

ax.set_xlabel("Number of Forwarding Rules", fontsize=12)
ax.set_ylabel("CDF", fontsize=12)
ax.legend(handles=ax.lines, labels=["W/O Cluster","W/I Cluster"], frameon=False, loc="lower right", prop={'size': 10})

ax.set_ylim(0.4,1)
ax.set_xlim(0,2000)



# plt.axvline(x=125, color="grey", linestyle='--', linewidth=1.2)

# plot.lines[1].set_linestyle("-.")
plot.lines[0].set_linestyle("--")
# plot.lines[2].set_linestyle("-.")
# plot1.lines[2].set_linestyle("--")
plt.tick_params(labelsize=10)

plt.tight_layout(w_pad=0.3, h_pad=0.3)
f.savefig("./table-entries.png")

