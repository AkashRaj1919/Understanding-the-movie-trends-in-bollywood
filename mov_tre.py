import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Bollywood Movie Data
data = {
    
    'movie_title': ['Pushpa 2', 'Jawan', 'Stree 2 C', 'Animal', 'Pathaan', 
                    'Gadar 2', 'Bahubali 2', 'Kabir Singh', 'RRR', 'Sultan'],
                    
    'genre': ['Action ', 'Thriller', 'Comedy Horror', 'Drama', 'Action', 
              'Action', 'Action', 'Romance', 'Drama', 'Romance'],
              
              
    'release_year': [2024, 2023, 2024, 2023, 2023, 
                     2023, 2017, 2019, 2022, 2016],
                     
                     
    'box_office_crores': [1600, 1140, 600, 900, 1050, 
                          691, 1429, 379, 1387, 623],
                          
    'lead_actor': ['Allu Arjun', 'Shah Rukh Khan', 'Rajkkumar Rao', 'Ranveer Singh', 
                   'Shah Rukh Khan', 'Sunny Deol', 'Prabhas', 'Shahid Kapoor', 
                   'Ram Charan', 'Salman Khan']
}

# Create a DataFrame
bollywood_df = pd.DataFrame(data)

# 1. Basic Data Exploration
print("First Five Rows of the DataFrame:")
print(bollywood_df.head())

print("\nDataFrame Info:")
print(bollywood_df.info())

# 2. Genre Analysis
genre_counts = bollywood_df['genre'].value_counts()
print("\nMovie Count by Genre: \n", genre_counts)

# 3. Box Office Collection by Genre
box_office_by_genre = bollywood_df.groupby('genre')['box_office_crores'].sum()
print("\nTotal Box Office Collection by Genre:\n", box_office_by_genre)

# 4. Lead Actor Analysis
lead_actor_box_office = bollywood_df.groupby('lead_actor')['box_office_crores'].sum()
print("\nTotal Box Office Collection by Lead Actor:\n", lead_actor_box_office)

# 5. Bar Chart of Movie Count by Genre
plt.figure(figsize=(10, 6))
sns.countplot(x='genre', data=bollywood_df, palette='viridis')
plt.title("Number of Movies by Genre")
plt.xlabel('Genre')
plt.ylabel('Number of Movies')
plt.show()

# 6. Pie Chart of Box Office Collection by Genre
plt.figure(figsize=(8, 8))
plt.pie(box_office_by_genre, labels=box_office_by_genre.index, 
        autopct='%1.1f%%', startangle=140)
plt.title('Box Office Collection by Genre')
plt.show()
