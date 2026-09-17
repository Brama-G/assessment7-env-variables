pipeline {
    agent any

    environment {
        APP_NAME    = 'OnlineExamSystem'
        APP_VERSION = '1.0.0'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/<your-username>/project5-env-variables.git'
            }
        }

        stage('Show App Info') {
            steps {
                echo "Building ${env.APP_NAME}, version ${env.APP_VERSION}"
            }
        }

        stage('Build') {
            steps {
                bat 'python -m py_compile exam_system.py'
                echo "${env.APP_NAME} version ${env.APP_VERSION} compiled successfully."
            }
        }

        stage('Version Check') {
            steps {
                bat 'python version_check.py'
            }
        }
    }
}
