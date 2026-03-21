pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // This pulls your code from the GitHub link you provide in Jenkins
                checkout scm
            }
        }

        stage('Set Up Environment') {
            steps {
                echo 'Installing dependencies...'
                // Create a virtual environment and install Selenium
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                echo 'Executing Automated UI Tests...'
                // Run the python script using the virtual environment
                bat 'venv\\Scripts\\python test_form.py'
            }
        }
    }

    post {
        always {
            echo 'Archiving results...'
            // This runs regardless of success or failure
            cleanWs()
        }
        success {
            echo 'Form validation and tests passed successfully!'
        }
        failure {
            echo 'Tests failed. Please check the console output.'
        }
    }
}