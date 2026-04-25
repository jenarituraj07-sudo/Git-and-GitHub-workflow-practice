import pandas as pd
import matplotlib.pyplot as plt

# data for graph
batman_stats = pd.DataFrame({
    "name": ["Abhishek sharma", "Sanju samson", "Virat kohli", "Shubman gill", "Heinrich klaasen"],
    "runs": [323, 293, 328, 297, 320]
})

# sort data
sorted_data = batman_stats.sort_values(by=("runs"), ascending= True)

# graph size and title
plt.figure(figsize=(18, 8))
plt.title("Orange cap ranking", fontsize = 16, fontweight="bold")

# find highest and lowest value
maximum_run = sorted_data["runs"].max()
minimum_run = sorted_data["runs"].min()

# show different color on bar graph
colors = ["Red" if col == maximum_run else
          "black" if col == minimum_run else
          "blue"
          for col in sorted_data["runs"]]

# show data on graph
bars = plt.bar(sorted_data["name"], sorted_data["runs"], color=colors, edgecolor= "black")

#show runs on each bars
plt.bar_label(bars, fontsize= 14)

# add grid on y label
plt.grid(axis="y", alpha= 0.7, linewidth= 0.8, linestyle= "--")

# show graph
plt.show()
