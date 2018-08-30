mainAccountName="" #This should be an email address
projectId="" #Must have only lowercase letters,hyphens,numbers
serviceAccountName="" #Must have only lowercaseletters,hyphens,numbers
envName="" #Name of the python environment that will be set up


#Installs Google Cloud Platform
installGcloud () {
    export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"
    echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
    sudo apt-get update && sudo apt-get install google-cloud-sdk
}

#Sets the account for the Google Cloud configuration
setConfigAccount () {
    gcloud config set account $mainAccountName
    gcloud auth login
}


#Creates a Google Cloud project
createProject () {
    gcloud projects create $projectId
}

#Sets the project for the Google Cloud configuration
setConfigProject () {
    gcloud config set project $projectId
}


#Enables services for the current Google Cloud project
enableProjectServices () {
    gcloud services enable \
        iam.googleapis.com \
        iamcredentials.googleapis.com \
        dialogflow.googleapis.com
}

#Creates a service account and gives it dialogflow admin role
#The admin role is purely for convenience sake
#TODO:Modifiying this to create two service accounts with the client role
createServiceAccount () {
    gcloud iam service-accounts create $serviceAccountName --display-name $serviceAccountName
    gcloud iam service-accounts keys create "./key.json" \
        --iam-account "$serviceAccountName@$projectId.iam.gserviceaccount.com"
    gcloud projects add-iam-policy-binding $projectId \
	--member "serviceAccount:$serviceAccountName@$projectId.iam.gserviceaccount.com" \
        --role roles/dialogflow.admin
}

#Activates a service account
activateServiceAccount () {
    gcloud auth activate-service-account "$serviceAccountName@$projectId.iam.gserviceaccount.com" \
        --key-file="./key.json"
}

#Sets Google application credentials
exportCredentials () {
    export GOOGLE_APPLICATION_CREDENTIALS="./key.json"
}

#Installs pip, installs virtualenv, creates a virtual environment
createVirtualEnv () {
    sudo apt-get install python-pip
    pip install --upgrade virtualenv
    virtualenv $envName
}

#Installs dialogflow module in virtual environment
installDialogflow () {
    source "./$envName/bin/activate"
    pip install dialogflow
}

setup () {
    installGcloud
    setConfigAccount
    createProject
    setConfigProject
    enableProjectServices
    createServiceAccount
    activateServiceAccount
    exportCredentials
    createVirtualEnv
    installDialogflow
}

#Set everything up
setup
