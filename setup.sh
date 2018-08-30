mainAccountName="" #This should be an email address
projectId="" #Must have only lowercaseletters,hyphens,numbers
serviceAccountName="" #Must have only lowercaseletters,hyphens,numbers
envName=""


installGcloud () {
    export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"
    echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
    sudo apt-get update && sudo apt-get install google-cloud-sdk
}

setConfigAccount () {
    gcloud config set account $mainAccountName
    gcloud auth login
}


createProject () {
    gcloud projects create $projectId
}

setConfigProject () {
    gcloud config set project $projectId
}


enableProjectServices () {
    gcloud services enable \
        iam.googleapis.com \
        iamcredentials.googleapis.com \
        dialogflow.googleapis.com
}

#Gives the service account admin role, not client
createServiceAccount () {
    gcloud iam service-accounts create $serviceAccountName --display-name $serviceAccountName
    gcloud iam service-accounts keys create "./key.json" \
        --iam-account "$serviceAccountName@$projectId.iam.gserviceaccount.com"
    gcloud projects add-iam-policy-binding $projectId \
	--member "serviceAccount:$serviceAccountName@$projectId.iam.gserviceaccount.com" \
        --role roles/dialogflow.admin
}

activateServiceAccount () {
    gcloud auth activate-service-account "$serviceAccountName@$projectId.iam.gserviceaccount.com" \
        --key-file="./key.json"
}

exportCredentials () {
    export GOOGLE_APPLICATION_CREDENTIALS="./key.json"
}

createVirtualEnv () {
    sudo apt-get install python-pip
    pip install --upgrade virtualenv
    virtualenv $envName
}

installDialogflow () {
    source "./$envName/bin/activate"
    pip install dialogflow
}

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
