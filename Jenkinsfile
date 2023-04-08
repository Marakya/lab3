pipeline {
    agent any

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
        stage('Checkout') {
            steps{
                git branch: 'main',
                    url: 'https://github.com/Marakya/lab3.git'        
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
    }
}


// pipeline {
//     agent any

//     stages {
//         stage('Docker version') {
//             steps {
//                 sh "echo $USER"
//                 sh 'docker version'
//             }
//         }
//         stage('Delete workspace before build starts') {
//             steps {
//                 echo 'Deleting workspace'
//                 deleteDir()
//             }
//         }
//         stage('Build docker image') {
//             steps{
// //                 sh 'docker build -t my_img -f /var/lib/jenkins/workspace/lab3/Dockerfile .'
//                 sh 'docker build -t my_img -f Dockerfile .'
//                 sh 'docker run -it -d --name my_cont -p 7000:7000  my_img:latest'
//                 sh 'docker logs -f my_cont'
//             }
//         }
//         stage('Push docker image to DockerHub') {
//             steps{
//                 withDockerRegistry(credentialsId: 'dockerhub_marakya', url: 'https://index.docker.io/v1/') {
//                     sh '''
//                         docker push my_img
//                     '''
//                 }
//             }
//         }
//     }
// }
