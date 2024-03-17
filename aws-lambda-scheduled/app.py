from chalice import Chalice

app = Chalice(app_name='aws-lambda-scheduled')


@app.schedule("cron(0 10 ? * * *)")
def scheduled(event):
    print("Scheduled event: %s" % event.to_dict())
    return True

