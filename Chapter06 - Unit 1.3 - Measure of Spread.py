# DataCamp-Python - Chapter06 - Unit 1.3 - Measure of Spread


# Variance
np.var(df['col1'], ddof=1)

# Standard Deviation
np.std(df['col1'], ddof=1)

# Mean Average Distance (MAD)
dists = df['col1'] - df['col1'].agg(np.mean)
np.mean(np.abs(dists))

# Quantiles: Median = 0.5, or a list for multiple quantiles
np.quantiles(df['col1'], 0.5)
np.quantiles(df['col1'], [0, 0.25, 0.5, 0.75, 1])

# Boxplots
import matplotlib.pyplot as plt
plt.boxplot(df['col1'])
plt.show()

# Quantiles using np.linspace(start, stop, num)
np.quantile(df['col1'], [0, 0.2, 0.4, 0.6, 0.8, 1])
np.quantile(df['col1'], np.linspace(0,1,5))

# IQR (Interquartile Range)
IQR = np.quantile(df['col1'], 0.75) - np.quantile(df['col1'], 0.25)

from scipy import iqr
iqr(df['col1'])

# Finding Outliers
from scipy import iqr
iqr = iqr(df['col1'])
lower_threshold = np.quantile(df['col1'], 0.25) - (1.5 * iqr)
upper_threshold = np.quantile(df['col1'], 0.75) + (1.5 * iqr)

df[ (df['col1'] < lower_threshold) | (df['col1'] > upper_threshold) ]
