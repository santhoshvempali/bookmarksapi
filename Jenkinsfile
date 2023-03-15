def test(){
	ans=2+2;
	echo "${ans}"
}
pipeline {
  agent any
  options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
  }
  environment {
    DOCKERHUB_CREDENTIALS = credentials('dockerhub')
  }
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t santhoshvemaplii/jenkins-docker-hub .'
      }
    }
    stage('Login') {
      steps {
        sh ' docker login -u santhoshvemaplii --password 8500436311'
	echo "hello"
      }
    }
    stage('Push') {
      steps {
        sh 'docker push santhoshvemaplii/jenkins-docker-hub'
        echo "test"
      }
    }
  }
  post {
    always {
      sh 'docker logout'
    }
  }
}
