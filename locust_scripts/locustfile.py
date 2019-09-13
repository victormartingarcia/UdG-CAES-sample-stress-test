from locust import HttpLocust, TaskSet, task


class BasicTaskSet(TaskSet):

    @task(2)
    def root(self):
        self.client.get('/')

    @task(1)
    def insert_fake_email(self):
    	self.client.get('/insert_fake_email')

    @task(1)
    def list_fake_emails(self):
    	self.client.get('/list_fake_emails')




class BasicTasks(HttpLocust):
    task_set = BasicTaskSet
    min_wait = 5000
    max_wait = 10000
    