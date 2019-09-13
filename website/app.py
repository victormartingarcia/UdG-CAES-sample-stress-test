from flask import Flask, request
from faker import Faker
fake = Faker()

app = Flask(__name__)

@app.route("/")
def home():
    return "This is a test web application for CAES stress test demonstration"

@app.route("/insert_fake_email")
def insert_fake_email():
    return "TODO:  insert email: {}".format(fake.email())

@app.route("/list_fake_emails")
def list_fake_emails():
    return "TODO: list all emails"

if __name__ == '__main__':
    app.run()