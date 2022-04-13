
[Gender Recognition Certificate service](../README.md) > Developer documentation

# Developer documentation

Information for new developers:

* [Accounts you will need to develop the service](accounts you will need to develop the service.md)
* [Software to install](Software to install.md)
* [Getting the code running](Getting the code running.md)

Environments and deployments:
* [Our environments](Our environments.md)
* [Hosting and live databases](Hosting and live databases.md)
* [Deployments](Deployments.md)

Database:
* TODO Database migrations

# Miscellaneous documentation
**Note: If we have time, we could put the following documentation into other sub-files.**

```
cf push grc-production -m 1G
```

## Help Section
. venv/bin/activate

pip3 install Flask
pip3 freeze | grep Flask >> requirements.txt
pip3 freeze >> requirements.txt

pip list --format=freeze

pip3 freeze requirements.txt


### How to generate good secret keys
python -c 'import secrets; print(secrets.token_hex())'

https://docs.cloud.service.gov.uk/deploying_services/s3/#connect-to-an-s3-bucket-from-outside-of-the-gov-uk-paas
`cf service-key grc-s3-dev grc-s3-dev-key`