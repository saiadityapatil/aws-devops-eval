import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Emp_Master')

def lambda_handler(event, context):
    if event['requestContext']['http']['method'] == 'POST':
        table.put_item(Item=json.loads(event['body']))
        return {
            'statusCode': 200,
            'body': json.dumps('Record added!! Great!!!!!')
        }
    elif event['requestContext']['http']['method'] == 'GET':
        response = table.get_item(Key={'Emp_Id': event['queryStringParameters']['emp_id']})
        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])
        }





