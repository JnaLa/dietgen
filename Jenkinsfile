pipeline {
    agent {
        docker {
            image 'python:latest' // Use the appropriate image for your app
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    stages {
        //stage('Checkout') {
        //    steps {
        //        git url: 'https://github.com/JnaLa/dietgen.git', credentialsId: 'github_token'
        //    }
        //}
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