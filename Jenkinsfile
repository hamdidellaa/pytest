pipeline {
    agent any
    stages {
        stage('Install requirements') {
              when {
              //  not {
                    anyOf {
                        branch 'develop';
                        branch 'master'
                   //     branch 'staging'
                    }
              //  }
             }
            steps {
                sh 'pwd' 
              //  sh 'pip install -r requirements.txt'  
              }
        }
       stage('Unit tests') {
                 when {
                        branch 'develop';
             }
            steps {
                sh ' python -m pytest --verbose --junit-xml test-reports/results.xml' 
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