import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

# Set chart title and labels for axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

# Set the size of tick labels.
ax.tick_params(labelsize=14)

plt.show()
