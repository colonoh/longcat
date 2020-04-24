import json

from locust import HttpLocust, TaskSet, between

def create(l):
    payload = {'url':'http://0.0.0.0:8000/redirect/dummy'}
    headers = {'content-type': 'application/json'}
    r = l.client.post("/api/v1/create/", data=json.dumps(payload), headers=headers)

def list(l):
    l.client.get("/api/v1/slugs")

# def profile(l):
#     l.client.get("/profile")

class UserBehavior(TaskSet):
    tasks = [create]

    # def on_start(self):
    #     login(self)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5.0, 9.0)
