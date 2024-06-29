# MARKDOWN CELL
# # Restaurant Data Merge Example
# 
# This notebook demonstrates how to generate sample restaurant data, perform different types of merges using pandas, and analyze the results. We'll walk through the process step-by-step, explaining each operation and its significance in data analysis.

# MARKDOWN CELL
# ## Setup
# First, we'll import the necessary libraries and set a random seed for reproducibility.

# CODE CELL
import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# MARKDOWN CELL
# ## Generating Restaurant Data
# 
# We'll create a sample dataset of 20 restaurants with the following attributes:
# - Name: Creative name of the restaurant
# - Cuisine: Type of food served (e.g., Italian, Chinese, Mexican)
# - Location: Area where the restaurant is located
# - RestaurantID: A unique identifier for each restaurant

# CODE CELL
# Define the restaurant data
restaurant_data = [
    ("The Pasta Palace", "Italian", "Downtown"),
    ("Sizzling Sichuan", "Chinese", "Chinatown"),
    ("Taco Fiesta", "Mexican", "Suburb"),
    ("Curry Comfort", "Indian", "Uptown"),
    ("Big Bob's BBQ", "American", "Suburb"),
    ("Pizza Paradise", "Italian", "Beach"),
    ("Golden Dragon", "Chinese", "Downtown"),
    ("Burrito Bonanza", "Mexican", "Downtown"),
    ("Naan & Curry", "Indian", "Suburb"),
    ("Stars & Stripes Diner", "American", "Highway"),
    ("Mama Mia's Trattoria", "Italian", "Little Italy"),
    ("Wok This Way", "Chinese", "Uptown"),
    ("Guac & Roll", "Mexican", "Beach"),
    ("Spice Route", "Indian", "Downtown"),
    ("Uncle Sam's Steakhouse", "American", "Financial District"),
    ("Olive Oasis", "Italian", "Suburb"),
    ("Dumpling Delight", "Chinese", "Chinatown"),
    ("Salsa Street", "Mexican", "Downtown"),
    ("Tandoori Nights", "Indian", "Little India"),
    ("Burger Barn", "American", "Countryside")
]

# Create a DataFrame from the restaurant data
restaurants_df = pd.DataFrame(restaurant_data, columns=['Name', 'Cuisine', 'Location'])

# Add a unique RestaurantID for each restaurant
restaurants_df['RestaurantID'] = range(1, len(restaurants_df) + 1)

print("Restaurants data:")
display(restaurants_df)

# MARKDOWN CELL
# ## Generating Ratings Data
# 
# Now we'll create a separate dataset for restaurant ratings. Not all restaurants will have ratings, simulating a real-world scenario where some restaurants might not have been reviewed yet.

# CODE CELL
# Generate ratings data (not all restaurants get ratings)
num_ratings = 15  # We'll generate ratings for 15 out of 20 restaurants
rated_restaurant_ids = np.random.choice(restaurants_df['RestaurantID'], num_ratings, replace=False)
ratings = np.random.randint(1, 6, num_ratings)  # Ratings from 1 to 5

ratings_df = pd.DataFrame({
    'RestaurantID': rated_restaurant_ids,
    'Rating': ratings
})

print("Ratings data:")
display(ratings_df)

# MARKDOWN CELL
# ## Performing Different Types of Merges
# 
# Now that we have our two datasets (restaurants and ratings), we'll demonstrate different types of merges in pandas. Each type of merge combines the datasets differently, which can be useful for various analysis scenarios.

# MARKDOWN CELL
# ### Inner Merge
# An inner merge returns only the rows where there's a match in both DataFrames. In our case, this will give us only the restaurants that have ratings.

# CODE CELL
inner_merge = pd.merge(restaurants_df, ratings_df, on='RestaurantID', how='inner')

print("Inner Merge Result:")
display(inner_merge)
print(f"Shape: {inner_merge.shape}")

# MARKDOWN CELL
# ### Left Merge
# A left merge returns all rows from the left DataFrame (restaurants) and matching rows from the right DataFrame (ratings). Restaurants without ratings will have NaN in the Rating column.

