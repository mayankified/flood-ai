import streamlit as st
import matplotlib.pyplot as plt
import rasterio
from rasterio.plot import show
from PIL import Image
import plotly.express as px
import pandas as pd
import numpy as np


def plot_specific_range(tiff_file, vmin, vmax):
    with rasterio.open(tiff_file) as src:
        # Read the first band of the TIFF file
        image_data = src.read(1)

        # Mask out the values that are not in the desired range
        mask = np.logical_or(image_data < vmin, image_data > vmax)
        masked_image_data = np.ma.masked_where(mask, image_data)

        # Plot the image with transparency for the masked out regions
        fig, ax = plt.subplots(figsize=(6, 6))
        cmap = plt.cm.get_cmap('Blues').copy()  # Use any colormap you prefer
        cmap.set_bad(color=(1, 1, 1, 0))  # Set masked (bad) values to transparent
        show(masked_image_data, ax=ax, cmap=cmap)
        plt.title("Predicted Flood (Specific Range)")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")

        st.pyplot(fig)
        
        
# Set page configuration
st.set_page_config(page_title="Kozhikode Flood Monitoring", page_icon="Images/flood.ico", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for improved UI
st.markdown("""
    <style>
        /* Main container */
        .stApp {
            background-color: #FFFFFF;
            color: #000000;
        }
        /* Sidebar */
        .sidebar .sidebar-content {
            background-color: #F5F5F5;
            color: #000000;
        }
        /* Sidebar Button Styles */
        .sidebar .sidebar-content a {
            background-color: #007BFF;
            color: #FFFFFF !important;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            padding: 10px;
            border-radius: 8px;
            display: block;
            margin-bottom: 10px;
            text-decoration: none;
        }
        .sidebar .sidebar-content a:hover {
            background-color: #0056b3;
            color: #FFFFFF !important;
        }
        /* Page Titles and Headers */
        h1, h2, h3 {
            color: #000;
            text-align: center;
        }
        h4 {
            color: #00C59F;
            text-align: left;
        }
        /* Image */
        .wide-image {
            width: 100%;
            height: auto;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        /* Video */
        video {
            width: 100%;
            height: auto;
            margin-bottom: 20px;
        }
        /* Divider */
        hr {
            margin: 1rem 0;
            border: none;
            border-top: 1px solid #ddd;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar with navigation links
st.sidebar.title("FLOOD SENSE")
st.sidebar.markdown("[Dashboard](#dashboard)", unsafe_allow_html=True)
st.sidebar.markdown("[Home](#home)", unsafe_allow_html=True)
st.sidebar.markdown("[Impact](#impact)", unsafe_allow_html=True)
st.sidebar.markdown("[Reporting](https://externalwebsite.com)", unsafe_allow_html=True)  # Replace with actual URL
st.sidebar.write("-----")

# Main Dashboard Content
st.markdown("<h1>Kozhikode Flood Monitoring Dashboard</h1>", unsafe_allow_html=True)

# Wide image in JPEG format
image = Image.open('img/WhatsApp Image 2024-08-25 at 11.18.23.jpeg')  # Replace with your actual image path
st.image(image, caption='Kozhikode Flood Monitoring', use_column_width=True, output_format='JPEG')

# Research Vertical Section
st.markdown("<h2>Research Vertical</h2>", unsafe_allow_html=True)

# Display 4 TIFF Files in 2x2 Grid
st.write("### Flood Data Analysis - TIFF Files")

tiff_files = [
    ('/home/mayank/Desktop/Projects/finalll/snapped_data/snapped_DEM.tif', "Digital Elevation Model"),
    ('/home/mayank/Desktop/Projects/finalll/snapped_data/snapped_landuse.tif', "Land Use"),
    ('/home/mayank/Desktop/Projects/finalll/snapped_data/snapped_slope.tif', "Slope"),
    ('/home/mayank/Desktop/Projects/finalll/snapped_data/snapped_soil.tif', "Soil Type")
]

# Create two rows with two columns each
row1_col1, row1_col2 = st.columns(2)
row2_col1, row2_col2 = st.columns(2)

# First row
for i, (tiff_file, title) in enumerate(tiff_files[:2]):
    with rasterio.open(tiff_file) as src:
        fig, ax = plt.subplots(figsize=(6, 6))
        show(src, ax=ax)
        ax.set_title(title)
        if i == 0:
            row1_col1.pyplot(fig)
        else:
            row1_col2.pyplot(fig)

# Second row
for i, (tiff_file, title) in enumerate(tiff_files[2:]):
    with rasterio.open(tiff_file) as src:
        fig, ax = plt.subplots(figsize=(6, 6))
        show(src, ax=ax)
        ax.set_title(title)
        if i == 0:
            row2_col1.pyplot(fig)
        else:
            row2_col2.pyplot(fig)

st.write("-----")

# Time Series Plot of Precipitation Data
st.write("### Precipitation Time Series Data")
precipitation_data = pd.read_csv('/home/mayank/Desktop/Projects/finalll/precipitation_data.csv')  # Replace with your actual CSV file path
fig = px.line(precipitation_data, x='Date', y='tp', title='Time Series of Precipitation in Kozhikode')
st.plotly_chart(fig, use_container_width=True)
st.write("-----")

# Video Simulation of Flood in MP4 format
# st.write("### Flood Simulation Video")
# video_file = open('Videos/flood_simulation.mp4', 'rb')  # Replace with your actual video path
# video_bytes = video_file.read()
# st.video(video_bytes)
# st.write("-----")

# Display Observed and Predicted TIFF Files Side by Side
st.write("### Flood Observation vs Prediction")
col1, col2 = st.columns(2)

with col1:
    st.write("**Observed Flood**")
    image1 = Image.open('/home/mayank/Desktop/Projects/finalll/img/predictredsdsda.jpeg')  # Replace with your actual image path
    st.image(image1, caption='Infrastructure Impact - Image 1', use_column_width=True, output_format='PNG')
    # with rasterio.open('/home/mayank/Desktop/Projects/finalll/pred/clipped_Sim7_2BaseDefault_2D_overland_elements_095.shp.tif') as observed_src:  # Replace with your actual TIFF file path
    #     fig, ax = plt.subplots(figsize=(6, 6))
    #     show(observed_src, ax=ax)
    #     plt.title("Observed Flood")
    #     st.pyplot(fig)

with col2:
    st.write("**Predicted Flood**")
    with rasterio.open('/home/mayank/Desktop/Projects/finalll/pred/predicted_flood_map.tif') as predicted_src:  # Replace with your actual TIFF file path
        fig, ax = plt.subplots(figsize=(6, 3))
        show(predicted_src, ax=ax)
        plt.title("Predicted Flood")
        plot_specific_range("/home/mayank/Desktop/Projects/finalll/pred/predicted_flood_map.tif", 1500, 6000)
