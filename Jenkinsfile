pipeline {
    environment {
        ordermicroservice = 'CoderCatA5/order-microservice'
        productmicroservice = 'CoderCatA5/product-microservice'
        usermicroservice = 'CoderCatA5/user-microservice'

        orderImage = ''
        productImage = ''
        userImage = ''
    }

    agent any

    stages {
        stage('Checkout Source') {
            steps {
                script {
                    // Clone the GitHub repository
                    git branch: 'main', url: 'https://github.com/tipra-bois/Cloud-ecommerce.git'
                }
                step {
                    sh 'echo "Hello, git completed"'
                }
                step {
                    sh 'dir'
                }
            }
        }
        stage('Build Images') {
            steps {
                script {
                    dir('order-microservice') {
                        orderImage = docker.build ordermicroservice
                    }
                    dir('product-microservice') {
                        productImage = docker.build productmicroservice
                    }
                    dir('user-microservice') {
                        userImage = docker.build usermicroservice
                    }
                }
            }
        }
        stage('Push Images') {
            environment {
                registryCredential = 'dockerhub-credentials'
            }
            steps {
                script {
                    dir('order-microservice') {
                        docker.withRegistry('https://registry.hub.docker.com', registryCredential) {
                            orderImage.push('latest')
                        }
                    }
                    dir('product-microservice') {
                        docker.withRegistry('https://registry.hub.docker.com', registryCredential) {
                            productImage.push('latest')
                        }
                    }
                    dir('user-microservice') {
                        docker.withRegistry('https://registry.hub.docker.com', registryCredential) {
                            userImage.push('latest')
                        }
                    }
                }
            }
        }

        stage('Deploy MongoDB') {
            steps {
                sh 'kubectl apply -f mongodb-deployment.yaml'
                sh 'kubectl apply -f mongodb-service.yaml'
            }
        }
        stage('Deploy RabbitMQ') {
            steps {
                sh 'kubectl apply -f rabbitmq-deployment.yaml'
                sh 'kubectl apply -f rabbitmq-service.yaml'
                sleep time: 60, unit: 'SECONDS'
            }
        }
        stage('Deploy Microservices') {
            steps {
                script {
                    dir('order-microservice') {
                        kubernetes.deploy(
                            configs: 'order-microservice-deployment.yaml',
                            service: 'order-microservice-service.yaml'
                        )
                    }
                    dir('product-microservice') {
                        kubernetes.deploy(
                            configs: 'product-microservice-deployment.yaml',
                            service: 'product-microservice-service.yaml'
                        )
                    }
                    dir('user-microservice') {
                        kubernetes.deploy(
                            configs: 'user-microservice-deployment.yaml',
                            service: 'user-microservice-service.yaml'
                        )
                    }
                }
            }
        }
    }
}
