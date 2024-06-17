pipeline {
    agent any
    stages {
        stage('Git Checkout') {
            steps {
                git 'https://github.com/asafcohen11/WorldOfGames.git'
            }
        }
        stage('Build image') {
             /* This builds the actual image; synonymous to
              * docker build on the command line */
            steps {
             sh 'docker build -t asafcohen11/maingame:0.1 .'
            }
        }
        stage('Run image') {
            steps {
             sh 'docker run -d --name game -p 5000:5000 asafcohen11/maingame:0.1'
            }
        }
         stage('Test MainGame') {
            steps {
             sh 'docker exec -d game python e2e.py'
            }
        }

    }
}
