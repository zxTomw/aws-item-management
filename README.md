# aws-item-management
This is a serverless backend implemented with python and deployed with AWS applications including Lambda, DynamoDB, CloudWatch and API Gateway. 

## Usage

To use this application:

- Deploy it to your AWS environment with the files provided in this repository.
- Access your API via the provided endpoint URL.
- Use the API to perform the supported operations: GET all items, GET an item by ID, and POST to add a new item.

## Access APIs

API endpoint: [https://s4c5y7evfl.execute-api.us-east-2.amazonaws.com/deploy/itemmanagement/](https://s4c5y7evfl.execute-api.us-east-2.amazonaws.com/deploy/itemmanagement/)

### GET
Use get request directly, it will respond with an array of all the items

### GET with ID
Attached the ID to the end of the provided API endpoint. Will respond the item with the given ID. Gives empty array if item with given ID does not exist. 

### POST
In the request body, include the non-empty ID, name and description of the item you want to add. Adds a new item to the database, or if an item with the same ID exists, replaces this item with new name and description. 