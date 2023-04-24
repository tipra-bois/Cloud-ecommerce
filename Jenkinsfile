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
            step {
                // Clone the GitHub repository
                git branch: 'main', url: 'https://github.com/tipra-bois/Cloud-ecommerce.git'
                sh 'echo "Hello, git completed"'
                sh 'dir'
            }
        }
        stage('Build Images') {
            steps {
                step {
                    dir('order-microservice') {
                        script {
                            orderImage = docker.build ordermicroservice
                        }
                    }
                }
                step {
                    dir('product-microservice') {
                        script {
                            productImage = docker.build productmicroservice
                        }
                    }
                }
                step {
                    dir('user-microservice') {
                        script {
                            userImage = docker.build usermicroservice
                        }
                    }
                }
            }
        }
        stage('Push Images') {
            environment {
                registryCredential = 'dockerhub-credentials'
            }
            steps {
                step {
                    dir('order-microservice') {
                        script {
                            docker.withRegistry('https://registry.hub.docker.com', registryCredential) {
                                orderImage.push('latest')
                            }
                        }
                    }
                }
                step {
                    dir('product-microservice') {
                        script {
                            docker.withRegistry('https://registry.hub.docker.com', registryCredential) {
                                productImage.push('latest')
                            }
                        }
                    }
                }
                step {
                    dir('user-microservice') {
                        script {
                            docker.withRegistry('https://registry.hub.docker.com', registryCredential) {
                                userImage.push('latest')
                            }
                        }
                    }
                }
            }
        }

        stage('Deploy MongoDB') {
            step {
                // Deploy MongoDB using kubectl
                sh 'kubectl apply -f mongodb-deployment.yaml'
                sh 'kubectl apply -f mongodb-service.yaml'
            }
        }
        stage('Deploy RabbitMQ') {
            step {
                // Deploy RabbitMQ using kubectl
                sh 'kubectl apply -f rabbitmq-deployment.yaml'
                sh 'kubectl apply -f rabbitmq-service.yaml'
                sleep time: 60, unit: 'SECONDS'
            }
        }
        stage('Deploy Microservices') {
            steps {
                step {
                    dir('order-microservice') {
                        script {
                            kubernetes.deploy(
                            configs: 'order-microservice-deployment.yaml',
                            'order-microservice-service.yaml'
                        )
                        }
                    }
                }
                step {
                    dir('product-microservice') {
                        script {
                            kubernetes.deploy(
                            configs: 'product-microservice-deployment.yaml',
                            'product-microservice-service.yaml'
                        )
                        }
                    }
                }
                step {
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
}

