pipeline {
    agent any

    stages {
        stage('Limpieza Previa') {
            steps {
                script {
                    // El "|| true" evita que falle si el contenedor no existe (primera ejecución)
                    sh 'docker stop aquatrans-v1 || true'
                    sh 'docker rm aquatrans-v1 || true'
                }
            }
        }
        
        stage('Construir Imagen') {
            steps {
                // Construye la imagen usando el Dockerfile del repo descargado
                sh 'docker build -t aquatrans-image:latest .'
            }
        }
        
        stage('Desplegar') {
            steps {
                // Corre el contenedor en el puerto 9090
                sh 'docker run -d --name aquatrans-v1 -p 9090:80 aquatrans-image:latest'
            }
        }
    }
}
