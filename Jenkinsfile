pipeline {
    agent any
    stages {
        stage('Setup parameters') {
            steps {
                script { 
                    properties([
                        parameters([
                        [$class: 'ChoiceParameter', 
                            choiceType: 'PT_MULTI_SELECT', 
                            description: 'Select the Env Name from the Dropdown List', 
                            name: 'Env',
                            randomName: 'choice-parameter-5631314439613978', 
                            script: [
                                $class: 'GroovyScript', 
                                fallbackScript: [
                                    classpath: [], 
                                    sandbox: true, 
                                    script: 
                                        'return[\'Could not get Env\']'
                                ], 
                                script: [
                                    classpath: [], 
                                    sandbox: true, 
                                    script: 
                                        'return["dev","test"]'
                                ]
                            ]
                        ], 
                        [$class: 'CascadeChoiceParameter', 
                            choiceType: 'PT_MULTI_SELECT', 
                            description: 'Select the repo from the Dropdown List', 
                            name: 'Repo', 
                            randomName: 'choice-parameter-5631314456178619', 
                            referencedParameters: 'Env', 
                            script: [
                                $class: 'GroovyScript', 
                                fallbackScript: [
                                    classpath: [], 
                                    sandbox: true, 
                                    script: 
                                        'return[\'Could not get Environment from Env Param\']'
                                ], 
                                script: [
                                    classpath: [], 
                                    sandbox: true, 
                                    script: 
                                        ''' 
                                            import groovy.json.JsonSlurper
                                            import jenkins.model.* 
                                            import hudson.model.*
                                            import hudson.slaves.EnvironmentVariablesNodeProperty
                                            import hudson.EnvVars
                                            jenkins = Jenkins.instance
                                            EnvironmentVariablesNodeProperty prop = jenkins.getGlobalNodeProperties().get(EnvironmentVariablesNodeProperty.class)
                                            EnvVars env = prop.getEnvVars()

                                            try {
                                            def jenkinsYAML = readYaml file: "${env['WORKSPACE']}/{Env}/jenkins.yaml"
                                            }catch(e){ return [e.toString()] }
                                           

                                            def get_versions_from_api(urlvar){
                                                def responsevar = urlvar.toURL().text
                                                def parser = new JsonSlurper()
                                                def Object jsonResp = parser.parseText(responsevar.toString())
                                                def versions_list = []
                                                jsonResp["items"].each { getversion ->
                                                def str = getversion["name"].split('/')
                                                versions_list.add(str[3])
                                                }
                                                return versions_list.sort().reverse()
                                            }

                                            try {
                                            if ( Env == "dev"){
                                                env.APP_NAME = jenkinsYAML.APP_NAME
                                                return get_versions_from_api("http://app:5000/${env.APP_NAME}")
                                            } else if ( Env == "test") {
                                                return get_versions_from_api("http://app:5000/test")
                                            }
                                            }catch(e){ return [e.toString()] }
                                        '''
                                    ]
                                ]
                            ]
                        ])
                    ])
                }
            }
        }

        stage('Print Param'){
            steps{
                script{
                    println(params.Repo)
                }
            }
        }
    }   
}