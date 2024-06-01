from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')  # Specify the parser explicitly

# Find the relevant table
table = soup.find('table', class_='wikitable sortable')

# Extract table headers
world_titles = table.find_all('th')
world_table_titles = [title.text.strip() for title in world_titles]

# Create a DataFrame
df = pd.DataFrame(columns=world_table_titles)

# Extract table rows
column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    # Append the row to the DataFrame
    length = len(df)
    df.loc[length] = individual_row_data

# Display the DataFrame
print(df)
