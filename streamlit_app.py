
import streamlit
import pandas


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')



streamlit.title('Hey')


fruits_selected = streamlit.multiselect("pick:", list(my_fruit_list.index))
fruits_to_show = my_fruits_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
