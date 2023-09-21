from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//',backend="rpc://")
# scelery -A tasks worker --loglevel=INFO -P solo
@app.task
def add(x, y):
    return x + y

@app.task
def hello():
    print('Hello')
    return "hello"