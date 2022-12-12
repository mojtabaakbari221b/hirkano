pipeline {
    agent any

    environment {
        PROJECT_DIR = '/home/dev/w/projects/hirkano/'
    }

    stages {
        stage('pull from git in development') {
            steps {
                echo "pull from git in development"
                sh """
                    cd ${PROJECT_DIR}
                    git pull
                """
            }
        }
        stage('build in development') {
            steps {
                echo "build project in development"
                sh """
                    cd ${PROJECT_DIR}
                    docker-compose up -d --build
                """
            }
        }
    }
}