# CODE CELL
left_merge = pd.merge(restaurants_df, ratings_df, on='RestaurantID', how='left')

print("Left Merge Result:")
display(left_merge)
print(f"Shape: {left_merge.shape}")

# MARKDOWN CELL
# ### Right Merge
# A right merge returns all rows from the right DataFrame (ratings) and matching rows from the left DataFrame (restaurants). In our case, this will be identical to the inner merge because all ratings have a matching restaurant.

# CODE CELL
right_merge = pd.merge(restaurants_df, ratings_df, on='RestaurantID', how='right')

print("Right Merge Result:")
display(right_merge)
print(f"Shape: {right_merge.shape}")

# MARKDOWN CELL
# ### Outer Merge
# An outer merge returns all rows when there is a match in either DataFrame. This will include all restaurants and all ratings, with NaN values where there's no match.

# CODE CELL
outer_merge = pd.merge(restaurants_df, ratings_df, on='RestaurantID', how='outer')

print("Outer Merge Result:")
display(outer_merge)
print(f"Shape: {outer_merge.shape}")

# MARKDOWN CELL
# ## Data Analysis
# 
# Now that we've explored different merge techniques, let's use our merged data to gain some insights about the restaurants.

# MARKDOWN CELL
# ### Cuisine Popularity Contest
# Let's see which cuisines are the most popular based on their average ratings.

# CODE CELL
cuisine_ratings = inner_merge.groupby('Cuisine')['Rating'].agg(['mean', 'count'])
cuisine_ratings = cuisine_ratings.sort_values('mean', ascending=False)

print("Cuisine Popularity Contest:")
display(cuisine_ratings)

# MARKDOWN CELL
# ### Location Hotspots
# Now let's check which locations have the highest-rated restaurants.

# CODE CELL
location_ratings = inner_merge.groupby('Location')['Rating'].agg(['mean', 'count'])
location_ratings = location_ratings.sort_values('mean', ascending=False)

print("Location Hotspots:")
display(location_ratings)

# MARKDOWN CELL
# ### Top 3 Restaurants
# Let's find out which are the three highest-rated restaurants.

# CODE CELL
top_restaurants = inner_merge.sort_values('Rating', ascending=False).head(3)

print("Top 3 Restaurants:")
display(top_restaurants[['Name', 'Cuisine', 'Location', 'Rating']])

# MARKDOWN CELL
# ### Underdog Restaurants (Not Yet Rated)
# Using our left merge result, we can identify which restaurants haven't been rated yet.

# CODE CELL
unrated = left_merge[left_merge['Rating'].isna()]

print("Underdog Restaurants (Not Yet Rated):")
display(unrated[['Name', 'Cuisine', 'Location']])

# MARKDOWN CELL
# ### Wordplay Winners
# Just for fun, let's find restaurants with repeated words in their names.

# CODE CELL
def has_repeated_word(name):
    words = name.lower().split()
    return len(words) != len(set(words))

wordplay_restaurants = restaurants_df[restaurants_df['Name'].apply(has_repeated_word)]

print("Wordplay Winners:")
display(wordplay_restaurants[['Name', 'Cuisine', 'Location']])

# MARKDOWN CELL
# ### Cuisine Diversity by Location
# Finally, let's see how many different types of cuisines are available in each location.

# CODE CELL
cuisine_diversity = restaurants_df.groupby('Location')['Cuisine'].nunique().sort_values(ascending=False)

print("Cuisine Diversity by Location:")
display(cuisine_diversity)

# MARKDOWN CELL
# ## Conclusion
# 
# In this notebook, we demonstrated how to:
# 1. Generate sample restaurant and ratings data
# 2. Perform different types of merges (inner, left, right, outer)
# 3. Analyze the merged data to gain insights about restaurants, cuisines, and locations
# 
# This example shows the power of pandas for data manipulation and analysis in Python. By using different merge techniques and grouping operations, we were able to extract various insights from our dataset, such as popular cuisines, top-rated locations, and cuisine diversity across locations.
# 
# Further analysis could involve more complex statistical methods, visualizations, or machine learning techniques to derive even more insights from this data.