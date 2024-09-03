pipeline {
    agent {
        any {
            image 'python:3.9' // Use the appropriate image for your app
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest tests/'
            }
        }
    }
}