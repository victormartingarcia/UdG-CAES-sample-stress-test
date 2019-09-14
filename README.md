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
* [http://127.0.0.1:5000/insert_fake_user](http://12.0.0.1:5000/insert_fake_user) - Inserts a user with a fake email into the database
* [http://127.0.0.1:5000/list_fake_users](http://12.0.0.1:5000/list_fake_users) - Print all users on the database

This is the website we are going to stress test using [a python locust script](locust_scripts/locustfile.py) that mimics a user accessing the 3 sections.

Open url address [http://127.0.0.1:8089](http://127.0.0.1:8089) to access locust web interface for running and analyzing load/stress tests