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
                sh 'aws s3 cp function.zip s3://aws-devops-evaluation/function.zip'
            }
        }
        stage('Deploy') {
            steps {
                    sh 'aws lambda update-function-code --function-name  EvaluationLambda --s3-bucket aws-devops-evaluation --s3-key function.zip'
            }
        }
    }
}