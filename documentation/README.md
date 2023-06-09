
[Gender Recognition Certificate service](../README.md) >
Developer documentation

# Developer documentation

Information for new developers:

* [Accounts you will need to develop the service](Accounts_you_will_need_to_develop_the_service.md)
* [Software to install](Software_to_install.md)
* [Getting the code running](Getting_the_code_running.md)

Environments and deployments:
* [Our environments](Our_environments.md)
* [Hosting and live databases](Hosting_and_live_databases.md)
* [Deployments](Deployments.md)
* [HTTP Basic Authentication](HTTP_Basic_Authentication.md)
* [Domain names and IP restrictions](Domain_names_and_IP_restrictions.md)

Database:
* TODO Database migrations

Other:
* [Backing up the database and files externally to Gov.UK PaaS](External_backups.md)
* [ClamAV virus scanning on Gov.UK PaaS](ClamAV.md)
* [Rotating encryption keys](Rotating_encryption_keys.md)
* [Useful commands](Useful_comands.md)

How-to:
* [How to put the service into Maintenance Mode / "Service unavailable"](Maintenance_mode.md)

# Miscellaneous documentation
**Note: If we have time, we could put the following documentation into other sub-files.**

### Technical diagnostic pages

The Admin portal contains some technical diagnostic pages.  
You will need to have an account on the Admin portal and have your IP address added to the allow list.  
Once you have access, you can [find the diagnostic pages here](admin.apply-gender-recognition-certificate.service.gov.uk/diagnostics)


## Help Section
. venv/bin/activate

pip3 install Flask
pip3 freeze | grep Flask >> requirements.txt
pip3 freeze >> requirements.txt

pip list --format=freeze

pip3 freeze requirements.txt


https://docs.cloud.service.gov.uk/deploying_services/s3/#connect-to-an-s3-bucket-from-outside-of-the-gov-uk-paas
`cf service-key grc-s3-dev grc-s3-dev-key`
