from flask import Flask, request
import psycopg2
import psycopg2.extras
from datetime import datetime
import time
from faker import Faker
fake = Faker()

app = Flask(__name__)


def get_database_connection():
    connection = psycopg2.connect(
        user="caes_username",
        password="caes_password",
        host="database",
        port="5432",
        database="caes_stress_test"
    )
        
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    return connection, cursor

def utc2local (utc):
    epoch = time.mktime(utc.timetuple())
    offset = datetime.fromtimestamp (epoch) - datetime.utcfromtimestamp (epoch)
    return utc + offset

@app.route("/")
def home():
    return """
        <h2>This is a test web application for CAES stress test demonstration</h2>
        <br/>
        <br/>
        <ul>
            <li><h3><a href="/insert_fake_user">Insert a fake user</a></h3></li>
            <li><h3><a href="/list_fake_users">List fake users</a></h3></li>
        </ul>
    """

@app.route("/insert_fake_user")
def insert_fake_user():
    full_name = fake.name()
    email = fake.email()

    connection, cursor = get_database_connection()
    
    cursor.execute("""
        INSERT INTO users (full_name, email, created_on) 
        VALUES ('{}', '{}', current_timestamp);

    """.format(full_name, email))
    connection.commit()

    if(connection):
        cursor.close()
        connection.close()

    return "Inserted user with name: {} email: {}".format(full_name, email)

@app.route("/list_fake_users")
def list_fake_users():

    connection, cursor = get_database_connection()
    
    cursor.execute("""
        SELECT user_id, full_name, email, created_on
        FROM users; 
    """)
    users = cursor.fetchall() 

    response_html = """
    <h2>CAES listing """ + str(len(users)) + """ fake users</h2>

    <table>
        <tr>
            <th style='border: 1px solid #999;'>User ID</th>
            <th style='border: 1px solid #999;'>Full Name</th>
            <th style='border: 1px solid #999;'>E-mail</th>
            <th style='border: 1px solid #999;'>Date Created</th>
        </tr>    
    """
    
    for user in users:
        response_html += "<tr>"
        response_html += "  <td style='border: 1px solid #999;'>" + str(user["user_id"]) + "</td>"
        response_html += "  <td style='border: 1px solid #999;'>" + user["full_name"] + "</td>"
        response_html += "  <td style='border: 1px solid #999;'>" + user["email"] + "</td>"
        response_html += "  <td style='border: 1px solid #999;'>" + utc2local(user["created_on"]).strftime("%d/%m/%Y, %H:%M:%S") + "</td>"
        response_html += "</tr>"

    if(connection):
        cursor.close()
        connection.close()

    response_html += "</table>"

    return response_html

if __name__ == '__main__':
    app.run()