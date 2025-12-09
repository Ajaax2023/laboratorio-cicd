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
                sh 'docker build -t aquatrans-image:latest .'
            }
        }

        stage('Test Unitario') {
            steps {
                echo 'Ejecutando pruebas DENTRO de la imagen...'
                sh 'docker run --rm aquatrans-image:latest python -m unittest test_logic.py'
            }
        }
        
        stage('Desplegar') {
            steps {
                sh 'docker run -d --name aquatrans-v1 -p 9090:80 aquatrans-image:latest'
            }
        }

        // --- NUEVA ETAPA: SMOKE TEST ---
        stage('Smoke Test (Prueba de Humo)') {
            steps {
                echo 'Esperando a que el contenedor inicie...'
                sleep 5 // Damos 5 segundos de cortesía para que el servidor arranque
                
                script {
                    echo 'Verificando salud del servicio HTTP...'
                    // Usamos docker exec para entrar al contenedor y pedirle a Python que intente abrir su propio localhost
                    // Si responde 200, sale con código 0 (éxito). Si falla, Python tira error y Jenkins falla.
                    sh '''
                        docker exec aquatrans-v1 python -c "import urllib.request; import sys; resp = urllib.request.urlopen('http://localhost:80'); sys.exit(0 if resp.getcode() == 200 else 1)"
                    '''
                }
            }
        }
    }
}
