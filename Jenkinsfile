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
        
        // --- NUEVA ETAPA DE TEST ---
        stage('Test Unitario') {
            steps {
                echo 'Ejecutando pruebas de seguridad y lógica...'
                // Usamos un contenedor temporal de python solo para correr el test
                // Esto asegura que el entorno de prueba sea limpio e idéntico a producción
                sh 'docker run --rm -v ${PWD}/app:/app -w /app python:3.9-slim python -m unittest test_logic.py'
            }
        }
        
        stage('Construir Imagen') {
            steps {
                sh 'docker build -t aquatrans-image:latest .'
            }
        }
        
        stage('Desplegar') {
            steps {
                sh 'docker run -d --name aquatrans-v1 -p 9090:80 aquatrans-image:latest'
            }
        }
    }
}
