import pandas as pd
import numpy as np

data_frame = pd.read_csv("/Python projects/test/DEC1.csv")

# Droping negative values
data_frame = data_frame.map(lambda x: np.nan if isinstance(x, (int, float)) and x < 0 else x)

# Droping duplicates
data_frame = data_frame.drop_duplicates()

# Droping empty columns
data_frame = data_frame.drop(columns=['Weight on Bit (kdaN)','Depth Hole TVD (m)'])

# Fill missing values with the mean 
columns = ['Total Depth (m)','Top Drive Torque (ft-lbs) (ft-lbs)','Top Drive RPM (rpm)','SPM Total (spm)','Pump Pressure (kPa)','Depth - Bit (m)','Flow In (m3/min)','Block Position (m)','Hookload (kdaN)']
data_frame[columns] = data_frame[columns].apply(lambda col: col.fillna(col.mean()))

print(data_frame)

data_frame.to_csv("/Python projects/test/Cleaned_DEC1.csv", index=False)


# Checking if there are any missing values
print("Missing values :\n",data_frame.isnull().sum())

# Counting negative values in each column
negative_counts = (data_frame.select_dtypes(include='number') < 0).sum()
print("Negative values :\n",negative_counts)

# Checking data types of each column
print("Data types :\n",data_frame.dtypes)
