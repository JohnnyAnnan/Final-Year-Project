'''Key points:
- Users uploading data and sytem taking csv or excel data and providing users columns to analyze against spending score
- utilization of kmeans and visualizaion leveraging streamlit with iteractive output with selected insights to present
- enhancing ui good, ( ... )
- checking libraries present in python standard library and installing requisites
( ... )
( !! no stress, efficiency, ( ... ) )
( !! good, ( ... ) learning, ( ... ) with implementation, ( ... ))
( !! corrections, additions, (...) )
'''

### Importing dependencies
import streamlit as st
import pandas as pd
import plotly.express as px

### Page title and icon
st.set_page_config(page_title="Machine Learning Customer Segmentation System", page_icon=":sparkles:")

### Custom CSS for accent color and other styles
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
    }
    .accent {
        color: #ff6347;
    }
    .stButton>button {
        background-color: #ff6347;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #ff4500;
    }
    .header {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
        background-color: #f8f9fa;
        padding: 10px 0;
    }
    .header h1 {
        font-size: 24px;
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
        <h1>Machine Learning Customer Segmentation System</h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<br>', unsafe_allow_html=True)

### Intro
st.markdown(
    """
    <div style='text-align: center;'>
        <p>Upload your sales data in CSV or Excel format to perform customer segmentation using K-Means clustering.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<br><br>', unsafe_allow_html=True)

### Data upload
st.markdown('<label style="font-size: 20px; font-weight: bold;">Upload Data</label>', unsafe_allow_html=True)
file = st.file_uploader("", type=['xlsx', 'csv'])

if file:
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)
    
    st.write(df.head())

    st.markdown('<br>', unsafe_allow_html=True)

    # Attribute selection for analysis
    st.markdown('<label style="font-size: 16px; font-weight: bold;">Select Attribute against Spending Score</label>', unsafe_allow_html=True)
    attribute = st.selectbox('', options=['Gender', 'Age', 'Annual Income ($)', 'Profession', 'Work Experience'])

    if attribute:
        # Define spending score categories
        bins = [0, 33, 66, 100]
        labels = ['Low', 'Medium', 'High']
        df['Spending Category'] = pd.cut(df['Spending Score (1-100)'], bins=bins, labels=labels, include_lowest=True)
        
        # Select which spending score group to visualize
        st.markdown('<label style="font-size: 16px; font-weight: bold;">Select Spending Score Group to Visualize</label>', unsafe_allow_html=True)
        selected_group = st.selectbox('', options=labels)
        
        # Filter data by selected spending score group
        group_data = df[df['Spending Category'] == selected_group]

        # Group data by selected attribute within the spending score group
        attribute_counts = group_data[attribute].value_counts(normalize=True) * 100
        attribute_counts = attribute_counts.reset_index()
        attribute_counts.columns = [attribute, 'Percentage']

        ### Leaderboard Visual for Selected Spending Score Group
        st.markdown(f'<label style="font-size: 20px; font-weight: bold;">{selected_group} Spending Score Distribution for {attribute}</label>', unsafe_allow_html=True)

        fig = px.bar(attribute_counts, x='Percentage', y=attribute, orientation='h', 
                     color='Percentage', color_continuous_scale='Viridis', 
                     labels={attribute: attribute, 'Percentage': 'Percentage (%)'}, 
                     title=f'{selected_group} Spending Score Distribution for {attribute}')
        
        fig.update_layout(yaxis={'categoryorder': 'total ascending'}, height=600)
        st.plotly_chart(fig, use_container_width=True)

### Summary
st.markdown('<br><br>', unsafe_allow_html=True)
st.markdown(
    """
    <div style='text-align: center;'>
        <p>Thank you for using the Machine Learning Customer Segmentation System!</p>
    </div>
    """,
    unsafe_allow_html=True
)
