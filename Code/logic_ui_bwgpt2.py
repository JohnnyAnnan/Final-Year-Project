
'''
- 
'''

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Function to perform clustering and visualization
def perform_clustering(filtered_df, attributes, selected_category):
    # Prepare data for clustering
    if attributes == 'Age':
        X = filtered_df[['Age', 'Spending Score (1-100)']].values
    elif attributes == 'Annual Income ($)':
        X = filtered_df[['Annual Income ($)', 'Spending Score (1-100)']].values
    else:
        st.warning("Invalid attribute for clustering.")
        return

    # Perform K-means clustering
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)

    # Finding optimal number of clusters
    differences = np.diff(wcss)
    second_differences = np.diff(differences)
    knee_index = np.argmax(second_differences) + 1
    optimal_clusters = knee_index + 1

    # Training K-means with optimal number of clusters
    kmeans = KMeans(n_clusters=optimal_clusters, init='k-means++', random_state=42)
    Y = kmeans.fit_predict(X)

    # Add cluster labels to the filtered dataframe
    filtered_df['Cluster'] = Y

    # Define spending score categories
    spending_bins = [0, 33, 66, 100]
    spending_labels = ['Low', 'Medium', 'High']
    filtered_df['Spending Category'] = pd.cut(filtered_df['Spending Score (1-100)'], bins=spending_bins, labels=spending_labels, include_lowest=True)

    # Create pie chart for spending score distribution
    category_counts = filtered_df['Spending Category'].value_counts().sort_index()

    st.markdown('<br><br>', unsafe_allow_html=True)
    # Plotting spending score distribution
    st.markdown(f'<h2 style="text-align:center; color:#ff6347;">Spending Score Distribution for {selected_category}</h2>', unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.pie(category_counts, labels=[f'{label} ({category_counts[label]})' for label in category_counts.index], autopct='%1.1f%%', startangle=140, colors=['#66c2a5', '#fc8d62', '#8da0cb'])
    st.pyplot(fig)

  


# Streamlit app
# Page configuration
st.set_page_config(page_title="Customer Segmentation", page_icon=":bar_chart:", layout="wide")

# Sidebar
st.sidebar.title('Navigation')
page = st.sidebar.radio('', ['Upload Data', 'Explore Data'])

if page == 'Upload Data':
    st.markdown('<style>body{background-color: #f0f2f6;}</style>', unsafe_allow_html=True)
    st.markdown(
        """
        <style>
        .header {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            background-color: #ffffff;
            padding: 10px 0;
        }
        .header h1 {
            font-size: 36px;
            margin: 0;
            color: #ff6347;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Full-width header with a title
    st.markdown(
        """
        <div class="header">
            <h1>Customer Segmentation</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<br>', unsafe_allow_html=True)

    # Intro
    st.markdown(
        """
        <div style='text-align: center;'>
            <p>Upload your sales data in CSV or Excel format to perform customer segmentation using K-Means clustering.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<br><br>', unsafe_allow_html=True)

    # Data upload
    st.markdown('<label style="font-size: 20px; font-weight: bold;">Upload Data</label>', unsafe_allow_html=True)
    files = st.file_uploader("Upload CSV or Excel files", type=['xlsx', 'csv'], accept_multiple_files=True)
    if files:
        df = pd.concat([pd.read_csv(file) for file in files])
        st.markdown('<label style="font-size: 16px; font-weight: bold;">Data Overview</label>', unsafe_allow_html=True)
        st.write(df.head())

        st.markdown('<br><br>', unsafe_allow_html=True)

        # Data selection
        st.markdown('<label style="font-size: 16px; font-weight: bold;">Explore Spending Score by</label>', unsafe_allow_html=True)
        attributes = st.selectbox('', options=['None', 'Gender', 'Age', 'Annual Income ($)', 'Profession', 'Work Experience'])
        if attributes != 'None':
            st.markdown(f"<h3 style='color:#ff6347;'>Selected Attribute: {attributes}</h3>", unsafe_allow_html=True)

            # Feature Engineering based on selected attribute
            if attributes == 'Age':
                # Categorize age into meaningful groups
                age_bins = [0, 30, 60, 100]
                age_labels = ['Youth', 'Adult', 'Elderly']
                df['Age Category'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, include_lowest=True)

                # Allow user to select age category for insights visualization
                selected_category = st.selectbox('Select Age Category', options=age_labels)

                # Filter data by selected age category
                filtered_df = df[df['Age Category'] == selected_category]

                # Perform K-means clustering
                perform_clustering(filtered_df, attributes, selected_category)

            elif attributes == 'Annual Income ($)':
                # Categorize annual income into meaningful groups
                income_bins = [0, 30000, 70000, 150000]
                income_labels = ['Low Income', 'Middle Income', 'High Income']
                df['Income Category'] = pd.cut(df['Annual Income ($)'], bins=income_bins, labels=income_labels, include_lowest=True)

                # Allow user to select income category for insights visualization
                selected_category = st.selectbox('Select Income Category', options=income_labels)

                # Filter data by selected income category
                filtered_df = df[df['Income Category'] == selected_category]

                # Perform K-means clustering
                perform_clustering(filtered_df, attributes, selected_category)

            else:
                st.warning("Please select an attribute to proceed.")
                st.stop()

elif page == 'Explore Data':
    st.markdown('<style>body{background-color: #f0f2f6;}</style>', unsafe_allow_html=True)
    st.markdown(
        """
        <style>
        .header {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            background-color: #ffffff;
            padding: 10px 0;
        }
        .header h1 {
            font-size: 36px;
            margin: 0;
            color: #ff6347;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Full-width header with a title
    st.markdown(
        """
        <div class="header">
            <h1>Customer Segmentation</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<br>', unsafe_allow_html=True)

    st.markdown('<h2 style="text-align:center; color:#ff6347;">Explore Customer Segmentation Insights</h2>', unsafe_allow_html=True)
    st.markdown(
        """
        <p>Use the sidebar to navigate and upload data for customer segmentation analysis. Explore different attributes such as age, annual income, profession, etc., to visualize spending score distributions and cluster visualizations.</p>
        """,
        unsafe_allow_html=True
    )

# Summary
st.markdown('<br><br>', unsafe_allow_html=True)
st.markdown(
    """
    <div style='text-align: center;'>
        <p>Thank you for using the Customer Segmentation System!</p>
    </div>
    """,
    unsafe_allow_html=True
)
