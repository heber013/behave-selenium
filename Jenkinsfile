#!/usr/bin/env groovy
pipeline {
  agent any

  environment {
    TAG = "demo_${env.BRANCH_NAME}_${env.BUILD_NUMBER}"
  }

  stages {
    stage("Checkout") {
      steps {
        checkout scm
      }
    }

    stage("Cleaning and preparing") {
      steps {
        sh """#!/bin/bash -e
          git clean -dfx
          mkdir reports
        """
      }
    }

    stage('Run Selenium Tests') {
      steps {
        try {
          sh """#!/bin/bash -e
            # run selenium tests
            docker-compose -p ${TAG} up --build -b chrome -g http://selenium_hub:4444/wd/hub --junit --wait_for chromenode:5555
          """
        } finally {
          junit 'reports/*.xml'
          sh """#!/bin/bash
            # Stop and remove the containers
            docker-compose -p ${TAG} down
          """
        }
      }
    }
  }
}