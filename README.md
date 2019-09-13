# UdG-CAES-sample-stress-test
A demonstration stress test using [locust python load testing tool](https://locust.io).

## Usage

Make sure you have the required dependencies installed on your system:

* [Docker](https://docs.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)

Clone this repository

```
git clone git@github.com:victormartingarcia/UdG-CAES-sample-stress-test.git
```

Go to base repo folder and run the docker containers

```
cd Udg-CAES-sample-stress-test
docker-compose up
```

That should have set up a toy website with 3 sections:

* [http://127.0.0.1:5000](http://12.0.0.1:5000) - Homepage with a fancy welcome text
* [http://127.0.0.1:5000/insert_fake_email](http://12.0.0.1:5000/insert_fake_email) - Inserts a fake email to the database
* [http://127.0.0.1:5000/list_fake_emails](http://12.0.0.1:5000/list_fake_emails) - Print all fake emails on the database

This is the website we are going to stress test using [a locust script]() that mimics a user accessing the 3 sections.

Open url address [http://127.0.0.1:8089](http://127.0.0.1:8089) to access locust web interface for launching and reviewing load tests