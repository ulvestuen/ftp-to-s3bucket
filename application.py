import subprocess


def startFtpServer():
    pid = subprocess.Popen(
        ["python3", "ftp_server.py"]).pid
    return "Started FTP server with pid: " + str(pid)


def startS3Uploader():
    pid = subprocess.Popen(
        ["python3", "s3_uploader.py"]).pid
    return "Started S3 uploader with pid: " + str(pid)


print(startFtpServer())
print(startS3Uploader())
print("Started ftp-to-s3bucket integration...")
