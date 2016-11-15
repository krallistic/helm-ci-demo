def pipeline = new io.estrado.Pipeline()


node {
  // continue only if pipeline enabled
  if (!config.pipeline.enabled) {
      println "pipeline disabled"
      return
  }

  git GIT_URL

  stage 'Canary release'

  stage 'Rolling upgrade Staging'

  stage 'Approve'

  stage 'Rolling upgrade Production'

}