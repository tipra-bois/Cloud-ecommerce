pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the GitHub repository
                git branch: 'main', url: 'https://github.com/tipra-bois/Cloud-ecommerce.git'
                sh 'echo "Hello, git completed"'
                sh 'dir'
            }
        }
     
        }
        stage('Deploy MongoDB') {
            steps {
                // Deploy MongoDB using kubectl
                sh 'kubectl apply -f mongodb-deployment.yaml'
                sh 'kubectl apply -f mongodb-service.yaml'
            }
        }
        stage('Deploy RabbitMQ') {
            steps {
                // Deploy RabbitMQ using kubectl
                sh 'kubectl apply -f rabbitmq-deployment.yaml'
                sh 'kubectl apply -f rabbitmq-service.yaml'
                sleep time: 60, unit: 'SECONDS'
            }
        }
        stage('Build and Deploy Microservices') {
            steps {
                // Build Docker images for each microservice
                dir('user-microservice') {
                    sh 'docker build -t user-microservice:4 .'
                    sh 'kubectl apply -f user-microservice-deployment.yaml'
                    sh 'kubectl apply -f user-microservice-service.yaml'
                    sleep time: 60, unit: 'SECONDS'
                }

                dir('product-microservice') {
                    sh 'docker build -t product-microservice:3 .'
                    sh 'kubectl apply -f product-microservice.deployment.yaml'
                    sh 'kubectl apply -f product-microservice-service.yaml'
                    sleep time: 60, unit: 'SECONDS'
                }

                dir('order-microservice') {
                    sh 'docker build -t order-microservice:3 .'
                    sh 'kubectl apply -f order-microservice-deployment.yaml'
                    sh 'kubectl apply -f order-microservice-service.yaml'
                    sleep time: 60, unit: 'SECONDS'
                }
            }
        }
//         stage('Port Forwarding') {
//             steps {
//                 // Port forward each microservice for local testing
//                 sh 'kubectl port-forward services/user-microservice 7070:7070'
//                 sh 'kubectl port-forward services/product-microservice 8080:8080'
//                 sh 'kubectl port-forward services/order-microservice 9090:9090'
//             }
//         }
//         stage('Port Forwarding') {

//                 // Run steps in parallel within the same stage
//                 parallel {
//                     stage('Port 7070') {
//                         steps {
//                             // Run step 1sleep time: 300, unit: 'SECONDS'
//                             sh 'kubectl port-forward services/user-microservice 7070:7070'
//                         }
//                     }
//                     stage('Port 8080') {
//                         steps {
//                             // Run step 2
//                             sh 'kubectl port-forward services/product-microservice 8080:8080'
//                         }
//                     }
//                     stage('Port 9090') {
//                         steps {
//                             // Run step 3
//                             sh 'kubectl port-forward services/order-microservice 9090:9090'
//                         }
//                     }
//                 }

    //         }
    }

//     post {
//         always {
//             // Clean up port forwarding processes
//             sh 'pkill -f "kubectl port-forward"'
//         }
//     }
}
