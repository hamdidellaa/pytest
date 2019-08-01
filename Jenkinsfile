pipeline {
    agent any
    triggers {
        cron('* * * * *')
    }
    stages {
        stage('Code Pull') {
            steps {
                git  url: 'https://github.com/hamdidellaa/pytest.git'
              }
        }
        stage('Install requirements') {
            steps {
                bat 'pip install -r requirements.txt'  
              }
        }
        stage('Unit tests') {
            steps {
               // bat ' python -m pytest --verbose --junit-xml test-reports/results.xml' 
            }
            post {
                always {
                    // Archive unit tests for the future
                    junit allowEmptyResults: true, testResults: 'test-reports/results.xml'
                }
            }
        }

    }
     post {
        failure {
            emailext body: """<p>FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
                         <p>Check console output at <a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a></p>""", subject: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'", to: 'hamdi.dellaa@arabesque.com'
        }
        success {
            emailext body: """<p>SECCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
                         <p>Check console output at <a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a></p>""", subject: "SECCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'", to: 'hamdi.dellaa@arabesque.com'
        }
    }
}