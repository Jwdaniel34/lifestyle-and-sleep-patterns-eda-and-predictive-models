import streamlit as st
import pandas as pd
import plotly.express as px

# Load data (replace with your actual data loading if not in notebook)
@st.cache_data
def load_data():
    # For demo, load CSV directly; or load preprocessed pandas_df
    return pd.read_csv('lifestyle_and_sleep_patterns.csv')

df = load_data()

df = df.dropna(subset=['Sleep Disorder'])
st.title("Sleep and Lifestyle Patterns Dashboard")

# Sidebar filters
gender_filter = st.sidebar.multiselect(
    "Select Gender",
    options=df['Gender'].unique(),
    default=df['Gender'].unique()
)

occupation_filter = st.sidebar.multiselect(
    "Select Occupation",
    options=df['Occupation'].unique(),
    default=df['Occupation'].unique()
)

# Filter dataframe based on selections
filtered_df = df[
    (df['Gender'].isin(gender_filter)) &
    (df['Occupation'].isin(occupation_filter))
]

st.write(f"### Filtered data has {len(filtered_df)} rows")

# Plot 1: Sleep Duration distribution by Gender
fig1 = px.histogram(filtered_df, x="Sleep Duration", color="Gender",
                    nbins=30, barmode='overlay', title="Sleep Duration Distribution by Gender")
st.plotly_chart(fig1)

# Plot 2: Sleep Quality vs Stress Level scatter plot
fig2 = px.scatter(filtered_df, x="Stress Level", y="Quality of Sleep", color="Occupation",
                  title="Stress Level vs Quality of Sleep")
st.plotly_chart(fig2)

# Plot 3: Sleep Disorder count by Occupation
sleep_disorder_count = filtered_df.groupby("Occupation")["Sleep Disorder"].apply(lambda x: x.notnull().sum()).reset_index()
sleep_disorder_count.columns = ['Occupation', 'Sleep Disorder Count']

fig3 = px.bar(sleep_disorder_count, x='Occupation', y='Sleep Disorder Count',
              title="Count of Sleep Disorders by Occupation")
st.plotly_chart(fig3)