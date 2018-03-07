pipeline {
    agent any
    environment {
    TAG = "demo_${env.BRANCH_NAME}_${env.BUILD_NUMBER}"
    }
    stages {
        stage('build') {
            steps {
                sh 'docker-compose build ui_tests:${TAG}'
            }
        }
        stage('run tests') {
            steps {
                sh 'docker-compose run ui_tests:${TAG}'
            }
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