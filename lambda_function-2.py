import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('items')

def lambda_handler(event, context):
    if event['httpMethod'] == 'GET':
        print("recieved GET request")
        params = event.get('pathParameters')
        if params:
            item_id = params.get('id')
            response = table.get_item(Key={'ID': item_id})
            if response:
                print("item exists")
                print("fetched item with id " + str(item_id))
        else:
            response = table.scan()
            print("fetched list of all items")
        return {
            'statusCode': 200,
            'body': json.dumps(response.get('Item', response.get('Items')))
        }
    elif event['httpMethod'] == 'POST':
        print("recived POST request")
        data = json.loads(event['body'])
        item_id = data.get('ID')
        item_name = data.get('name')
        item_description = data.get('description')
        log = str("recieved request: \n" + str(data))
        print(log)
        if (None in (item_id, item_name, item_description)): # missing field(s)
            return {
                'statusCode': 400,
                'body': json.dumps('Missing field(s). Requires ID, Name and Description.')
            }
        item = {"ID": str(item_id), "name": str(item_name), "description": str(item_description)}
        print("item is valid")
        response = table.put_item(Item=item)
        print("item stored to database")
        return {
            'statusCode': 201,
            'body': json.dumps('Item created successfully')
        }
    else:
        print("recieved"+str(event['httpMethod'])+"method")
        return {
            'statusCode': 400,
            'body': json.dumps('Unsupported HTTP method')
        }
