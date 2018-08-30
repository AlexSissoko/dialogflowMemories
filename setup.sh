projectId=""
serviceAccountName=""
envName=""


installGcloud () {
    export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"
    echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
    sudo apt-get update && sudo apt-get install google-cloud-sdk
}

5. `gcloud init`

createProject () {
    gcloud projects create $projectId
}

2. `gcloud init`

enableProjectServices () {
    gcloud services enable \
        iam.googleapis.com \
        iamcredentials.googleapis.com \
        dialogflow.googleapis.com
}

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
    sudo apt-get install pip
    pip install --upgrade virtualenv
    virtualenv $envName
}

installDialogflow () {
    source "$envName/bin/activate"
    pip install dialogflow
}

