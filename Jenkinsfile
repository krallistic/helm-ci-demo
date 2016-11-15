node {
  def appName = 'helm-ci-demo'
  def feSvcName = "${appName}-frontend"

  //def imageTag = "gcr.io/${project}/${appName}:${env.BRANCH_NAME}.${env.BUILD_NUMBER}"

  checkout scm

  stage 'Build image'
  //sh("docker build -t ${imageTag} .")

  stage 'Run Go tests'
  //sh("docker run ${imageTag} go test")

  stage 'Push image to registry'
  //sh("gcloud docker push ${imageTag}")

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