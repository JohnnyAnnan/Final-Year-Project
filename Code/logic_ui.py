### Importing dependencies

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

### Page title and icon
st.set_page_config(page_title="Machine Learning Customer Segmentation System", page_icon=":sparkles:")

### Body

# Custom CSS for accent color and other styles
st.markdown(
    """
    <style>
    /* General styles */
    body {
        font-family: 'Arial', sans-serif;
    }
    
    /* Accent color for headers and buttons */
    .accent {
        color: #ff6347;  /* Tomato color */
    }
    
    .stButton>button {
        background-color: #ff6347;  /* Tomato color */
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
    }
    
    .stButton>button:hover {
        background-color: #ff4500;  /* Darker tomato color */
    }
    
    /* Full-width header */
    .header {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
        background-color: #f8f9fa;
        padding: 10px 0;
    }
    .header img {
        margin-right: 20px;
    }
    .header h1 {
        font-size: 24px;
        margin: 0;
        color: #ff6347;  /* Tomato color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Full-width header with an image
st.markdown(
    """
    <div class="header">
        <h1>Machine Learning Customer Segmentation System</h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<br>', unsafe_allow_html=True)

# Intro
st.markdown(
    """
    <div style='text-align: center;'>
        <p>For Sample Sales Data</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<br><br>', unsafe_allow_html=True)

# Data upload

st.markdown('<label style="font-size: 20px; font-weight: bold;">Upload Data</label>', unsafe_allow_html=True)
files_names = list()
files = st.file_uploader("", key="file_uploader", type=['xlsx', 'csv'], accept_multiple_files=True)
if files:
    for file in files:
        files_names.append(file.name)

    st.markdown('<br>', unsafe_allow_html=True)

# Data selection

    st.markdown('<label style="font-size: 16px; font-weight: bold; margin-bottom: -16px;">Select Data for Analysis</label>', unsafe_allow_html=True)
    selected_files = st.multiselect('', options = files_names)
    if selected_files:
        attributes = st.radio('Select Atribute against Spending Score', options=[ 'None', 'Gender', 'Age', 'Annual Income ($)', 'Profession',	'Work Experience'])

# Feature Engineering ( Feature Extraction: Extracting 'Age' column and 'Spending Score' column )
X = customer_data.iloc[:,[2,4]].values

''' print(X) '''

# Implementing the k-means clustering model and choosing the optimal number of clusters for the model

    # Instantiating the K-means clustering model and finding the WCSS values of different number of clusters of the dataset
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

        #Identification of the optimal number of clusters

        #Calculating the first differences
differences = np.diff(wcss)

        #Calculating the second differences
second_differences = np.diff(differences)

        # Finding the index of the knee point (maximum curvature)
knee_index = np.argmax(second_differences) + 1

        # Optimal number of clusters
optimal_clusters = knee_index + 1

''' print("Optimal number of clusters:", optimal_clusters) '''

# Training the k-means clustering model

    # Supplying the optimal number of clusters to the model
kmeans = KMeans(n_clusters=optimal_clusters, init='k-means++', random_state=42)

    # Specifying the return of a label for each data point based on their cluster
Y = kmeans.fit_predict(X)

''' print(Y) '''

# Visualizing of insights
