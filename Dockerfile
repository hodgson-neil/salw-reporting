FROM python:3.6

# ssh
ENV SSH_PASSWD "root:Docker!"
RUN apt-get update \
        && apt-get install -y --no-install-recommends dialog \
        && apt-get update \
    && apt-get install -y --no-install-recommends openssh-server \
    && echo "$SSH_PASSWD" | chpasswd

COPY sshd_config /etc/ssh/
COPY init.sh /usr/local/bin/

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

# CHANGE!!! should be passed in a secrets using the CI tool
ENV DJANGO_SU_NAME admin
ENV DJANGO_SU_EMAIL admin@admin.org
ENV DJANGO_SU_PASSWORD admin

RUN chmod u+x /usr/local/bin/init.sh
EXPOSE 8000 2222
ENTRYPOINT ["init.sh"]
