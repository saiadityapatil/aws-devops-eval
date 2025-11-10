pipeline {
    agent any

    environment {
        REGION = "ap-south-1"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/saiadityapatil/aws-devops-eval.git'
            }
        }
        stage('Zip') {
                steps {
                    withAWS(region: 'us-east-1', credentials: 'my-aws-credentials') { // Use the ID you defined
                        script {
                            // Example: List S3 buckets using AWS CLI
                            sh 'zip function.zip lambda_handler.py'
                            sh 'aws s3 ls'
                            sh 'aws s3 cp function.zip s3://test-s3-080/'
                        }
                    }
                }
        }
        stage('Deploy') {
            withAWS(credentials: 'aws-cred') {
                steps {
                    withAWS(region: 'us-east-1', credentials: 'my-aws-credentials') { // Use the ID you defined
                        script {
                            sh 'aws lambda update-function-code --function-name test --s3-bucket test-s3-080 --s3-key function.zip'
                        }
                    }
                }
            }
        }
    }

}




