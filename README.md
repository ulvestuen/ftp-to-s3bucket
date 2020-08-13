# ftp-to-s3bucket
### Prerequisites for running the ftp-to-s3bucket integration
* Clone the source code of `ftp-to-s3bucket` from the [ftp-to-s3bucket GitHub-repository](https://github.com/ulvestuen/ftp-to-s3bucket) 
##Run on host machine
### Setup
The `ftp-to-s3bucket` integration relies on the following
environmental variables:
```
export FTP_USERNAME=...
export FTP_PASSWORD=...
export FTP_IP_ADDRESS=...
export FTP_PORT=

export S3_BUCKET_NAME=...
export S3_UPLOAD_INTERVAL=60

export AWS_REGION=...
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
```

From within the `ftp-to-s3bucket/` folder, first create a python virtual environment:
```
python3 -m venv env
```
Activate the python virtual environment:
```
source env/bin/activate
```
Install dependencies:
```
pip install -r requirements.txt
```

### Start the application
```
python3 application.py
```

## Run with docker
### Prerequisites
* Make sure to have docker installed: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
* Get an `ftp-to-s3bucket` docker image
  * Alternative A: Pull the latest pre-built docker container with `docker pull ulvestuen/ftp-to-s3bucket`
  * Alternative B: From the `/ftp-to-s3bucket` folder, run the following command to build a local docker image:
`docker build -t ftp-to-s3bucket:latest .`

### Setup
In the file `docker-compose.yml` configure appropriate values for environment variables that is 
defined in the container. Define the port mapping to  Also consider changing image reference based on your choice of Alternative
A or B from Prerequisites above.

### Start the application
From the `ftp-to-s3bucket/` folder, start the test environment:
```
docker-compose up -d
```