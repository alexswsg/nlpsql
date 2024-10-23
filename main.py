# Set up and run this Streamlit App
import streamlit as st
import sqlite3


# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit Text to Sql App"
)
# endregion <--------- Streamlit App Configuration --------->


st.title("Streamlit App")

def test_sql():
    connection = sqlite3.connect("aquarium.db")
    print(connection.total_changes)


    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS fish (name TEXT, species TEXT, tank_number INTEGER)")

    rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()

    if len(rows) == 0:
        cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
        cursor.execute("INSERT INTO fish VALUES ('Jamie', 'cuttlefish', 7)")

    rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
    print(rows)

    target_fish_name = "Jamie"
    rows = cursor.execute(
        "SELECT name, species, tank_number FROM fish WHERE name = ?",
        (target_fish_name,),
    ).fetchall()
    print(rows)

    cursor.close()

    return rows

st.write("Start run sql...")
st.divider()

return_rows = test_sql()

st.write(return_rows)

st.divider()
st.write("Completed run sql!!!")

