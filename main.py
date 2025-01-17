import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.header("Data Analysis of dataset")
uploaded_file = st.file_uploader("Upload file", type='csv')
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Displaying first five rows of the dataframe:")
    st.write(df.head())
    st.subheader("Displaying the summary of the whole dataset:")
    st.write(df.describe())
    st.subheader("Filter Data:")
    iterable_columns = df.columns
    selected_column = st.selectbox("Please select a column to filter:", options=iterable_columns)
    unique_values = df[selected_column].unique()
    selected_unique_value = st.selectbox("Please select the value to filter:", options=unique_values)
    
    filtered_df = df[df[selected_column]==selected_unique_value]
    st.write(filtered_df)

    st.subheader("Plot the data:")
    data_to_plot = st.multiselect(f"Please select a column to plot\
                                 against date for the city of {selected_unique_value}:", \
                                    options=iterable_columns)
    st.line_chart(data=filtered_df, x='Date', y=data_to_plot)
    pass
else:
    st.write("Waiting to upload file...")