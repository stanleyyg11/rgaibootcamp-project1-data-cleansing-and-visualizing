import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Initiate Dataset
url = 'https://storage.googleapis.com/rg-ai-bootcamp/assignment-1/fifa21_raw_data.csv'
fifa_df = pd.read_csv(url, low_memory=False)
fifa_df

# Data Cleansing
fifa_df2 = fifa_df.drop("Unnamed: 0", axis='columns')
fifa_df2['Club'] = fifa_df2['Club'].map(lambda x : x.replace('\n', ''))
fifa_df2[['W/F', 'SM', 'IR']] = fifa_df2[['W/F', 'SM', 'IR']].apply(lambda x : x.str.replace('★', ''))
fifa_df2 = fifa_df2.fillna({'Loan Date End': 'Not on Loan', 'Hits': 'Unknown'})
fifa_df2[['Value', 'Wage', 'Release Clause']] = fifa_df2[['Value', 'Wage', 'Release Clause']].replace({'€': '', 'K': '*1e3', 'M': '*1e6'}, regex=True).map(pd.eval).astype(np.int64)

#====================================================================================================================================================
# Data Visualization (Only uncomment when used)

# Pie Chart
kaki = fifa_df2['Preferred Foot'].value_counts()

category = kaki.index
totalCategory = kaki.values
labelTotalCategory = ['Kaki kiri', 'Kaki kanan']

plt.pie(totalCategory, labels=labelTotalCategory)
plt.title("Fifa Data Player's Preferred Foot")
plt.show()

# Bar Plot Visualization of FIFA 21 Players' Preferred Foot 

# Bar Plot Visualization of Top 6 FIFA 21 Players

# Bar Plot Visualization of Top 8 FIFA Teams with most numbers of Best Players

# Bar Plot Visualization of Top 10 FIFA Teams with the most players in Top 100 Valuable Players

# Scatter Plot for Underpaid but Valuable Players
x = fifa_df2['Value']
y = fifa_df2['Wage']

plt.scatter(x, y, label='All Player')


highValueThres = fifa_df2['Value'].quantile(0.75)
lowWageThres = fifa_df2['Wage'].quantile(0.25)

highValueUnderpaid = fifa_df2[(fifa_df2['Value'] >= highValueThres) & (fifa_df4['Wage'] <= lowWageThres)]

x1 = highValueUnderpaid['Value']
y1 = highValueUnderpaid['Wage']

plt.scatter(x1,y1, label='High Value Underpaid Player')

plt.legend()
plt.ylabel("Player's Value")
plt.xlabel("Player's Wage")
plt.show()