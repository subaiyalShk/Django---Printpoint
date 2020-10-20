# Django - Printpoint website + CRM      
![Django - Printpoint website + CRM](pp.gif?raw=true "Landing page demo")
### <a href="https://printpoint.io/">LIVE DEMO</a> 

## Description
This project is build using Django. It Utilizes django forms, built in authentication and is rendered as a single page application (SPA) using Ajax. This app lets admins create a 'Catalogue' which can contain multiple products. Each product can have a display pic that shows on the catalogue and multiple gallery pics which are visible on the product's detail page. Anon users / visitors can post inquiries on each product which is stored in SQLite DB and rendered on admin dasboard. All user generated media files and static files are uploaded to AWS S3 bucket which can be configured in settings.py The contact form allows anon users to email admin with a general inquiry form. This is done using an SMTP server and settings can be modifed at settings.py. The front end is built using Bootstrap <a href="https://github.com/StartBootstrap/startbootstrap-grayscale">Grayscale Theme</a>. This website is built for a printing and packaging company based in Dallas, TX. 

## Development
### 1. Setup virtual environment 
1. cd {{ repo name }} 
2. ~/myRepoName$ python3 -m venv venv 
3. ~/myRepoName$ source venv/bin/activate
4. ~/myRepoName$ pip install -r requirements.txt
5. create .env file in root directory and add environment variables.
    AWS_ACCESS_KEY_ID=%{{your AWS KEY ID}}
    AWS_SECRET_ACCESS_KEY=%{{your AWS SECRET ACCESS KEY}}
    SECRET_KEY=%{{your Django SECRET KEY }}

    EMAIL_HOST_USER=%{{email address you want to use to send email}}
    EMAIL_HOST_PASSWORD=%{{password for that email address}}
    DEBUG=%True

### 2. Change SMTP server 'email to' address [ core/views.py ]
send_mail(subject, 
            message, 
            'from@email.com', 
            ['recipent@email.com'], 
            fail_silently=False,
            )

### 3. Configure Static files and Media files for development [ {{projectName}}/settings.py ]
comment out line 157 and 158 in settings.py
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

### 4. Register Super User <a href="https://github.com/StartBootstrap/startbootstrap-grayscale">click here for official Django documentation</a>
method 1: from root directory of your project run : python manage.py createsuperuser
method 2: from root directory of your project run : python manage.py shell
    >>> from django.contrib.auth.models import User
    >>> user=User.objects.create_user('foo', password='bar')
    >>> user.is_superuser=True
    >>> user.is_staff=True
    >>> user.save()

### 4. Run development server
Once you have followed through all the steps, run the following from your project root:
python manage.py runserver

## Deployment
The Following steps should be taken after ssh'ing into your deployment machine, installing nginx or apache server and cloning the project repo into your deployment machine.

### 1. Server Configuration
run the following commands:
    ubuntu@54.162.31.253:~$ sudo apt-get install python3-venv
    ubuntu@54.162.31.253:~$ cd {{ project repo name }} 
    ubuntu@54.162.31.253:~/myRepoName$ python3 -m venv venv //We are using the venv command and naming our virtual env venv
    ubuntu@54.162.31.253:~/myRepoName$ source venv/bin/activate
    (venv) ubuntu@54.162.31.253:~/myRepoName$ pip install gunicorn
    (venv) ubuntu@54.162.31.253:~/myRepoName$ pip install -r requirements.txt


### 1. Create Amazon Web Services S3 buckets
1. Give the bucket a unique, DNS-compliant name and select a region
2. On the "Set permissions" page, turn off "Block all public access" THIS IS IMPORTANT

### 2. Create Amazon Web Services IAM Access
1. IAM Group - Within the AWS Console, navigate to the main <a href="https://console.aws.amazon.com/iam/home#/home"> IAM page </a> and click <a href="https://console.aws.amazon.com/iam/home#/groups"> groups </a> on the sidebar. Then, click the "Create New Group" button, provide a name for the group and then search for and select the built-in policy "AmazonS3FullAccess". Click the "Next Step" button and then "Create Group" to finish setting up the group
2. IAM User - Back on the main IAM page, click <a href="https://console.aws.amazon.com/iam/home#/users"> Users </a> and then "Add user". Define a user name and select "Programmatic access" under the "Access type". Click the next button to move on to the "Permissions" step. Select the group we just created. Click next again and then click "Create user" to create the new user. You should now see the user's access key ID and secret access key.

### 3. Configure settings.py [ {{projectName}}/settings.py ]
1. Take Access key Id and secret key that you just created above and place it in your .env file which should be in your projects root directory (if there is no .env file create one and add all your secret environment variables there). Like this:
    AWS_ACCESS_KEY_ID=%{{your AWS KEY ID}}
    AWS_SECRET_ACCESS_KEY=%{{your AWS SECRET ACCESS KEY}}
    EMAIL_HOST_USER=%{{email Id you want to use to send emails}}
    EMAIL_HOST_PASSWORD=%{{password for that email}}
    DEBUG=%False
2. Make sure Boto3 (python library for AWS) is installed in your virtual env by running pip freeze in your terminal.
3. Add your deployment machine's IP address and domain name you plane to use if you have one in ALLOWED_HOSTS. Like this: 
    ALLOWED_HOSTS = ['123.456.78.910', 'yourdomainname.com']
3. Check to see if storages is added in your installed Apps. Like this :
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'core',
        'admindash',
        'catalogue', 
        'storages',
    ]
4. See if AWS S3 Bucket settings are properly defined in settings.py. Uncomment DEFAULT_FILE_STORAGE and STATICFILES_STORAGE. Like this:
    #S3 BUCKETS CONFIG
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY= config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME= 'printpoint-crm-bucket'
    AWS_DEFAULT_ACL='public-read'
    AWS_S3_FILE_OVERWRITE= False
    AWS_QUERYSTRING_AUTH = False

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'



## Credits
##### Coding Dojo
Instructor - <a href="https://www.linkedin.com/in/sadieflick/">Sadie Flick</a> & <a href="https://www.linkedin.com/in/petejung/">Pete Jung</a>

#### HTML & CSS Design Template
<a href="https://github.com/StartBootstrap/startbootstrap-grayscale">Grayscale Theme</a>



