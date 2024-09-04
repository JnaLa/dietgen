pipeline {
    agent {
        docker {
            image "korho185/dietgen:latest" // Use the appropriate image for your app
            args "-v /var/run/docker.sock:/var/run/docker.sock"
        }
    }
    options {
        timeout(time: 30, unit: 'MINUTES') // Add a timeout for the entire pipeline
    }
    stages {
        stage('Build') {
            steps {
                script {
                    try {
                        sh 'pip install -r requirements.txt'
                    } catch (Exception e) {
                        error "Build failed: ${e.getMessage()}"
                    }
                }
            }
        }
        stage('Print Environment Variables') {
            steps {
                script {
                    withEnv(["DB_HOST=${env.DB_HOST}", "DB_PORT=${env.DB_PORT}", "DB_NAME=${env.DB_NAME}"]) {
                        echo "DB_HOST: ${env.DB_HOST}"
                        echo "DB_PORT: ${env.DB_PORT}"
                        echo "DB_NAME: ${env.DB_NAME}"
                    }
                }
            }
        }
        stage('Run Flask') {
            steps {
                script {
                    try {
                        sh 'flask run --host=0.0.0.0 > flask.log 2>&1 &'
                        // Wait for the Flask server to be up and running
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
                    } catch (Exception e) {
                        error "Run Flask failed: ${e.getMessage()}"
                    } finally {
                        sh 'cat flask.log'
                    }
                }
            }
        }
        stage('Test DB Connection') {
            steps {
                script {
                    try {
                        def response = sh(script: 'curl -s -o /dev/null -w "%{http_code}" 172.19.0.3:5000/db_test', returnStdout: true).trim()
                        if (response != '200') {
                            error "Database connection test failed with status code ${response}"
                        } else {
                            echo "Database connection test succeeded"
                        }
                    } catch (Exception e) {
                        error "Test DB Connection failed: ${e.getMessage()}"
                    }
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    try {
                        sh 'behave ./tests/api_tests/'
                    } catch (Exception e) {
                        error "Test failed: ${e.getMessage()}"
                    }
                }
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