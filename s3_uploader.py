import sched
import time
from os import listdir, getenv

import boto3


def uploadFiles():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(getenv('S3_BUCKET_NAME'))
    for filename in listdir('files'):
        with open('files/' + filename, 'rb') as data:
            key = filename
            bucket.put_object(
                Key=key,
                Body=data,
                ContentType='image/png',
                Metadata={
                    'Content-Type': 'image/png'
                }
            )
            object_acl = s3.ObjectAcl(getenv('S3_BUCKET_NAME'), key)
            object_acl.put(ACL='public-read')


s = sched.scheduler(time.time, time.sleep)
last_time = time.time()


def nextTime():
    global last_time
    return last_time + float(getenv('S3_UPLOAD_INTERVAL'))


def updateLastTime():
    global last_time
    last_time = nextTime()


def uploadAndScheduleNextUpload(sc):
    global last_time
    updateLastTime()
    print(str(last_time) + ": Uploading files...")
    uploadFiles()
    s.enterabs(nextTime(), 1, uploadAndScheduleNextUpload, (sc,))


s.enterabs(nextTime(), 1, uploadAndScheduleNextUpload, (s,))
s.run()
