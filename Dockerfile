# When docker image is built from this file, the image bundles the latest version of Python 3, which is available under
# a "PSF" license. For details, see https://docs.python.org/3/license.html

FROM python:3

RUN groupadd -g 999 ftp-to-s3bucket && \
    useradd -r -u 999 -g ftp-to-s3bucket ftp-to-s3bucket

ADD --chown=ftp-to-s3bucket:ftp-to-s3bucket ./ src/
WORKDIR /src

USER ftp-to-s3bucket
ENTRYPOINT ["/bin/bash","entrypoint.sh"]