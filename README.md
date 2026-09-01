# Society Events Booker

A web application for managing and registering for university society events.

This project was inspired by my experience as a Marketing Representative for university societies, where promoting and organising society events is an important part of the role. I wanted to build a simple system that could make it easier to display upcoming events and allow students to register for them.

## Features

* View upcoming society events
* Add new society events
* Register for an event using a name and email
* Store event and registration information in a MySQL database
* Connect a Flask backend to a MySQL database
* Simple and clean web interface

## Tech Stack

* **Python**
* **Flask** – backend web framework
* **MySQL** – relational database
* **MySQL Connector/Python** – connects Python to MySQL
* **HTML** – webpage structure
* **CSS** – styling
* **DBeaver** – database management and SQL development
* **Git & GitHub** – version control

## How It Works

The application follows a simple flow:

```text
User
 ↓
HTML Form
 ↓
Flask / Python
 ↓
MySQL Database
 ↓
Stored Event / Registration
```

Flask handles requests from the website and uses MySQL Connector/Python to communicate with the MySQL database.

For example, when a student registers for an event:

```text
Student enters name + email
          ↓
      Flask receives it
          ↓
    SQL INSERT statement
          ↓
   MySQL stores registration
```

## Database

The project uses a MySQL database called `society_events`.

The main tables are:

### Events

Stores information about society events such as:

* Event name
* Date
* Location
* Description
* Capacity

### Registrations

Stores information about students registering for events, including:

* Event ID
* Name
* Email

The registration table connects a student registration to a specific event using the event ID.

## What I Learned

This was my **first project using SQL with Python and connecting an application to a relational database**.

Through this project, I learned how to:

* Create and manage MySQL tables
* Write basic SQL queries such as `SELECT` and `INSERT`
* Use MySQL Connector/Python
* Connect Flask to a MySQL database
* Retrieve database information using Python
* Insert form data into a database
* Use Flask routes and HTML forms together
* Use python-dotenv library to keep database credentials private

One of the main things I learned was how the different parts of a web application communicate with each other rather than working independently.

## Project Structure

```text
society_events_booker/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── static/
│   └── style.css
│
└── templates/
    ├── index.html
    ├── add_event.html
    └── register.html
```

## Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/sr191006/Society_events_booker.git
cd Society_events_booker
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up MySQL

Create a MySQL database called:

```sql
CREATE DATABASE society_events;
```

Then create the required tables using the SQL included in the project.

### 5. Add your database credentials

Create a `.env` file locally containing your MySQL password.

The `.env` file is excluded from GitHub using `.gitignore` so that database credentials are not publicly exposed.

### 6. Run the Flask application

```bash
python3 app.py
```

Then open the link on browser.

## Future Improvements

Some features I would like to add in future versions include:

* Preventing registrations when an event reaches capacity
* Showing the number of available spaces
* Allowing users to cancel registrations
* Adding event search and filtering
* Improving the UI
* Adding user authentication
* Deploying the application online
