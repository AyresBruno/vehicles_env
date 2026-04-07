import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # data reading
st.header('Car sales dashboard')

# Create button for histogram
hist_button = st.button('Create histogram')
if hist_button:  # if hist_button is pressed
    st.write('Creating histogram for car sales advertising')

    # histogram axis
    fig = px.histogram(car_data, x="odometer")

    # Show interactive Plotly graph
    st.plotly_chart(fig, use_container_width=True)


# Create scatter plots using car prices, model_year, cylinders, fuel, odometer and odometer readings

st.subheader('Scatter Plot')

# Variables
numeric_columns = ['price', 'model_year',
                   'cylinders', 'fuel', 'odometer', 'days_listed']

# Checkbox variables
x_axis = st.selectbox('Choose X variable:', numeric_columns)
y_axis = st.selectbox('Choose Y variable:', numeric_columns, index=1)

# Checkbox to hide or show scatter plot
show_scatter = st.button('Show Scatter Plot')

if show_scatter:  # if thecheckbox is marked
    st.write(f'Creating {x_axis} and {y_axis} Scatter Plot')

    # Create scatter plot
    fig_scatter = px.scatter(car_data, x=x_axis, y=y_axis)

    # Show graph
    st.plotly_chart(fig_scatter, use_container_width=True)
