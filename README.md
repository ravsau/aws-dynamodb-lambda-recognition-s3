# aws-dynamodb-lambda-recognition-s3

Code for a simple  lambda function which stores the labels for in image in DynamoDB table.

## AWS services used
1) AWS Lambda
2) Amazon S3: You have to change the bucket name in the function
3) DynamoDB
4) Amazon Rekognition: This is where the magic happens. Rekognition is an Image recognition service which provides a simple API that let's us find labels(car, person), detect faces, detect celebrities etc. We use this service to find out the items/labels in an image.



 
