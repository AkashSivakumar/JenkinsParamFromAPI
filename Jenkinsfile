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
                            name: 'EnvParam',
                            randomName: 'choice-parameter-5631314439613978', 
                            script: [
                                $class: 'GroovyScript', 
                                fallbackScript: [
                                    classpath: [], 
                                    sandbox: false, 
                                    script: 
                                        'return[\'Could not get Env\']'
                                ], 
                                script: [
                                    classpath: [], 
                                    sandbox: false, 
                                    script: 
                                        'return["dev","test"]'
                                ]
                            ]
                        ], 
                        [$class: 'ChoiceParameter', 
                            choiceType: 'PT_SINGLE_SELECT', 
                            description: 'Select the Env Name from the Dropdown List', 
                            name: 'JobNameParam',
                            randomName: 'choice-parameter-5631314439613978', 
                            script: [
                                $class: 'GroovyScript', 
                                fallbackScript: [
                                    classpath: [], 
                                    sandbox: false, 
                                    script: 
                                        'return[\'Could not get Env\']'
                                ], 
                                script: [
                                    classpath: [], 
                                    sandbox: false, 
                                    script:
                                        '''
                                            def build = Thread.currentThread().toString()
                                            def regexp= ".+?/job/([^/]+)/.*"
                                            def match = build  =~ regexp
                                            def jobName = match[0][1]
                                            return [jobName]
                                        '''
                                ]
                            ]
                        ], 
                        [$class: 'CascadeChoiceParameter', 
                            choiceType: 'PT_MULTI_SELECT', 
                            description: 'Select the repo from the Dropdown List', 
                            name: 'Repo', 
                            randomName: 'choice-parameter-5631314456178619', 
                            referencedParameters: 'EnvParam,JobNameParam',
                            script: [
                                $class: 'GroovyScript', 
                                fallbackScript: [
                                    classpath: [], 
                                    sandbox: false, 
                                    script: 
                                        'return[\'Could not get Environment from Env Param\']'
                                ], 
                                script: [
                                    classpath: [], 
                                    sandbox: false, 
                                    script: 
                                        ''' 
                                        import groovy.json.JsonSlurper
                                        import jenkins.model.* 
                                        import hudson.model.*
                                        import hudson.EnvVars
                                        import groovy.yaml.YamlSlurper
                                        
                                        List example = new YamlSlurper().parse("example.yaml" as File)
                                        def homeDir = EnvVars.masterEnvVars['HOME']



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
                                        if ( EnvParam == "dev"){
                                            def jenkinsYAML = readYaml file: homeDir + "/workspace/" + JobNameParam + "/dev/jenkins.yaml"
                                            env.APP_NAME = jenkinsYAML.APP_NAME
                                            return get_versions_from_api("http://app:5000/${env.APP_NAME}")
                                        } else if ( EnvParam == "test") {
                                            def jenkinsYAML = readYaml file: "/var/jenkins_home/workspace/final2/test/jenkins.yaml"
                                            env.APP_NAME = jenkinsYAML.APP_NAME
                                            return get_versions_from_api("http://app:5000/${env.APP_NAME}")
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
                    println(params.JobNameParam)
                }
            }
        }
    }   
}