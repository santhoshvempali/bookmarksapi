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
    stage('Login') {
      steps {
        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
	echo "hello"
      }
    }
  stages {
    stage('Build') {
      steps {
        sh 'docker pull santhoshvemaplii/microshop-orders'
      }
    }


  }
  post {
    always {
      sh 'docker logout'
    }
  }
}
