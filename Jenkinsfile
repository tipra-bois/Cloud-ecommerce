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
                dir('product-microservice') {
                    script {
                        productImage = docker.build productmicroservice
                    }
                }
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
                dir('product-microservice') {
                    script {
                        docker.withRegistry('https://registry.hub.docker.com', registryCredential) {
                            productImage.push('latest')
                        }
                    }
                }
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
                dir('order-microservice') {
                    script {
                        kubernetes.deploy(
                            configs: 'order-microservice-deployment.yaml',
                            delegate: true,
                            enableConfigSubstitution: true
                        )
                        kubernetes.deploy(
                            configs: 'order-microservice-service.yaml',
                            delegate: true,
                            enableConfigSubstitution: true
                        )
                    }
                }
                dir('product-microservice') {
                    script {
                        kubernetes.deploy(
                            configs: 'product-microservice-deployment.yaml',
                            delegate: true,
                            enableConfigSubstitution: true
                        )
                        kubernetes.deploy(
                            configs: 'product-microservice-service.yaml',
                            delegate: true,
                            enableConfigSubstitution: true
                        )
                    }
                }
                dir('user-microservice') {
                    script {
                        kubernetes.deploy(
                            configs: 'user-microservice-deployment.yaml',
                            delegate: true,
                            enableConfigSubstitution: true
                        )
                        kubernetes.deploy(
                            configs: 'user-microservice-service.yaml',
                            delegate: true,
                            enableConfigSubstitution: true
                        )
                    }
                }
            }
        }
    }
}
