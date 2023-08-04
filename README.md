# Build-It Roll Die Application

This is a reference architecture for the Build-It application. This application uses AWS SAM as infrastructure as code. The application architecture is composed of Amazon API Gateway, AWS Lambda, and Amazon DynamoDB. When an HTTP POST request is made to the Amazon API Gateway endpoint, the AWS Lambda function is invoked and inserts an item into the Amazon DynamoDB table.

## Requirements

* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone git@github.com:dancfox/build-it.git
    ```
1. Change directory to the pattern directory:
    ```
    cd build-it
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yaml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the API endpoint URL you will use for testing.

## Testing

- Download and install Postman.
- Configure a POST request to the API Gateway endpoint printed in the CloudFormation outputs. 
- Send a request with an empty body.  You should receive and `"Invalid request body"` error.
- Send a request with the following JSON as the raw body: `{"name":"dan"}`. You should receive a die roll between 1 and 6.
- Send several more die rolls. The application has a 25% chance of returning an error with each die roll.
- Now go to DynamoDB and find the `DieRollResults` table. The table should be populated with a history of your die rolls.

## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
## License
MIT-0
