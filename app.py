from flask import Flask, render_template, request
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost", #my own computer
        user="root",
        password=os.getenv("MYSQL_PASSWORD"),
        database="society_events"
    )
    #connects to MySQL society_events database, which contains events and registration tables.
    return connection


#homepage- show all events
@app.route("/")
def home():

    connection = get_db_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM events")

    events = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("index.html", events=events)


#add a new event
@app.route("/add-event", methods=["GET", "POST"])
def add_event():

    if request.method == "POST":

        name = request.form["name"]
        event_date = request.form["event_date"]
        location = request.form["location"]
        description = request.form["description"]
        capacity = request.form["capacity"]

        connection = get_db_connection()

        cursor = connection.cursor()

        sql = """
            INSERT INTO events
            (name, event_date, location, description, capacity)
            VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            name,
            event_date,
            location,
            description,
            capacity
        )

        cursor.execute(sql, values)

        connection.commit()

        cursor.close()
        connection.close()

    return render_template("add_event.html")


@app.route("/register/<int:event_id>", methods=["GET", "POST"])
def register(event_id):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute( #run this SQL command
        "SELECT * FROM events WHERE id = %s",
        (event_id,)
    )

    event = cursor.fetchone()

    if request.method == "POST": #if they have submitted the form do the folowing:

        name = request.form["name"]
        email = request.form["email"]

        cursor.execute(
            """
            INSERT INTO registrations (event_id, name, email)
            VALUES (%s, %s, %s)
            """,
            (event_id, name, email)
        )

        connection.commit() #save database changes

        cursor.close()
        connection.close()

        return "Registration successful!"

    cursor.close()
    connection.close()

    return render_template("register.html", event=event)


if __name__ == "__main__":
    app.run(debug=True)