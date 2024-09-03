pipeline {
    agent {
        docker {
            image 'python:3.8' // Use a Python Docker image with pip installed
            args '-u root' // Run as root to install dependencies
        }
    }

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