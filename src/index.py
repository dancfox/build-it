# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import boto3
import random
import os
import uuid

dynamodb_client = boto3.client('dynamodb')

def lambda_handler(event, context):

  id = uuid.uuid1()

  # create a failure
  failure_chance = int(os.environ.get('chanceOfFailure'))
  if random.randint(0, 100) < failure_chance:   
    print('Failure!') 
    dynamodb_client.put_item(TableName='DieRollResults',  Item={'id': {'S': str(id)}, 'Result': {'S': 'Failure!'}})
    return {
        'statusCode': 500,
        'body': 'Something went wrong!'
        }

  # generate random number between 1 and 6
  die_roll = random.randint(1, 6)
  dynamodb_client.put_item(TableName='DieRollResults', Item={'id': {'S': str(id)}, 'Result': {'S': 'You rolled a ' + str(die_roll) + '!'}})

  return {
      'statusCode': 200,
      'body': 'You rolled a ' + str(die_roll) + '!'
  }
