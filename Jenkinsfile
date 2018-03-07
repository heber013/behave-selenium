pipeline {
    agent any
    stages {
        stage('run tests') {
            steps {
                sh 'docker-compose up --build -d'
            }
        stage('clean containers') {
            steps {
                sh 'docker-compose down'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '**/docker_outputs/**'
            junit '**/docker_outputs/**/TESTS-*.xml'
        }
    }
}