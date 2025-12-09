pipeline {
    agent any

    stages {
        stage('Limpieza Previa') {
            steps {
                script {
                    sh 'docker stop aquatrans-v1 || true'
                    sh 'docker rm aquatrans-v1 || true'
                }
            }
        }
        
        stage('Construir Imagen') {
            steps {
                // Primero construimos la imagen con TODO el código adentro
                sh 'docker build -t aquatrans-image:latest .'
            }
        }

        stage('Test Unitario') {
            steps {
                echo 'Ejecutando pruebas DENTRO de la imagen construida...'
                // Usamos la imagen que acabamos de crear.
                // Sobrescribimos el comando CMD para que en vez de iniciar el server, corra el test.
                sh 'docker run --rm aquatrans-image:latest python -m unittest test_logic.py'
            }
        }
        
        stage('Desplegar') {
            steps {
                // Si el test pasó, desplegamos la misma imagen
                sh 'docker run -d --name aquatrans-v1 -p 9090:80 aquatrans-image:latest'
            }
        }
    }
}
