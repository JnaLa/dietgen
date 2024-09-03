pipeline {
    agent any

    environment {
        FLASK_ENV = 'development'
        DOCKER_IMAGE = 'dietgen'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    echo "Checking out the repository..."
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    echo "Building Docker image..."
                    docker.build("${env.DOCKER_IMAGE}")
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo "Running tests..."
                    docker.image(DOCKER_IMAGE).inside {
                        sh 'behave tests/features'
                    }
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    echo "Deploying application..."
                    docker.image(DOCKER_IMAGE).inside {
                        sh 'docker run -d -p 5000:5000 dietgen'
                    }
                }
            }
        }
        
    }
    

    post {
        always {
            cleanWs()
        }
    }
}