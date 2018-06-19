# eb-deploy-docker

A command line utility to recreate the behaviour of `eb deploy` for Elastic Beanstalk environments using Docker and Dockerrun.aws.json files.

If you are using Docker you have two ways to deploy:
- Use the AWS Console to upload the Dockerrun.aws.json
- Use `eb deploy` that will upload the source folder to S3 and then deploy using the Dockerrun.aws.json, which is slow

`eb-deploy-docker` will obtain the environment information from `eb` and perform the deploy using the AWS SDK.

## Install

```
pip install eb-deploy-docker
```

## Usage

Deploy using the current directory settings, if `file` is ommited Dockerrun.aws.json will be used. The version will be named using the latest git commit.

```
eb-deploy-docker [file]
```

Also you can specify all the environment information

```
$ eb-deploy-docker -h
usage: eb-deploy-docker [-h] [--version-label VERSION_LABEL]
                        [--profile PROFILE]
                        [--application-name APPLICATION_NAME]
                        [--environment-name ENVIRONMENT_NAME]
                        [--environment-id ENVIRONMENT_ID] [--region REGION]
                        [file]
```
