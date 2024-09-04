pipeline {
    agent {
        docker {
            image 'korho185/dietgen:latest' // Use the appropriate image for your app
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    environment {
        DB_HOST = 'host.docker.internal'
        DB_PORT = '5432'
        DB_NAME = 'dietgen_db'
        DB_USER = credentials('postgres-username') // Replace with your Jenkins credential ID for the username
        DB_PASSWORD = credentials('postgres-password') // Replace with your Jenkins credential ID for the password
    }
    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Flask') {
            steps {
                sh 'flask run > flask.log 2>&1 &'
                // Wait for the Flask server to be up and running
                script {
                    def maxRetries = 30
                    def retries = 0
                    while (retries < maxRetries) {
                        try {
                            sh 'curl -s http://localhost:5000 > /dev/null'
                            echo "Flask server is up and running"
                            break
                        } catch (Exception e) {
                            echo "Waiting for Flask server to start..."
                            sleep 5
                            retries++
                        }
                    }
                    if (retries == maxRetries) {
                        error "Flask server did not start in time"
                    }
                }
                sh 'cat flask.log'
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