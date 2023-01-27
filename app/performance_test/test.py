from locust import HttpUser, TaskSet, task

class UserBehavior(TaskSet):
    @task
    def get_deals(self):
        self.client.post("/transaction/deals?page=1&size=50")

    @task
    def get_trans(self):
        self.client.post("/transaction/transactions?page=1&size=50")

    @task
    def get_trans_details(self):
        self.client.post("/details", data={
            "ids": [1],
            "transaction_type": "TR"
        })

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 1000
    max_wait = 5000