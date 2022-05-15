import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import codecademylib3

# load in the data
df = pd.read_csv("mushroom_data.csv")
print(df.head())

# list of all column headers
columns = df.columns.tolist()


# plot the data using for loop for each column

for column in columns:
  print(column)

  sns.countplot(df[column].value_counts(ascending=True).index, palette = "Set3")

  # avoids overlaping of labels
  plt.xticks(rotation=30, fontsize=10)
  plt.xlabel(column, fontsize=12)

  plt.title(column + " Value Counts")

  plt.show()
  plt.clf()
  








