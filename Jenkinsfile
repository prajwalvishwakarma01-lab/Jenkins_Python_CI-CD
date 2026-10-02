pipeline {
  agent any

  environment {
    IMAGE_NAME = 'flask-demo'
    CONTAINER_NAME = 'flask-app'
  }

  stages {
    stage('Checkout') {
      steps {
        echo 'Source code checkout completed'
      }
    }
    stage('Check Python') {
      steps {
          bat 'where python'
          bat 'python --version'
      }
    }

    stage('Build') {
      steps {
        echo 'Building Docker Image'
        bat 'docker build -t %IMAGE_NAME% .'
      }
    }

    stage('Install Dependencies') {
      steps {
        echo 'Installing Dependencies'
        bat 'pyton -m pip install -r requirements.txt'
      }
    }

    stage('Run Tests') {
      steps {
        echo 'Running Pytest'
        bat 'python -m pytest'
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying Application'
        bat 'docker stop %CONTAINER_NAME% || exit 0'
        bat 'docker rm %CONTAINER_NAME% || exit 0'

        bat '''
          docker run -d ^
          --name %CONTAINER_NAME% ^
          -p 5000:5000 ^
          %IMAGE_NAME%
        '''
      }
    }
  }

  post {
    success {
      echo 'Deployment Successful'
    }

    failure {
      echo 'Pipeline Failed'
    }
  }
}