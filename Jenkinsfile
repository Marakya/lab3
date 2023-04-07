pipeline {
    agent { label 'ubuntu' }

    stages {
        stage('Docker version') {
            steps {
                sh "echo $USER"
                sh 'docker version'
            }
        }
        stage('Delete workspace before build starts') {
            steps {
                echo 'Deleting workspace'
                deleteDir()
            }
        }
        stage('Build docker image') {
            steps{
                sh 'docker build -t my_img -f Dockerfile .'
                sh 'docker run -it -d --name my_cont -p 7000:7000  my_img:latest'
                sh 'docker logs -f my_cont'
            }
        }
        stage('Push docker image to DockerHub') {
            steps{
                withDockerRegistry(credentialsId: 'dockerhub_marakya', url: 'https://index.docker.io/v1/') {
                    sh '''
                        docker push my_img
                    '''
                }
            }
        }
        stage('Delete docker image locally') {
            steps{
                sh 'docker rmi bakavets/jenkins-images:0.4'
            }
        }
    }
}
