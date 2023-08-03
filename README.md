# Build-It Roll Die Application

This is a reference architecture for the Build-It application. This application uses AWS SAM as infrastructure as code. The application architecture is composed of Amazon API Gateway, AWS Lambda, and Amazon DynamoDB. When an HTTP POST request is made to the Amazon API Gateway endpoint, the AWS Lambda function is invoked and inserts an item into the Amazon DynamoDB table.

## Requirements

* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone git@ssh.gitlab.aws.dev:dfxamzn/build-it.git
    ```
1. Change directory to the pattern directory:
    ```
    cd apigw-lambda-dynamodb
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

When an HTTP POST request is sent to the Amazon API Gateway endpoint, the AWS Lambda function is invoked and inserts an item into the Amazon DynamoDB table.

## Testing

After deployment, use the AWS Management Console (explained below) to test this pattern by sending an HTTP POST request to the Amazon API Gateway endpoint (found in the CloudFormation console Stacks Outputs tab) to confirm an item is added to the Amazon DynamoDB table. Alternatively, a command line shell or another application can be used to send the HTTP POST request.

Using the Amazon API Gateway console, select the API, Resources, and POST method execution. Click Test on the Client box and the Test button without a request body. The request should return a response message 'You have rolled X!'. If any errors occur, this view also shows logs from the invocation for troubleshooting. Navigate to the Amazon DynamoDB console to verify the item was added into the table.

## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
