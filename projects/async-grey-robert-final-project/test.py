import pandas as pd
import os
import matplotlib.pyplot as plt

# Update the path to point directly to the cases.csv file
data_path = os.path.join(os.getcwd(), 'data', 'cases.csv')

# Load the CSV file into a DataFrame
df = pd.read_csv(data_path)

# Count the occurrences of each crime type
crime_counts = df['CRIMETYPE'].value_counts()

# Display the most common crime types
print(crime_counts.head(20))
