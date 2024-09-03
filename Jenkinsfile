pipeline {
    agent {
        dockerContainer {
            image 'python-java:3.8' // Use a Python Docker image with pip installed
            //args '-u root' // Run as root to install dependencies
        }
    }

    environment {
        FLASK_ENV = 'development'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    echo "Checking out the repository..."
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo "Installing dependencies..."
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo "Running tests..."
                    try {
                        sh 'behave tests/features'
                    } catch (Exception e) {
                        echo "Error during tests: ${e}"
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }

        stage('Docker Test') {
            steps {
                script {
                    echo "Testing Docker integration..."
                    sh 'docker run hello-world'
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