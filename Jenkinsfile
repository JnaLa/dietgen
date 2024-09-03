pipeline {
    agent any

    environment {
        FLASK_ENV = 'development'

    stages {
        stage('Checkout') {
            steps {
                script {
                    echo "Checking out the repository..."
                    //git credentialsId: 'dietgen_token', url: 'https://github.com/JnaLa/dietgen.git'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo "Running tests..."
                    try {
                        sh 'pip install -r requirements.txt'
                        sh 'behave tests/features'
                    } catch (Exception e) {
                        echo "Error during tests: ${e}"
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }
        
    }
    

    post {
        always {
            echo "Cleaning workspace..."
            cleanWs()
        }
    }
}