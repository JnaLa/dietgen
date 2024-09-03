pipeline {
    agent {
        docker {
            image 'korho185/dietgen:latest' // Use the appropriate image for your app
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }/
        stage('Run Flask') {
            steps {
                sh 'flask run --host=0.0.0.0 &'
                // Wait for the Flask server to be up and running
                sh 'while ! nc -z localhost 5000; do sleep 1; done'
            }
        }
        stage('Test') {
            steps {
                sh 'behave ./tests/api_tests/'
            }
        }
    }
    post {
        always {
            echo "Cleaning up workspace..."
            deleteDir()
        }
    }
}