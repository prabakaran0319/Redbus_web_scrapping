# Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit

# Redbus_web_scrapping
I used Selenium to scrape bus route names and details from redbus.in. The scraped data, including bus name, route, rate, and ratings, was stored in a MySQL database. I then developed a Streamlit web app to display and filter the data interactively. The app allows users to easily access and explore bus route information.

# Project Overview
This project involves scraping bus route details from the redbus.in website, storing the data in a MySQL database, and creating an interactive Streamlit web app to filter and explore the data.

# Steps Involved:
# Web Scraping with Selenium:

Step 1: First, I used Selenium to scrape bus route names and route links from the redbus.in website. These links were essential for gathering more specific data on each bus route.
Step 2: I created a Jupyter Notebook (IPYNB) file to store this route data.

# Scraping Bus Details:
-With the route links collected earlier, I scraped detailed information about each bus, including:
Bus Name
Bus Type
Start Time
End Time
Total Duration
Price
Seats Available
Ratings
Route Name
Route Link
This scraping task was also stored in a separate IPYNB file.

# Combining Data:
- After scraping bus details for buses from 10 states, combined all the data into a single dataframe.
- Then performed data cleaning and preprocessing to ensure the dataset was accurate and well-structured for use in the MySQL database.
# Storing Data in MySQL:
-established a connection with MySQL to store the cleaned data.
-created a MySQL database and stored the web-scraped data under the following columns:
Bus_name
Bus_type
Start_time
End_time
Total_duration
Price
Seats_Available
Ratings
Route_name
Route_link

# Developing the Streamlit Web App:
- After the data was successfully stored in MySQL, I developed a Streamlit web application.
- This app allows users to filter the bus details based on various attributes like bus type, ratings, price, and others.
- The Streamlit app provides a user-friendly interface for exploring and analyzing the bus data interactively.
# Technologies Used:
- Selenium for web scraping.
- Pandas for data manipulation and preprocessing.
-MySQL for storing the data.
-Streamlit for creating the web app interface.
-Jupyter Notebook for organizing the scraping tasks.
# Key Features:
- Scraping Data: Fetches bus route names, links, and detailed information such as price, ratings, and schedule.
- MySQL Database: Stores the scraped data in a structured format.
- Streamlit Interface: An interactive web app to filter and explore the bus details.
# How the Project Works:
- Data Collection: The project begins by scraping bus route names and bus details using Selenium.
-Data Storage: After cleaning and preprocessing the data, it's stored in a MySQL database.
-User Interface: Users can then use the Streamlit app to filter and view bus data based on criteria like bus name, price, ratings, etc.
-This project demonstrates how to integrate web scraping, database management, and interactive web development into a single cohesive application.

