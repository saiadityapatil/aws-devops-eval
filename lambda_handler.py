import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table_name = 'Emp_Master'

def lambda_handler(event, context):
    table = dynamodb.Table(table_name)
    operation = event['httpMethod']
    payload = event['payload']
    if operation == 'POST':
        response = table.put_item(Item=payload)
        return {'statusCode': 200, 'body': 'Item added successfully'}
    elif operation == 'GET':
        response = table.get_item(Key=payload)
        return {'statusCode': 200, 'body': response['Item']}
    else:
        return {'statusCode': 400, 'body': 'Invalid operation'}

print("hello")