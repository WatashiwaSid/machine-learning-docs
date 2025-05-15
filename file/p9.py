import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("30students.csv")

#count total number of missing values
print("Missing Values Count Before Replacement: \n", df.isna().sum())

#Fill missing values with mean marks
df['Maths'] = df['Maths'].fillna(df['Maths'].mean())
df['Science'] = df['Science'].fillna(df['Science'].mean())
df['English'] = df['English'].fillna(df['English'].mean())

#count total number of missing values
print("\nMissing Values Count After Replacement: \n", df.isna().sum())

#Create two distinct data frames for girls and boys
males = df[df['Gender'] == 'Male'].iloc[:, 0:2]
females = df[df['Gender'] == 'Female'].iloc[:, 0:2]
print("\nBoys: \n", males[:3])
print("\nGirls: \n", females[:3])

df['Percentage'] = df[['Maths', 'Science', 'English']].mean(axis=1)
print("\nPercentage: \n", df.head(3))

#normalize marks between 0 and 1
df['mn'] = df['Maths'] / 100
df['sn'] = df['Science'] / 100
df['en'] = df['English'] / 100
print("\nNormalized Marks: \n", df.head(3))

#plot bar graph
genders = df['Gender'].value_counts()
plt.figure(figsize=(6, 4))
plt.subplot(1,2,1)
genders.plot(kind='bar')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Number of Students')

## add percentage category for pie chart
def categorize(p):
    if p >= 60:
        return '>=60'
    elif p >= 50:
        return '50-59'
    else:
        return '<50'

df['Category'] = df['Percentage'].apply(categorize)
categories = df['Category'].value_counts()

#plot pie chart
plt.subplot(1,2,2)
plt.title("Percentage Distribution")
categories.plot(kind='pie', colors=['red','blue','yellow'])
plt.show()
