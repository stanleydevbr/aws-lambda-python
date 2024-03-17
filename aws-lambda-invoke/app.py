from chalice import Chalice

app = Chalice(app_name='aws-lambda-invoke')


@app.lambda_function(name="invoke")
def invoke(event, context):
    print(event['nome'])
    print(event['idade'])
    return True

