# importing libraries
import pandas as pd
import pymysql
import streamlit as slt
from streamlit_option_menu import option_menu
import time

# kerala bus
lists_k=[]
df_k=pd.read_csv("df_K.csv")
for i,r in df_k.iterrows():
    lists_k.append(r["Route_name"])

#Andhra bus
lists_A=[]
df_A=pd.read_csv("df_A.csv")
for i,r in df_A.iterrows():
    lists_A.append(r["Route_name"])

#West bengal bus
lists_WB=[]
df_WB=pd.read_csv("df_WB.csv")
for i,r in df_WB.iterrows():
    lists_WB.append(r["Route_name"])

#Telungana bus
lists_T=[]
df_T=pd.read_csv("df_TS.csv")
for i,r in df_T.iterrows():
    lists_T.append(r["Route_name"])

#Himachal bus
lists_H=[]
df_H=pd.read_csv("df_H.csv")
for i,r in df_H.iterrows():
    lists_H.append(r["Route_name"])

#Rajastan bus
lists_R=[]
df_R=pd.read_csv("df_R.csv")
for i,r in df_R.iterrows():
    lists_R.append(r["Route_name"])


#Punjab bus 
lists_P=[]
df_P=pd.read_csv("df_P.csv")
for i,r in df_P.iterrows():
    lists_P.append(r["Route_name"])

#Chandigarh bus
lists_C=[]
df_C=pd.read_csv("df_C.csv")
for i,r in df_C.iterrows():
    lists_C.append(r["Route_name"])

#Jammu and Kashmir bus
lists_JK=[]
df_JK=pd.read_csv("df_JK.csv")
for i,r in df_JK.iterrows():
    lists_JK.append(r["Route_name"])

#UP bus
lists_UP=[]
df_UP=pd.read_csv("df_UP.csv")
for i,r in df_UP.iterrows():
    lists_UP.append(r["Route_name"])

#Assam bus
lists_AS=[]
df_AS=pd.read_csv("df_AS.csv")
for i,r in df_AS.iterrows():
    lists_AS.append(r["Route_name"])

#setting up streamlit page
slt.set_page_config(layout="wide")

web=option_menu(menu_title="🚌OnlineBus",
                options=["Home","📍States and Routes"],
                icons=["house","info-circle"],
                orientation="horizontal"
                )
# Home page setting
if web=="Home":
    slt.image("bus_image.jpg",width=200)
    slt.title("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit")
    slt.subheader(":red[Domain:]  Transportation")
    slt.subheader(":red[Ojective:] ")
    slt.markdown("The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.")
    slt.subheader(":red[Overview:]") 
    slt.markdown("Selenium: Selenium is a tool used for automating web browsers. It is commonly used for web scraping, which involves extracting data from websites. Selenium allows you to simulate human interactions with a web page, such as clicking buttons, filling out forms, and navigating through pages, to collect the desired data...")
    slt.markdown('''Pandas: Use the powerful Pandas library to transform the dataset from CSV format into a structured dataframe.
                    Pandas helps data manipulation, cleaning, and preprocessing, ensuring that data was ready for analysis.''')
    slt.markdown('''MySQL: With help of SQL to establish a connection to a SQL database, enabling seamless integration of the transformed dataset
                    and the data was efficiently inserted into relevant tables for storage and retrieval.''')
    slt.markdown("Streamlit: Developed an interactive web application using Streamlit, a user-friendly framework for data visualization and analysis.")
    slt.subheader(":red[Skill-take:]")
    slt.markdown("Selenium, Python, Pandas, MySQL, mysql-connector-python, pymysql, Streamlit.")
    slt.subheader(":red[Developed-by:]  Swetha Suresh")

