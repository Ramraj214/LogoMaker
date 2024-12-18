pipeline {
    agent any

    parameters {
        string(name: 'GIT_BRANCH', defaultValue: 'main', description: 'Branch to build')
        string(name: 'DOCKER_IMAGE_TAG', defaultValue: 'latest', description: 'Docker image tag')
    }

    environment {
        FRONTEND_IMAGE = "frontend-app"
        BACKEND_IMAGE = "backend-app"
        FRONTEND_CONTAINER = "frontend-app"
        BACKEND_CONTAINER = "backend-app"
        FRONTEND_PORT = '3000'
        BACKEND_PORT = '8000'
    }
    stages {
        stage('Clear Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout Code') {
            steps {
                git branch: params.GIT_BRANCH, changelog: false, poll: false, url: 'https://github.com/Ramraj214/LogoMaker'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh """
                        docker build -t ${FRONTEND_IMAGE}:${params.DOCKER_IMAGE_TAG} .
                        docker build -t ${BACKEND_IMAGE}:${params.DOCKER_IMAGE_TAG} .  
                    """
                }
            }
        }

        stage('Clean Up Old Containers') {
            steps {
                script {
                    sh """
                        docker rm -f ${FRONTEND_CONTAINER} || true
                        docker rm -f ${BACKEND_CONTAINER} || true
                    """
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh """
                        docker run -d --name ${FRONTEND_CONTAINER} -p ${FRONTEND_PORT}:${FRONTEND_PORT} ${DOCKER_IMAGE_NAME}:${params.DOCKER_IMAGE_TAG}
                        docker run -d --name ${BACKEND_CONTAINER} -p ${BACKEND_PORT}:${BACKEND_PORT} ${DOCKER_IMAGE_NAME}:${params.DOCKER_IMAGE_TAG}
                    """
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed! Please check the logs.'
            mail to: 'ramrajnagapure54321@@gmail.com',
                 subject: "Jenkins Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Check the Jenkins logs for job: ${env.BUILD_URL}"
        }
    }
}
