import streamlit as st
import pandas as pd
import pymysql
from sqlalchemy import create_engine

# Database connection details
host = "localhost"
user = "root"
password = "praba12"  
database = "redbus_scrap"

# Connect to the database
@st.cache_data
def load_data():
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")
    query = "SELECT * FROM bus_details;"
    return pd.read_sql(query, engine)

# Load the data
df = load_data()

# Handle "No Rating" in the Ratings column
df["Ratings"] = df["Ratings"].replace("No Rating", 0.0).astype(float)

# Streamlit app layout
st.title("RedBus Data Filter")
st.write("Explore bus schedules, prices, ratings, and more")

# Filters
st.sidebar.header("Filters")
bus_type_filter = st.sidebar.multiselect("Select Bus Type", options=df["Bus_type"].unique(), default=df["Bus_type"].unique())
route_filter = st.sidebar.multiselect("Select Route", options=df["Route_name"].unique(), default=df["Route_name"].unique())
price_range = st.sidebar.slider("Select Price Range", int(df["Price"].min()), int(df["Price"].max()), (int(df["Price"].min()), int(df["Price"].max())))

# Streamlit slider for Ratings
ratings_filter = st.sidebar.slider(
    "Select Ratings Range",
    float(df["Ratings"].min()),
    float(df["Ratings"].max()),
    (float(df["Ratings"].min()), float(df["Ratings"].max()))
)

# Apply filters
filtered_data = df[
    (df["Bus_type"].isin(bus_type_filter)) &
    (df["Route_name"].isin(route_filter)) &
    (df["Price"] >= price_range[0]) &
    (df["Price"] <= price_range[1]) &
    (df["Ratings"] >= ratings_filter[0]) &
    (df["Ratings"] <= ratings_filter[1])
]

# Display filtered data
st.write(f"Showing {len(filtered_data)} results:")
st.dataframe(filtered_data)

# Option to view route links
if st.checkbox("Show Route Links"):
    st.write(filtered_data[["Route_name", "Route_link"]])

# Visualizations
st.header("Visualizations")
col1, col2 = st.columns(2)

with col1:
    st.bar_chart(filtered_data.groupby("Bus_type")["Price"].mean(), use_container_width=True)

with col2:
    st.bar_chart(filtered_data.groupby("Bus_type")["Ratings"].mean(), use_container_width=True)

# Footer
st.write("---")
st.write("**Developed by Prabakaran_D** - Data scraped from [RedBus](https://www.redbus.in)")