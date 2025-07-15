###Data Exploration###
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("movies_dataset.csv")

print("first 5 rows:\n",df.head())
print("\n show the shape:\n",df.shape)
print("\n Descriptive statistics:\n",df.describe())
print("\n missing columns:\n",df.isnull().sum())

###Data Filtering and Selection###
print("movies released after 2010:\n", df[df['release year'] > 2010][['title' , 'release year']])
print("\nMovies with a rating higher than 8.0:\n", df[df['rating'] > 8.0][['title' , 'rating']])
print("\nMovies in genre Action or Comedy:\n" , df[df['genre'].isin(['Action' , 'Comedy'])][['title' , 'genre']])
print("\nMovies with box office greater than twice the budget:\n",df[df['box Office'] > 2*df['budget']][['title' , 'budget' ,'box Office' ]])
print("\ndirected by Christopher Nolan:\n" ,df[df['director'].isin(['Christopher Nolan'])][['title' , 'director']])

###Data Transformation###
#Add Profit column 
df['profit'] = df['box Office']-df['budget']
print("Profit column added:\n",df[['title' ,'budget', 'box Office', 'profit']])

#ROI (Return on Investment)
df['ROI'] = (df['box Office'] - df['budget']) / df['budget']
print("\nROI (Return on Investment):\n",df[['title' , 'budget', 'box Office' , 'ROI']])

#Length column (Short, Medium, Long)
def length(runtime):
    if runtime < 90:
        return 'short'
    elif runtime <= 120:
        return 'medium'
    else: 
        return 'long'
df['Length'] = df['runtime'].apply(length)
print("\nMovie length classified:\n",df[['title' , 'runtime' , 'Length']])

#Decade column
df['decade'] = (df['release year'] // 10 * 10).astype(str) + "s"
print("\nDecade column:\n",df[['title' , 'release year' , 'decade']])

#Rating Category (Poor, Average, Excellent)
def rate_category(rating):
    if rating < 4:
        return 'Poor'
    elif rating <= 7:
        return 'Average'
    else:
        return 'Excellent'
df['rate_category'] = df['rating'].apply(rate_category)
print("\nRating Category\n",df[['title' , 'rating' , 'rate_category']])

###Aggregation and Grouping###
avg_rating = df.groupby('genre')['rating'].mean()
print("\nAverage rating for each genre:\n", avg_rating)

highest_grossing = df.sort_values('box Office', ascending=False).groupby('director').first()
print("\nHighest-grossing movie by director:\n", highest_grossing[['title', 'box Office']])

avg_by_decade = df.groupby('decade')[['budget', 'box Office']].mean()
print("\nAverage budget and box office by decade:\n", avg_by_decade)

country_stats = df.groupby('country').agg({'rating': 'mean','budget': 'sum','box Office': 'sum'})
print("\nCountry-wise stats (average rating, total budget, total box office):\n", country_stats)

df['profitable'] = df['ROI'] > 1
profitable_percent = df.groupby('genre')['profitable'].mean() * 100
print("\n % of profitable movies (ROI > 1) by genre:\n", profitable_percent)

###Data Visualization###
#Group by genre and calculate average rating
avg_rating = df.groupby('genre')['rating'].mean().sort_values(ascending=False).reset_index()
plt.figure(figsize=(8, 5))
sns.barplot(
    data=avg_rating,
    x='genre',
    y='rating',
    hue='genre',
    palette='mako')
plt.title("Average Rating by Genre")
plt.xlabel("Genre")
plt.ylabel("Average Rating")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Scatter Plot– Budget vs Box Office
plt.figure(figsize=(8, 6))

sns.scatterplot(
    data=df,
    x='budget',
    y='box Office',
    hue='rating',          
    palette='coolwarm',     
    size='rating',          
    sizes=(20, 200),        
    legend=True)             
plt.title("Budget vs Box Office (colored by Rating)")
plt.xlabel("Budget")
plt.ylabel("Box Office")
plt.tight_layout()
plt.show()

#Histogram – Movie Runtime Distribution 
plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x='runtime',
    bins=10,           
    color='skyblue')
plt.title("Distribution of Movie Runtimes")
plt.xlabel("Runtime")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.show()

#Box Plot showing ROI by Genre 
plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df,
    x='genre',
    y='ROI',
     hue='genre',
    palette="Set2")
plt.title("Distribution of ROI by Genre")
plt.xlabel("Genre")
plt.ylabel("Return on Investment (ROI)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Line Plot – Budget & Box Office Trend by Year 
plt.figure(figsize=(10, 6))
yearly_stats = df.groupby('release year')[['budget', 'box Office']].mean().reset_index()

sns.lineplot(
    data=yearly_stats,
    x='release year',
    y='budget',
    label='Average Budget',
    marker='o')
sns.lineplot(
    data=yearly_stats,
    x='release year',
    y='box Office',
    label='Average Box Office',
    marker='o')
plt.title("Trend of Average Budget and Box Office by Year")
plt.xlabel("Release Year")
plt.ylabel("Average Amount")
plt.legend()
plt.tight_layout()
plt.show()
