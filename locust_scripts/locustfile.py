from locust import HttpLocust, TaskSet, task


class CaesTaskSet(TaskSet):

    @task(10)
    def insert_fake_email(self):
    	self.client.get('/insert_fake_user')

    @task(1)
    def list_fake_emails(self):
    	self.client.get('/list_fake_users')




class CaesTasks(HttpLocust):
    task_set = CaesTaskSet
    min_wait = 5000
    max_wait = 10000
    