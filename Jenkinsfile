pipeline {
    agent any
    stages {
        stage('Install requirements') {
              steps{
                  
                    sh ' pip3 install -r requirements.txt '
              /* script {
                    if (env.BRANCH_NAME.startsWith('release') ) {
                        echo 'this step created for release branch'
                    } else if(env.BRANCH_NAME.startsWith('feature')) {
                       echo 'this step created for feature branch'
                    }
                 }*/
              }
        }
       stage('Unit tests') {
            when {
                expression { env.BRANCH_NAME == 'develop'}
            }
            steps {
              sh ' python3 -m pytest --verbose --junit-xml test-reports/results.xml' 
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
              script {
                    if (env.BRANCH_NAME.startsWith('release') || env.BRANCH_NAME.startsWith('feature')   ) {
                          emailext body: """<p>SECCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
                         <p>Check console output at <a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a></p>
                         <p> This Branch is ready to merge </p>
                         """, subject: "SECCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'", to: 'hamdi.dellaa@arabesque.com'
                    } else  {
                         emailext body: """<p>SECCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
                         <p>Check console output at <a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a></p>
                         """, subject: "SECCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'", to: 'hamdi.dellaa@arabesque.com'
                    }
                 }

          
        }
    }
}