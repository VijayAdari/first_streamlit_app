import streamlit

streamlit.title("๐๐๐ฑโ๐ My parents new healthy dinner")
streamlit.header("๐ฑโ๐Breakfast Menu")
streamlit.text("โ๐Omega 3 & Blueberry oatmeal")
streamlit.text("๐ถKale, Spinnach & rocket smoothie")
streamlit.text("๐ฑโ๐ปHard boilded Free-range egg")

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruit_to_show = my_fruit_list.loc[fruit_selected]

# Display the table on the page.

streamlit.dataframe(fruit_to_show)
