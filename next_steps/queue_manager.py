from celery import Celery

app = Celery('tasks', backend='rpc://', broker='amqp://localhost')

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
