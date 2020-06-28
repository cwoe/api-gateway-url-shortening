This is URL Shortener using multiple AWS Services (S3, Lambda, API Gateway).

You can find a live version here: [https://cwoellner.com/urlshortener/](https://cwoellner.com/urlshortener/)

![](./design.png)

Cloudformation Template:

Creates the Bucket with Lifecycle Policy and Website hosting enabled.
Creates the Lambda function and the reqired AIM role and policy for accesing the bucket.
Creates the API, connects it with the the Lambda function via Lambda Proxy, adds the required AMI roles and policies and deploys the API.

TODO:
  - Add CORS for API Gateway
  - Throttle API Gateway
  - Find a way to upload the lambda code within the template

The live version has these issues fixed via manual intervention.
