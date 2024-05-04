# %%


import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('/Users/jubacochran/Downloads/assignment_5_1_starter/data/coupons.csv')


#Filling in the values that were missing with "unknown" This is so I can plot and analize data better. I didn't wan to drop nulls
df['CarryAway'].fillna('Unknown', inplace=True)  # Assuming 'Unknown' as a placeholder for missing
df['car'].fillna('Unknown', inplace=True)
df['Bar'].fillna('Unknown', inplace=True)
df['CoffeeHouse'].fillna('Unknown', inplace=True)
df['RestaurantLessThan20'].fillna('Unknown', inplace=True)
df['Restaurant20To50'].fillna('Unknown', inplace=True)


#adding ordinal categories for some of the user attributes. This will help with plots and stat analysis with the whole picture in mind

category_mapping = {
    '0': 0,
    'less than 1': 1,
    '1 to 3': 2,
    '4 to 8': 3,
    'greater than 8': 4,
    'never': -1,
    'Unknown': -2
}

age_category_mapping = {
    'below 21': 0,
    '21 to 25': 1,
    '26 to 30': 2,
    '50plus': 3
}

# adding ordinal for age column
df['AgeOrdinal'] = df['age'].map(age_category_mapping)

# Handling missing values by assigning a -2 this is to keep the logic in line with all mappings
df['AgeOrdinal'].fillna(-2, inplace=True)


# Apply the mapping to Bar, Car, Coffee House and creating new columns. Row order will persist. 
df['BarOrdinal'] = df['Bar'].map(category_mapping)
df['BarOrdinal'].fillna(-2, inplace=True)

df['CarryAwayOrdinal'] = df['CarryAway'].map(category_mapping)
df['CarryAwayOrdinal'].fillna(-2, inplace=True)

df['CoffeeHouseOrdinal'] = df['CoffeeHouse'].map(category_mapping)
df['CoffeeHouseOrdinal'].fillna(-2, inplace=True)

df['CarOrdinal'] = df['car'].map(category_mapping)
df['CarOrdinal'].fillna(-2, inplace=True)

df['RestaurantLessThan20_Ordinal'] = df['RestaurantLessThan20'].map(category_mapping)
df['RestaurantLessThan20_Ordinal'].fillna(-2, inplace=True)

df['Restaurant20To50_Ordinal'] = df['Restaurant20To50'].map(category_mapping)
df['Restaurant20To50_Ordinal'].fillna(-2, inplace=True)

#print(df.info())

#Those that said yes

yes_population = df.query("Y == 1")
#print(yes_population)


##Those that said no
no_population = df.query("Y == 0")
#print(no_population)

#Keep this Juba
#Getting a count of yes and no according the restarauntless than $20
#sns.countplot(data=df, x="RestaurantLessThan20", hue=df['Y'].astype(str))
#sns.set_style('whitegrid')

#Keep this Juba
#Getting a plt that filters based on the highest yes group from above and plotting cout according to passanager category
#sns.countplot(data=df.query("RestaurantLessThan20 == '1~3'"), x="passanger", hue=df['Y'].astype(str))
#fig = px.scatter(df.query("age == 21 and Y == 1"), x='income', y='direction_opp')
#fig


yes_no_counts = df['Y'].value_counts()

# Calculate the percentage
yes_no_percentage = yes_no_counts / yes_no_counts.sum() * 100

#print(yes_no_percentage)

categories = df.groupby('coupon')['Y'].value_counts
#print(categories)

#using groupby method to create sub's of coupon and perform cal and to returen proportions
catagoryies_of_coupons = df.groupby('coupon')['Y'].value_counts(normalize=True).unstack() * 100
#print(catagoryies_of_coupons)
'''
#Using a style for polish
plt.style.use('ggplot')
catagoryies_of_coupons.plot(kind='bar', stacked=True, color=['Red', 'Gold'], figsize=(10, 7))

plt.title('Coupon Categoy Proportions of Yes and No')
plt.xlabel('Coupon Categories')
plt.ylabel('Percentage')
plt.legend(title='Response', labels=['No', 'Yes'])

plt.show()
'''
plt.hist(df['temperature'], edgecolor='black', alpha=0.5)
plt.title('Temperature Distribution')
plt.xlabel('Temperature')
plt.ylabel('Count')
plt.grid(True)
#plt.show()

#Try transformation
#['never' 'less1' '1~3' 'gt8' 'Unknown' '4~8']

print(df['temperature'].isnull().value_counts())
print(df['temperature'].describe())
print(df.columns)
print(df[['coupon']])
bar_coupons = df[df['coupon']=='Bar']
#print(bar_coupons)
#print(type(bar_coupons))
#print(bar_coupons.iloc[3: , :-9])
went_to_bar_3_or_less = bar_coupons.query("Bar == '1~3' or Bar == 'less1' ")
print(went_to_bar_3_or_less.iloc[3:, :-9].reset_index())
print(bar_coupons['Bar'].unique())
went_to_bar_4_or_more = bar_coupons.query("Bar == '4~8' or Bar == 'gt8' ")
print(went_to_bar_4_or_more)
#number_of_yes_bar = ratio_of1_t0_3.query("Y == 0").sum()
#print(number_of_yes_bar)

# Calculate the acceptance rate for those who went to a bar 3 or fewer times
yes_count_3_or_less = went_to_bar_3_or_less['Y'].sum()
total_responses_3_or_less = went_to_bar_3_or_less['Y'].count()
print(total_responses_3_or_less)
acceptance_rate_3_or_less = yes_count_3_or_less / total_responses_3_or_less

# Calculate the acceptance rate for those who went to a bar 4 or more times
yes_count_4_or_more = went_to_bar_4_or_more['Y'].sum()
total_responses_4_or_more = went_to_bar_4_or_more['Y'].count()
print(total_responses_4_or_more)
acceptance_rate_4_or_more = yes_count_4_or_more / total_responses_4_or_more

# Print the results
print(f"Acceptance Rate for 3 or fewer times: {acceptance_rate_3_or_less:.2f}")
print(f"Acceptance Rate for 4 or more times: {acceptance_rate_4_or_more:.2f}")