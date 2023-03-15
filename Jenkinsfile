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
        stage('build') {
            steps {
                echo 'building the application .l....'
	        sh 'docker build -t santhoshvemaplii/jenkins-docker-hub .'
								
            }
        }
        stage('test') {
            steps {
    
                echo 'testing the applicataion....'
		            sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                test()
            }
        }
        stage('deploy') {
            steps {
                echo 'deploying the application'
// 							  sh 'docker push santhoshvemaplii/jenkins-docker-hub'

							  
            }
        }
    }
	  post {
    always {
      sh 'docker logout'
	    echo "hi"
    }
  }
}
