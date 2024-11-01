// pipeline {
//     agent any

//     environment {
//         DOCKER_CREDENTIALS = credentials('docker-hub-credentials') // Replace with your Jenkins Docker credentials ID
//         DOCKER_IMAGE = 'your-docker-repo/crypto-price-service:latest' // Replace with your Docker image name
//     }

//     stages {
//         stage('Checkout Code') {
//             steps {
//                 checkout scm
//             }
//         }

//         stage('Build Docker Image') {
//             steps {
//                 script {
//                     docker.build(DOCKER_IMAGE)
//                 }
//             }
//         }

//         stage('Run Tests') {
//             steps {
//                 script {
//                     // Add your test command here, e.g., npm test or python -m unittest
//                     echo "Running tests..."
//                 }
//             }
//         }

//         stage('Login to Docker Hub') {
//             steps {
//                 script {
//                     docker.withRegistry('https://index.docker.io/v1/', DOCKER_CREDENTIALS) {
//                         echo "Logged in to Docker Hub"
//                     }
//                 }
//             }
//         }

//         stage('Push Docker Image') {
//             steps {
//                 script {
//                     docker.image(DOCKER_IMAGE).push()
//                 }
//             }
//         }

//         stage('Deploy to Kubernetes') {
//             steps {
//                 script {
//                     // Ensure kubectl is configured
//                     sh 'kubectl config use-context your-kubernetes-context' // Replace with your Kubernetes context
//                     // Deploy the application using kubectl
//                     sh 'kubectl apply -f deployment.yaml'
//                     sh 'kubectl apply -f service.yaml'
//                     sh 'kubectl apply -f hpa.yaml'
//                 }
//             }
//         }
//     }

//     post {
//         success {
//             echo 'Pipeline completed successfully!'
//         }
//         failure {
//             echo 'Pipeline failed!'
//         }
//     }
// }

###################################################################################################


pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t crypto-service:latest .'
            }
        }
        stage('Test') {
            steps {
                sh 'docker run crypto-service:latest python -m unittest discover tests'
            }
        }
        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-registry', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    sh 'docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD} abbeydauda'
                    sh 'docker tag crypto-service:latest abbeydauda/crypto-service:latest'
                    sh 'docker push abbeydauda/crypto-service:latest'
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
                    sh 'kubectl apply -f deployment.yaml'
                    sh 'kubectl apply -f service.yaml'
                    sh 'kubectl apply -f autoscaling.yaml'
                }
            }
        }
    }
    post {
        failure {
            mail to: 'abbeydauda20@gmail.com',
                 subject: 'Crypto Service Deployment Failed',
                 body: 'Deployment failed, please check Jenkins logs.'
        }
        success {
            mail to: 'abbeydauda20@gmail.com.com',
                 subject: 'Crypto Service Deployment Successful',
                 body: 'Deployment successful!'
        }
    }
}