# States and Routes page setting
if web == "📍States and Routes":
    S = slt.selectbox("Lists of States", ["Kerala", "Adhra Pradesh", "West Bengal", "Telungana", "Himachal" "Rajastan", 
                                          "Punjab", "Chandigarh", "Jammu and kashmir", "Uttar Pradesh", "Assam"])
    
    col1,col2=slt.columns(2)
    with col1:
        select_type = slt.radio("Choose bus type", ("sleeper", "semi-sleeper", "others"))
    with col2:
        select_fare = slt.radio("Choose bus fare range", ("50-1000", "1000-2000", "2000 and above"))
    TIME=slt.time_input("select the time")

    # Kerala bus fare filtering
    if S == "Kerala":
        K = slt.selectbox("List of routes",lists_k)

        def type_and_fare(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="Chwe@2106", database="red_bus_details")
            mycursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT  * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}" AND {bus_type_condition}
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)

    # Andhra Pradesh bus fare filtering
    if S=="Adhra Pradesh":
        A=slt.selectbox("list of routes",lists_A)

        def type_and_fare_A(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="Chwe@2106", database="red_bus_details")
            mycursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT  * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{A}" AND {bus_type_condition} 
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_A(select_type, select_fare)
        slt.dataframe(df_result)
          

    # West bengal bus fare filtering
    if S=="West bengal":
        WB=slt.selectbox("list of routes",lists_WB)

        def type_and_fare_WB(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="Chwe@2106", database="red_bus_details")
            mycursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT  * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{WB}" AND {bus_type_condition} 
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_WB(select_type, select_fare)
        slt.dataframe(df_result)

    # Telungana bus fare filtering
    if S=="Telungana":
        T=slt.selectbox("list of routes",lists_T)

        def type_and_fare_T(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="Chwe@2106", database="red_bus_details")
            mycursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT  * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{T}" AND {bus_type_condition} 
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_T(select_type, select_fare)
        slt.dataframe(df_result)

    # Himachal bus fare filtering
    if S=="Himachal":
        H=slt.selectbox("list of routes",lists_H)

        def type_and_fare_H(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="Chwe@2106", database="red_bus_details")
            mycursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT  * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{H}" AND {bus_type_condition} 
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_H(select_type, select_fare)
        slt.dataframe(df_result)
          

    # Rajasthan bus fare filtering       
    if S=="Rajasthan":
        R=slt.selectbox("list of routes",lists_R)

        def type_and_fare_R(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="Chwe@2106", database="red_bus_details")
            mycursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT  * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{R}" AND {bus_type_condition} 
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_R(select_type, select_fare)
        slt.dataframe(df_result)
    
    # Punjab bus fare filtering
    if S=="Punjab":
        P=slt.selectbox("list of rotes",lists_P)

        def type_and_fare_P(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="Chwe@2106", database="red_bus_details")
            mycursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT  * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{P}" AND {bus_type_condition} 
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_P(select_type, select_fare)
        slt.dataframe(df_result)


    # Chandigarh bus fare filtering
    if S=="Chandigarh":
        C=slt.selectbox("list of rotes",lists_C)

        def type_and_fare_C(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="Chwe@2106", database="red_bus_details")
            mycursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT  * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{C}" AND {bus_type_condition} 
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_C(select_type, select_fare)
        slt.dataframe(df_result)

    # Jammu and kashmir fare filtering
    if S=="Jammu and kashmir":
        JK=slt.selectbox("list of rotes",lists_JK)

        def type_and_fare_JK(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="Chwe@2106", database="red_bus_details")
            mycursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT  * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{JK}" AND {bus_type_condition} 
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_JK(select_type, select_fare)
        slt.dataframe(df_result)

    # Uttar pradesh bus fare filtering
    if S=="Uttar pradesh":
        UP=slt.selectbox("list of rotes",lists_UP)

        def type_and_fare_UP(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="Chwe@2106", database="red_bus_details")
            mycursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT  * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{UP}" AND {bus_type_condition} 
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_UP(select_type, select_fare)
        slt.dataframe(df_result)

    # Assam bus fare filtering
    if S=="Assam":
        AS=slt.selectbox("list of rotes",lists_AS)

        def type_and_fare_AS(bus_type, fare_range):
            conn = pymysql.connect(host="localhost", user="root", password="Chwe@2106", database="red_bus_details")
            mycursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT  * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{AS}" AND {bus_type_condition} 
                ORDER BY Price and Start_time DESC
            '''
            mycursor.execute(query)
            out = mycursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_AS(select_type, select_fare)
        slt.dataframe(df_result)
print("Selenium script started")
slt.write("Streamlit app loaded")

