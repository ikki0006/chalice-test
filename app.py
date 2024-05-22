from chalice import Chalice

app = Chalice(app_name='helloworld')

@app.schedule("rate(1 hour)")
def scheduled_event1(event):
    print("Scheduled event: %s" % event.to_dict())
    return {"hello": "world"}

@app.schedule("rate(2 hour)")
def scheduled_event2(event):
    print("Scheduled event: %s" % event.to_dict())
    return {"hello": "world2"}

@app.route('/')
def index():
    print('logだよ')
    return {'hello': 'world'}