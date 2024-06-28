pipeline {
    agent any

    stages {
        stage('Static analysis') {
            steps {
                sh 'pylint main/'
            }
        }
        stage('Pytest stage') {
            steps {
                sh 'pytest -v main/main.py'
            }
        }
    }
}