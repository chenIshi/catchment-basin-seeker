import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('./emulated_result.csv')

'''
snmp = data[data["type"]=="SNMP"]
worst = data[data["type"]=="Worst-MonAggr"]

print(np.percentile(snmp["pkt_num"], 90))
print(np.percentile(worst["pkt_num"], 90))
'''


f, ax = plt.subplots(figsize=(6,3))
# fig0,ax0=plt.subplots(figsize=(6,3))

plot = sns.ecdfplot(data, x="pkt_num", hue="type", color=["royalblue", "maroon", "seagreen"], linewidth=2, ax=ax)

ax.set_xlabel("Response Traffic Volume (No. of Packets)", fontsize=12)
ax.set_ylabel("CDF", fontsize=12)
ax.legend(handles=ax.lines, labels=["MonAggr(No Clustering)","MonAggr(One Clustering)","SNMP"], frameon=False, loc="lower right", prop={'size': 10})

ax.set_ylim(0.4,1)
ax.set_xlim(0,800)


# plt.axvline(x=125, color="grey", linestyle='--', linewidth=1.2)

# plot.lines[1].set_linestyle("-.")
plot.lines[1].set_linestyle("--")
plot.lines[2].set_linestyle("-.")
# plot1.lines[2].set_linestyle("--")
plt.tick_params(labelsize=10)

plt.tight_layout(w_pad=0.3, h_pad=0.3)
f.savefig("./large-scale-emulation.png")

