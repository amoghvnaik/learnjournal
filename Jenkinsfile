pipeline{
        agent any
        
        stages{
		stage('--building--'){
			steps{
                        	sh '''. ~/.bashrc
				      docker build --build-arg NAME=$NAME --build-arg TEST_NAME=$TEST_NAME --build-arg USER=$USER -
-build-arg PASSWORD=$PASSWORD --build-arg HOST=$HOST --build-arg SECRET_KEY=$SECRET_KEY -t journalapp .
                                      docker tag journalapp instance-1:5000/journalapp
				      docker push instance-1:5000/journalapp
				      '''
			}
		}
                stage('--deployment--'){
                        steps{
				sh '''. ~/.bashrc 
				      sed "s/{{NAME}}/${NAME}/g;s/{{TEST_NAME}}/${TEST_NAME}/g;s/{{USER}}/${USER}/g;s/{{PASSWORD}}/${PASSWORD}/g;s/{{HOST}}/${HOST}/g;s/{{SECRET_KEY}}/${SECRET_KEY}/g" ./kubernetes.yaml | kubectl apply -f -
                                      '''
                        }
                }
        }
}
