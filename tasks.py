from celery import Celery

app = Celery('tasks', backend='redis://localhost', broker='redis://')
#app = Celery('task', broker='redis://guest@localhost//', backend='redis://localhost')
#app = Celery('tasks', broker='redis://localhost:6379', backend='redis://localhost:6379')

@app.task
def add(x, y):
    while x <= y:
        x += 1
    return x
