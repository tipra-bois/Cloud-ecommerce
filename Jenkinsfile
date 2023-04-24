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
                // Clone the GitHub repository
                git branch: 'main', url: 'https://github.com/tipra-bois/Cloud-ecommerce.git'
                sh 'echo "Hello, git completed"'
                sh 'dir'
            }
        }
        stage('Build Images') {
            steps {
                dir('order-microservice') {
                    script {
                        orderImage = docker.build ordermicroservice
                    }
                }
            }
            steps {
                dir('product-microservice') {
                    script {
                        productImage = docker.build productmicroservice
                    }
                }
            }
            steps {
                dir('user-microservice') {
                    script {
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
                dir('order-microservice') {
                    script {
                        docker.withRegistry('https://registry.hub.docker.com', registryCredential) {
                            orderImage.push('latest')
                        }
                    }
                }
            }
            steps {
                dir('product-microservice') {
                    script {
                        docker.withRegistry('https://registry.hub.docker.com', registryCredential) {
                            productImage.push('latest')
                        }
                    }
                }
            }
            steps {
                dir('user-microservice') {
                    script {
                        docker.withRegistry('https://registry.hub.docker.com', registryCredential) {
                            userImage.push('latest')
                        }
                    }
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
        stage('Deploy Microservices') {
            steps {
                dir('order-microservice') {
                    script {
                        kubernetes.deploy(
                            configs: 'order-microservice-deployment.yaml',
                            'order-microservice-service.yaml'
                        )
                    }
                }
            }
            steps {
                dir('product-microservice') {
                    script {
                        kubernetes.deploy(
                            configs: 'product-microservice-deployment.yaml',
                            'product-microservice-service.yaml'
                        )
                    }
                }
            }
            steps {
                dir('user-microservice') {
                    script {
                        kubernetes.deploy(
                            configs: 'user-microservice-deployment.yaml',
                            'user-microservice-service.yaml'
                        )
                    }
                }
            }
        }
    }
}

