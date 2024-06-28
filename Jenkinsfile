pipeline {
    agent any

    stages {
        stage('pylint') {
            steps {
                sh 'pylint main/fun_to_test.py'
            }
        }
        stage('pytest') {
            steps {
                sh 'pytest -v main/main.py'
            }
        }
    }
}