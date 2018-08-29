# How to set up Google Cloud Platform

## Reference pages
+ [Quickstart](https://cloud.google.com/dialogflow-enterprise/docs/quickstart)
+ [Install gcloud](https://cloud.google.com/sdk/docs/downloads-apt-get)
+ [Create Project](https://cloud.google.com/sdk/gcloud/reference/projects/create)
+ [Enable Services](https://cloud.google.com/sdk/gcloud/reference/services/)
+ [Service Accounts](https://cloud.google.com/iam/docs/creating-managing-service-accounts)
+ [Activate Service Account](https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account)
+ [Python Client github repo](https://github.com/dialogflow/dialogflow-python-client-v2)
+ [Python Client docs](https://dialogflow-python-client-v2.readthedocs.io/en/latest/)
+ [DialogFlow Client docs](https://dialogflow-python-client-v2.readthedocs.io/en/latest/gapic/v2/api.html)
+ [Dialoflow Types docs](https://dialogflow-python-client-v2.readthedocs.io/en/latest/gapic/v2/types.html)

## Steps
* [Installing gcloud](#InstallGcloud)
* [Creating a project](#CreateProject)
* [Enabling Services](#EnableServices)
* [Creating a Service Account](#CreateServiceAccount)
* [Activating a service account](#ActivateServiceAccount)
* [Set credentials environment variable](#SetEnvironmentVariable)
* [Create Dialogflow agent](#CreateAgent)
* [Using the Python Client library](#PythonClient)


## Steps
<a name="InstallGcloud"></a>

### Installing gcloud
Refer to [Install gcloud](https://cloud.google.com/sdk/docs/downloads-apt-get) for more
detailed explanations of the following instructions.

1. `export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"`

2. `echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list`

3. `curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -`

4. `sudo apt-get update && sudo apt-get install google-cloud-sdk`

5. `gcloud init`

<a name="CreateProject"></a>

### Creating a project
Refer to [Create Project](https://cloud.google.com/sdk/gcloud/reference/projects/create) 
for more detailed explanations and examples.

1. `gcloud projects create [NewProject-ID]`

2. `gcloud init`

If you just want to change the default configuration, then just reinitialize **[default]**
configuration. Otherwise:

1. Choose "Create a new configuration"
2. Enter new configuration name
3. Choose a configuration account
4. Choose newly created project

<a name="EnableServices"></a>

### Enabling services
Refer to [Enable Services](https://cloud.google.com/sdk/gcloud/reference/services/) 
for more detailed explanations and examples.

1. `gcloud services list`
This lists what services you have already enabled for the project. If the response you 
get is something like `PERMISSION_DENIED`, then try to `gcloud init` using the original 
email/account used to make the project. This account should have the proper permissions. 

2. `gcloud services list --available`
This lists what services you can enable for the project.

3. 
    ```
    gcloud services enable \
    iam.googleapis.com \
    iamcredentials.googleapis.com \
    dialogflow.googleapis.com
    ```
This enables dialogflow as well as some permission/credential apis for the project.

<a name="CreateServiceAccount"></a>

### Creating a service account
Refer to [Service Accounts](https://cloud.google.com/iam/docs/creating-managing-service-accounts)
for more detailed explanations and examples.

1. `gcloud iam service-accounts create [SA-NAME] --display-name "[SA-DISPLAY-NAME]"`
There should be a response saying that the account was created. To see what accounts there
are in a particular project, run `gcloud iam service-accounts list`

Move to whichever directory you want to hold your service account key. Run:
2. 
    ```
    gcloud iam service-accounts keys create ./key.json \
        --iam-account [SA-NAME]@[PROJECT-ID].iam.gserviceaccount.com
    ```
There should be a response saying that the key was created.

3. 
    ```
    gcloud iam service-accounts keys list \ 
	--iam-account [SA-NAME]@[PROJECT-ID].iam.gserviceaccount.com
    ```
This lists the keys assocatied with the account.

**NOTE**: To delete a key:
```
 gcloud iam service-accounts keys delete [KEY-ID] \
    --iam-account [SA-NAME]@[PROJECT-ID].iam.gserviceaccount.com
```

4. `gcloud projects get-iam-policy [PROJECT-ID]`
Lets you see the bindings and roles of accounts in the project.

5. 
    ```
    gcloud projects add-iam-policy-binding [PROJECT-ID] \
	--member serviceAccount:[SA-NAME]@[PROJECT-ID].iam.gserviceaccount.com --role roles/[roleType]
    ```
  
Adds a role to your service account. Typical role value should be `dialogflow.client` as [roleType].
However, I've encountered bugs where the first gservice account that you create in the client role
somehow doesn't work properly (can't use dialogflow api). Creating a second gservice account 
and then giving it the client role will work as intended. Also, if you're lazy and also need other
permissions, you can grant the `dialogflow.admin` role to the service account. But, this is a bad
way to do things. Creating a second gservice account and giving it the client role is recommended.

<a name="ActivateServiceAccount"></a>

### Activating a service account
Refer to [Activate Service Account](https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account) for more detailed explanations and examples.

`gcloud auth activate-service-account [ACCOUNT_NAME] --key-file=[PATH_TO_KEY_FILE]`

Remember, the service account name is of the form [SA-NAME]@[PROJECT-ID].iam.gserviceaccount.com.

<a name="SetEnvironmentVariable"></a>

### Set credentials environment variable 
Refer to [Quickstart](https://cloud.google.com/dialogflow-enterprise/docs/quickstart).

`export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"`

Where PATH is the path to the service account key file (e.g. ~/key.json)

Remember that this only applies to the current shell session. You will need to reinitialize this
variable each time unless you put a command in your bashrc.

<a name="CreateAgent"></a>

### Create Dialogflow agent
Refer to [Quickstart](https://cloud.google.com/dialogflow-enterprise/docs/quickstart).
If at this point, you do not yet have a dialogflow agent associated with the project, create one.
Follow the quickstart reference page's instructions on this in order to do so.

<a name="PythonClient"></a>

### Using the Python client library.
I used the Python client library. If you want to use a different language, refer to 
[Libaries](https://cloud.google.com/dialogflow-enterprise/docs/reference/libraries/overview).

**Note**: This is for Python 2.7, but it should work pretty similarly for python3.

1. Install pip: `sudo apt-get install pip`
2. Install virtualenv: `pip install --upgrade virtualenv`
3. Create virtual environment : `virtualenv [envName]`
This creates a virtual environment with your default python version
4. Activate virtual environment: `source [envName/bin/activate]`
(To deactivate, simply run `deactivate`)
5. Install dialogflow : `pip install dialogflow`

For reference on the python client:
+ [Python Client github repo](https://github.com/dialogflow/dialogflow-python-client-v2)
+ [Python Client docs](https://dialogflow-python-client-v2.readthedocs.io/en/latest/)
+ [DialogFlow Client docs](https://dialogflow-python-client-v2.readthedocs.io/en/latest/gapic/v2/api.html)
+ [Dialoflow Types docs](https://dialogflow-python-client-v2.readthedocs.io/en/latest/gapic/v2/types.html)
