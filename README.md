# DialogflowMemories
Just some basic instructions on how to get set up to start creating and 
modifying your own DialogFlow agent


# How to set up Google Cloud Platform

## Reference pages
### Getting Set up
+ [Install gcloud](https://cloud.google.com/sdk/docs/downloads-apt-get)
+ [Gcloud config](https://cloud.google.com/sdk/gcloud/reference/config) 
+ [Gcloud auth](https://cloud.google.com/sdk/gcloud/reference/auth/)
+ [Create Project](https://cloud.google.com/sdk/gcloud/reference/projects/create)
+ [Enable Services](https://cloud.google.com/sdk/gcloud/reference/services/)
+ [Service Accounts](https://cloud.google.com/iam/docs/creating-managing-service-accounts)
+ [Activate Service Account](https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account)
### Dialogflow agent docs
+ [Dialogflow](https://dialogflow.com/)
+ [Enterprise Quickstart](https://cloud.google.com/dialogflow-enterprise/docs/quickstart)
+ [pypi](https://pypi.org/project/pip/) 
+ [Virtualenv](https://virtualenv.pypa.io/en/stable/) 
+ [Client Libaries](https://cloud.google.com/dialogflow-enterprise/docs/reference/libraries/overview)
+ [Python Client github repo](https://github.com/dialogflow/dialogflow-python-client-v2)
+ [Python Client docs](https://dialogflow-python-client-v2.readthedocs.io/en/latest/)
+ [DialogFlow Client docs](https://dialogflow-python-client-v2.readthedocs.io/en/latest/gapic/v2/api.html)
+ [Dialoflow Types docs](https://dialogflow-python-client-v2.readthedocs.io/en/latest/gapic/v2/types.html)
+ [Dialogflow RPC reference](https://cloud.google.com/dialogflow-enterprise/docs/reference/rpc/)

## QuickStart
+ [I don't want to understand, just get me started](#QuickStart)

## Steps
* [Installing gcloud](#InstallGcloud)
* [Set up Configuration Account](#setConfigAccount)
* [Creating a project](#CreateProject)
* [Enabling Services](#EnableServices)
* [Creating a Service Account](#CreateServiceAccount)
* [Activating a service account](#ActivateServiceAccount)
* [Set credentials environment variable](#SetEnvironmentVariable)
* [Create Dialogflow agent](#CreateAgent)
* [Using the Python Client library](#PythonClient)

<a name="QuickStart"></a>

## QuickStart
**Note**: The following script to get you started asks for sudo permission for some 
commands. As a general rule, it's probably smarter to check out what commands are being
run with sudo permission just to be safe. I'd recommend at least checking out what is 
being run before running it in the nature of fostering good habits. 

### Quick Explanation

By going through the following instructions you will have:
+ Downloaded the Google Cloud Platform command-line interface
+ Enabled the Google Cloud SDK for an email account.
+ Created a Google Cloud project
+ Created a Google Cloud service Account
+ Downloaded pip
+ Downloaded virtualenv
+ Created a virtual environment for Python
+ Installed the Python dialogflow client library in a virtual environment
+ Created a Dialogflow account
+ Created a Dialogflow agent


1. Clone the repository.
`git clone https://github.com/AlexSissoko/dialogflowMemories`

1. Open up **setup.sh**. Fill in the 4 given variables with your chosen values. Save. Exit.
    * **mainAccountName** should be a valid email address.
    * **projectId** must have only lowercase letters, hyphens, or numbers.
    * **serviceAccountName** must have only lowercase letters, hyphens, or numbers.
    * **envName** Whatever you want it to be.
2. Make sure **setup.sh** is executable. 
  If not, `chmod 700 setup.sh`
3. Run `./setup.sh`. Follow any instructions you are given when prompted. 
4. Follow the instructions at [Create Dialogflow Agent](#CreateAgent)
5. Huzzah! You're ready to go!

## Steps
<a name="InstallGcloud"></a>

### Installing gcloud
Refer to [Install gcloud](https://cloud.google.com/sdk/docs/downloads-apt-get) for more
detailed explanations of the following instructions.

1. `export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"`

2. `echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list`

3. `curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -`

4. `sudo apt-get update && sudo apt-get install google-cloud-sdk`

<a name="setConfigAccount"></a>

### Set up Configuration Account
Refer to [Gcloud config](https://cloud.google.com/sdk/gcloud/reference/config) and 
[Gcloud auth](https://cloud.google.com/sdk/gcloud/reference/auth/) for more
detailed explanations of the following instructions.

1. Peek at the current configuration. 
`gcloud config list`

The output should be: 
```
[core]
disable_usage_reporting = True
Your active configuration is: [default]
```

2. Set the main email address/account you want to use as the owner of your project.
`gcloud config set account [email-address]`

3. Active the gcloud sdk for your account.
`gcloud auth login`

This will take you to your default web browser. You will need to log in to your account/email.
Follow the instructions when prompted.

<a name="CreateProject"></a>

### Creating a project
Refer to [Create Project](https://cloud.google.com/sdk/gcloud/reference/projects/create) 
for more detailed explanations and examples.

1. `gcloud projects create [NewProject-ID]`

2. `gcloud config set project [NewProject-ID]`

This just changes the default configuration. If you want to initialize a new configuration, then:

1. `gcloud init`
2. Choose "Create a new configuration"
3. Enter new configuration name
4. Choose a configuration account
5. Choose newly created project

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
 
3. Enable dialogflow as well as some permission/credential apis for the project.
    ```
    gcloud services enable \
    iam.googleapis.com \
    iamcredentials.googleapis.com \
    dialogflow.googleapis.com
    ```

<a name="CreateServiceAccount"></a>

### Creating a service account
Refer to [Service Accounts](https://cloud.google.com/iam/docs/creating-managing-service-accounts)
for more detailed explanations and examples.

1. `gcloud iam service-accounts create [SA-NAME] --display-name "[SA-DISPLAY-NAME]"`

There should be a response saying that the account was created. To see what accounts there
are in a particular project, run `gcloud iam service-accounts list`.

2. Move to whichever directory you want to hold your service account key. Run:
    ```
    gcloud iam service-accounts keys create ./key.json \
        --iam-account [SA-NAME]@[PROJECT-ID].iam.gserviceaccount.com
    ```
There should be a response saying that the key was created.

3. Run:
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

5. Add a role to your service account.
    ```
    gcloud projects add-iam-policy-binding [PROJECT-ID] \
	--member serviceAccount:[SA-NAME]@[PROJECT-ID].iam.gserviceaccount.com --role roles/[roleType]
    ```
  
Typical role value should be `dialogflow.client` as [roleType].
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
This sets the service account as the account for your current configuration.

<a name="SetEnvironmentVariable"></a>

### Set credentials environment variable 
Refer to [Enterprise Quickstart](https://cloud.google.com/dialogflow-enterprise/docs/quickstart).

`export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"`

Where PATH is the path to the service account key file (e.g. ~/key.json)

Remember that this only applies to the current shell session. You will need to reinitialize this
variable each time unless you put a command in your bashrc.

<a name="CreateAgent"></a>

### Create Dialogflow agent
If at this point, you do not yet have a dialogflow agent associated with the project, create one.
Refer to [Enterprise Quickstart](https://cloud.google.com/dialogflow-enterprise/docs/quickstart)
to create an enterprise edition agent. 

1. Go to [Dialogflow](https://dialogflow.com/)
2. Select **Go to Console**
3. Log in/create account with the same email address you used in creating your Google Cloud project. 
4. In the top left corner, under the Dialogflow logo, there should be some buttons that you can
press in order to start the process to create a new agent. This will be left as an exercise 
for the reader. 
5. Choose agent name. Choose default agent language. Choose default agent time zone.
6. In the Google Project section click the **Create a new Google Project** segment. Under 
**OR IMPORT AN EXISTING PROJECT**  you should see the project you just created. Select it.
7. Press the blue **CREATE** button.

<a name="PythonClient"></a>

### Using the Python client library.
I used the Python client library. If you want to use a different language, refer to 
[Client Libaries](https://cloud.google.com/dialogflow-enterprise/docs/reference/libraries/overview).
Refer to [pypi](https://pypi.org/project/pip/) for more information about pip, 
and [Virtualenv](https://virtualenv.pypa.io/en/stable/) for more information about 
virtualenv.

**Note**: This is for Python 2.7, but it should work pretty similarly for python3.

1. Install pip: `sudo apt-get install python-pip`
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
