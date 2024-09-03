pipeline {
    agent any

    environment {
        FLASK_ENV = 'development'
        DOCKER_IMAGE = 'dietgen'
        DOCKER_HOST = 'unix:///var/run/docker.sock' // Use Unix socket for Docker communication
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
        stage('Build') {
            steps {
                script {
                    echo "Building Docker image..."
                    try {
                        sh 'docker --version'
                        docker.build("${env.DOCKER_IMAGE}")
                    } catch (Exception e) {
                        echo "Error during Docker build: ${e}"
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo "Running tests..."
                    try {
                        docker.image("${env.DOCKER_IMAGE}").inside {
                            sh 'behave tests/features'
                        }
                    } catch (Exception e) {
                        echo "Error during tests: ${e}"
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    echo "Deploying application..."
                    try {
                        docker.image("${env.DOCKER_IMAGE}").inside {
                            sh 'docker run -d -p 5000:5000 dietgen'
                        }
                    } catch (Exception e) {
                        echo "Error during deployment: ${e}"
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