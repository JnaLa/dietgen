pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'korho185/dietgen'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    echo "Checking out the repository..."
                    
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image..."
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        //stage('Push Docker Image') {
        //    steps {
        //        script {
        //            echo "Pushing Docker image to Docker Hub..."
        //            sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
        //            sh 'docker push $DOCKER_IMAGE'
        //        }
        //    }
        //}

        //stage('Run Tests') {
        //    agent {
        //        docker {
        //            image 'your-dockerhub-username/python-app:latest'
        //            args '-v /var/run/docker.sock:/var/run/docker.sock'
        //        }
        //    }
        //    steps {
        //        script {
        //            echo "Running tests..."
        //            sh 'pip install -r requirements.txt'
        //            sh 'pytest'
        //        }
        //    }
        //}
    }

    post {
        always {
            echo "Cleaning up workspace..."
            deleteDir()
        }
    }
}