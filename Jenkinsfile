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
        stage('Print Environment Variables') {
            steps {
                script {
                    echo "DB_HOST: ${env.DB_HOST}"
                    echo "DB_PORT: ${env.DB_PORT}"
                    echo "DB_NAME: ${env.DB_NAME}"
                    echo "DB_USER: ${env.DB_USER}"
                    echo "DB_PASSWORD: ${env.DB_PASSWORD}"
                }
            }
        }
        stage('Run Flask') {
            steps {
                sh 'flask run --host=0.0.0.0 > flask.log 2>&1 &'
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
        stage('Test DB Connection') {
            steps {
                script {
                    def response = sh(script: 'curl -s -o /dev/null -w "%{http_code}" http://localhost:5000/dietgen_db', returnStdout: true).trim()
                    if (response != '200') {
                        error "Database connection test failed with status code ${response}"
                    } else {
                        echo "Database connection test succeeded"
                    }
                }
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