pipeline {
    agent any

    environment {
        APP_NAME    = 'OnlineExamSystem'
        APP_VERSION = '2.0.0'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Brama-G/assessment7-env-variables.git'
            }
        }

        stage('Show App Info') {
            steps {
                echo "Building ${env.APP_NAME}, version ${env.APP_VERSION}"
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m py_compile exam_system.py'
                echo "${env.APP_NAME} version ${env.APP_VERSION} compiled successfully."
            }
        }

        stage('Version Check') {
            steps {
                sh 'python3 version_check.py'
            }
        }
    }
}
