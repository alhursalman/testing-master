pipeline{
        agent any
        stages{
		    stage('---Run Test---'){
                        steps{
                            sh "python3 -m pytest test/test_factorialfunction.py"
                        }
                }
        }
}
