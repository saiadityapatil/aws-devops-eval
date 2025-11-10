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
                sh 'zip function.zip lambda_handler.py'
                sh 'aws s3 cp function.zip s3://test-s3-080/'
            }
        }
        stage('Deploy') {
            steps {
                    sh 'aws lambda update-function-code --function-name test --s3-bucket test-s3-080 --s3-key function.zip'
            }
        }
    }

}

