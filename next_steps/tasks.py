from __future__ import absolute_import, unicode_literals
from queue_manager import app


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)


class User():
    def __init__(self, name):
        self.name = name







