import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Kozhikode Flood Monitoring - Impact", page_icon="Images/flood.ico", layout="wide", initial_sidebar_state="expanded")

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
            color: #000000;
            text-align: center;
        }
        h4 {
            color: #00C59F;
            text-align: left;
            margin-bottom: 20px;
        }
        /* Center and resize smaller images */
        .smaller-image {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%;  /* Set to 50% of original size */
        }
        /* Image Styling */
        .impact-image {
            width: 100%;
            height: auto;
            border-radius: 10px;
            margin-bottom: 20px;
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

# Main Impact Page Content
st.markdown("<h1>Impact of Floods</h1>", unsafe_allow_html=True)

# Infrastructure Impact Section
st.markdown("<h2>Infrastructure Impact</h2>", unsafe_allow_html=True)

# Display two images side by side for Infrastructure Impact
col1, col2 = st.columns(2)

with col1:
    image1 = Image.open('/home/mayank/Desktop/Projects/finalll/img/buildings.png')  # Replace with your actual image path
    st.image(image1, caption='Infrastructure Impact - Image 1', use_column_width=True, output_format='PNG')

with col2:
    image2 = Image.open('/home/mayank/Desktop/Projects/finalll/img/Impacted_roads.png')  # Replace with your actual image path
    st.image(image2, caption='Infrastructure Impact - Image 2', use_column_width=True, output_format='PNG')

st.write("-----")

# Community Impact Section
st.markdown("<h2>Community Impact</h2>", unsafe_allow_html=True)

# Display one image for Community Impact
community_image = Image.open('/home/mayank/Desktop/Projects/finalll/maps/Social Vulnerability map.png')  # Replace with your actual image path
st.image(community_image, caption='Community Impact', width=500, output_format='PNG')

st.write("-----")

# General Info Section
st.markdown("<h2>General Information</h2>", unsafe_allow_html=True)

# Dropdown to select an image to view
general_images = {
    "General Info - Household": "/home/mayank/Desktop/Projects/finalll/maps/Household.png",  # Replace with your actual image paths
    "General Info - Illiterate population": "/home/mayank/Desktop/Projects/finalll/maps/Illiterate population.png",
    "General Info - Infant Population": "/home/mayank/Desktop/Projects/finalll/maps/Infant population.png",
    "General Info - Total population": "/home/mayank/Desktop/Projects/finalll/maps/Total Population.png"
}

selected_image = st.selectbox("Select an image to view:", list(general_images.keys()))

# Display the selected image with smaller size and centered
selected_image_path = general_images[selected_image]
selected_img = Image.open(selected_image_path)
st.image(selected_img, caption=selected_image, use_column_width=False, output_format='PNG', width=500)  # Resize to 50% width

st.write("-----")

# Footer or Additional Content
st.markdown("<h4>For more information, visit the Reporting section in the sidebar.</h4>", unsafe_allow_html=True)
