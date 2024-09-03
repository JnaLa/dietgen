pipeline {
    agent any

    environment {
        FLASK_ENV = 'development'
        DOCKER_IMAGE = 'dietgen'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/JnaLa/dietgen'
            }
        }
        stage('Build') {
            steps {
                script {
                    docker.build("${env.DOCKER_IMAGE}")
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    docker.image(DOCKER_IMAGE).inside {
                        sh 'behave tests/features'
                    }
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
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