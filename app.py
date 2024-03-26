import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('data/world.sqlite')
c = conn.cursor()


def sql_executor(query):
    c.execute(query)
    data = c.fetchall()
    return data


city = ['ID', 'Name', 'CountryCode', 'District', 'Population']
country = ['Code', 'Name', 'Continent', 'Region', 'SurfaceArea', 'IndepYear', 'Population', 'LifeExpectancy', 'GNP',
           'GNPOld', 'LocalName', 'GovernmentForm', 'HeadOfState', 'Capital', 'Code2']
countrylanguage = ['CountryCode', 'Language', 'IsOfficial', 'Percentage']

def main():
    st.title('SQL Playground')

    menu = ['Home', 'About']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home':
        st.subheader('Home')

        col1, col2 = st.columns(2)
        with col1:
            with st.form(key="query_form"):
                query = st.text_area("SQL Code Here")
                submit_button = st.form_submit_button(label="Execute")

            with st.expander("Table Info"):
                t_info = {'city': city, 'country': country, 'countrylanguage': countrylanguage}
                st.json(t_info)

        with col2:
            if submit_button:
                st.info('Query Executed')
                st.code(query)

                query_result = sql_executor(query)
                with st.expander("Query Result"):
                    st.write(query_result)
                with st.expander("Pretty Table"):
                    df = pd.DataFrame(query_result)
                    st.dataframe(df)

    else:
        st.subheader('About')


if __name__ == '__main__':
    main()