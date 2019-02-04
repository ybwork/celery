from celery import Celery

app = Celery('first_step', backend='rpc://', broker='amqp://localhost')


@app.task
def add(x, y):
    return x + y


add.delay(4, 4)
