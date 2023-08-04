# License-Identifier: MIT-0

import boto3
import random
import os
import json
import id_generator

dynamodb_client = boto3.client('dynamodb')

def lambda_handler(event, context):

  # get name from event body
  body = event["body"]
  print("body = " + body)
  json_body = json.loads(body)
  name = json_body["name"]

  # create a unique id for the database record
  id = id_generator.get_id()

  # introduce a failure at random
  failure_chance = int(os.environ.get('chanceOfFailure'))
  if random.randint(1, 100) < failure_chance:   
    print('A failure occurred.') 
    dynamodb_client.put_item(TableName='DieRollResults',  Item={'id': {'S': str(id)}, 'Result': {'S': 'A failure occured.'}, 'Name': {'S': name}})
    return {
      'statusCode': 500,
      'body': 'Uh oh. Something went wrong!'
    }

  # generate random number between 1 and 6
  die_roll = random.randint(1, 6)
  dynamodb_client.put_item(TableName='DieRollResults', Item={'id': {'S': str(id)}, 'Result': {'S': 'You rolled a ' + str(die_roll) + '!'}, 'Name': {'S': name}})

  return {
    'statusCode': 200,
    'body': 'You rolled a ' + str(die_roll) + '!'
  }
