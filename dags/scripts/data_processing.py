import pandas as pd
#import pandas as pd
import numpy as np

# Define the dimensions of the DataFrame (rows, columns)
num_rows = 5
num_cols = 3

# Create a NumPy array of random numbers with the specified dimensions
random_data = np.random.rand(num_rows, num_cols)

# Create a Pandas DataFrame using the random NumPy array
df=pd.DataFrame(random_data, columns=['A', 'B', 'C'])  # Replace column names as needed
df.to_csv('data/raw/dataset.csv', index=False)




