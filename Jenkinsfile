pipeline {
    agent any

    stages {
        stage('pylint') {
            steps {
                sh 'pylint main/'
            }
        }
        stage('pytest') {
            steps {
                sh 'pytest -v main/main.py'
            }
        }
    }
}