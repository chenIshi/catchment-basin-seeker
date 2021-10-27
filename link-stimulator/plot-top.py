import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('./emulated_result.csv')

f, ax = plt.subplots(figsize=(6,3))
# fig0,ax0=plt.subplots(figsize=(6,3))

plot = sns.ecdfplot(data, x="pkt_num", hue="type", color=["royalblue", "maroon", "seagreen"], linewidth=2, ax=ax)

ax.set_xlabel("Response Traffic Volume (No. of Packets)", fontsize=12)
ax.set_ylabel("CDF", fontsize=12)
ax.legend(handles=ax.lines, labels=["MonAggr(No Clustering)","MonAggr(One Clustering)","SNMP"], frameon=False, loc="lower right", prop={'size': 10})
'''
axs[1].set_xlabel("One-directional link usage")
axs[1].set_ylabel("")
axs[2].set_xlabel("")
axs[2].set_ylabel("")
'''
ax.set_ylim(0.95,1)
ax.set_xlim(0,800)

'''
arr1 = plt.arrow(x=1.0, y=1.0, dx=0.2, dy=0.5)
ax.add_patch(arr1)
'''
# plt.axvline(x=125, color="grey", linestyle='--', linewidth=1.2)

# plot.lines[1].set_linestyle("-.")
plot.lines[1].set_linestyle("--")
plot.lines[2].set_linestyle("-.")
# plot1.lines[2].set_linestyle("--")
plt.tick_params(labelsize=10)

plt.tight_layout(w_pad=0.3, h_pad=0.3)
f.savefig("./large-scale-emulation-top.png")
