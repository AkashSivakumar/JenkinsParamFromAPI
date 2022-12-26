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
                                        ''' if ( Env == "dev") {
                                            def value1 = "http://app:5000/data?DevREPO".toURL().text
                                            return [value1]
                                            } else if ( Env == "test") {
                                            def value2 = "http://app:5000/data?TestREPO".toURL().text
                                            return [value2]
                                            }
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
                    print 'DEBUG: parameter Repo = ' + params.Repo
                }
            }
        }
    }   
}



