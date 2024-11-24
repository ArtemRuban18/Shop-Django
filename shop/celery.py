from celery import Celery

app = Celery('shop', broker='redis://redis:6379/0')
app.conf.result_backend = 'redis://redis:6379/0'