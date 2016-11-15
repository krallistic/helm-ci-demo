node {
  def appName = 'helm-ci-demo'

  def backendName = "${appName}-backend"
  stage 'Checkout'
  checkout scm

  dir("backend/") {
    //TODO change user
    def imageTag = "jkaralus/${backendName}:${env.BRANCH_NAME}.${env.BUILD_NUMBER}"


    stage 'Building Image'
      cd backend
      docker.build ${imageTag} "backend/"
      //sh("docker build -t ${imageTag} backend/")

      stage 'UnitTest with Image'
      sh("docker run  ${imageTag} pytest tests/")

      stage 'Push image to registry'
      //sh("gcloud docker push ${imageTag}")
  }



  input message: 'Deploy to Prod?', ok: 'Yes'
  //input message: 'Please Confirm Deploy from Staging to Production', parameters: [choice(choices: ['Yes', 'No'], description: '', name: 'Answer')]


  stage "Deploy Application"
  switch (env.BRANCH_NAME) {
    // Roll out to staging
    case "staging":
               break

    // Roll out to production
    case "master":
              break

    // Roll out a dev environment
    default:
        echo 'To access your environment run `kubectl proxy`'
        echo "Then access your service via http://localhost:8001/api/v1/proxy/namespaces/${env.BRANCH_NAME}/services/${feSvcName}:80/"
  }
}
