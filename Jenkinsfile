pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/saiadityapatil/aws-devops-eval.git'
            }
        }
        stage('Zip') {
                steps {
                    withAWS(region: 'ap-south-1',credentials: 'aws-cred') {
                        script {
                            sh 'zip function.zip lambda_function.py'
                            sh 'aws s3 ls'
                            sh 'aws s3 cp function.zip s3://<s3-bucket-name>/'
                        }
                    }
                }
        }
        stage('Deploy') {
                steps {
                    withAWS(region: 'ap-south-1', credentials: 'aws-cred') { // Use the ID you defined
                        script {
                            def functionExists = sh(script: "aws lambda get-function --function-name MyLambdaFunction > /dev/null 2>&1", returnStatus: true)

                            if (functionExists == 0) {
                                echo "Function exists. Updating..."
                                sh "aws lambda update-function-code --function-name test --s3-bucket <s3-bucket-name> --s3-key function.zip"
                            } else {
                                echo "Function does not exist. Creating..."
                                sh """
                                    aws lambda create-function \
                                        --function-name MyLambdaFunction \
                                        --runtime python3.9 \
                                        --role <role-with-execution-and-dynamodb-access> \
                                        --handler lambda_function.lambda_handler \
                                        --s3-bucket <s3-bucket-name> 
                                        --s3-key function.zip
                                """
                            }
                    }
                }
        }
    }

}








