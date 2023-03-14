pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                echo 'building the application .....'
            }
        }
        stage('test') {
            steps {
                def test():return 2+2;
                echo 'testing the applicataion....'
                echo test()
            }
        }
        stage('deploy') {
            steps {
                echo 'deploying the application'
            }
        }
    }
}
