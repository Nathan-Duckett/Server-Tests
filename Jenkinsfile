pipeline {
    agent any
    stages {
        stage('test') {
            steps {
                sh "python3 -m unittest tests/reverse_proxy_tests.py"
            }
        }
    }
}
