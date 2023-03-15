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
        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
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
