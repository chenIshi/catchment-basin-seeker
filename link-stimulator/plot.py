import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('./emulated_result.csv')

f, ax = plt.subplots()
# fig0,ax0=plt.subplots(figsize=(6,3))

plot = sns.ecdfplot(data, x="pkt_num", hue="type", color=["royalblue", "maroon", "seagreen"], ax=ax)
'''
plot1 = sns.ecdfplot(data_e3, x="Pkt Count", hue="Type", color=["royalblue", "maroon"], ax=axs[1])
plot2 = sns.ecdfplot(data_e4, x="Pkt Count", hue="Type", color=["royalblue", "maroon"], ax=axs[2])
axs[0].legend(handles=axs[0].lines, labels=["SNMP","MonAggr"], frameon=False, loc="lower right")
axs[1].legend(handles=axs[1].lines, labels=["SNMP","MonAggr"], frameon=False, loc="lower right")
axs[2].legend(handles=axs[2].lines, labels=["SNMP","MonAggr"], frameon=False, loc="lower right")
'''

ax.set_xlabel("Bidirectional link usage")
ax.set_ylabel("Cumulative Proportion")
'''
axs[1].set_xlabel("One-directional link usage")
axs[1].set_ylabel("")
axs[2].set_xlabel("")
axs[2].set_ylabel("")
'''

# plot.lines[1].set_linestyle("-.")
plot.lines[1].set_linestyle("--")
plot.lines[2].set_linestyle("-.")
# plot1.lines[2].set_linestyle("--")
plt.tick_params(labelsize=10)

plt.tight_layout(w_pad=0.3, h_pad=0.3)
f.savefig("./result.png")
