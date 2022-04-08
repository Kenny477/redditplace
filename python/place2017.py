import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_parquet('data/place2017.parquet')
print(df)

# Get list of timestamps for each user
user_time = df.drop(['x_coordinate', 'y_coordinate', 'color'], axis=1)
user_time = user_time.groupby(['user_hash'])['ts'].apply(np.array)
user_time = user_time.to_frame(name="ts")
print(user_time)

# Add counter to each user
user_time['count'] = user_time['ts'].apply(lambda x: len(x))

plt.hist(user_time['count'], bins=100, density=True)
plt.savefig('place2017_hist.png')

# Find users in the top 10%
user_time_sorted = user_time.sort_values(by='count', ascending=False)
user_time_sorted = user_time_sorted.reset_index()
user_time_sorted = user_time_sorted.head(int(user_time_sorted.shape[0]*0.1))
print(user_time_sorted)