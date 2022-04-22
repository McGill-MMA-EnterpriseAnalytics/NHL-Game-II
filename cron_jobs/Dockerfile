FROM python:3.7
RUN apt-get update && apt-get -y install cron vim
EXPOSE 8000
COPY . /usr/app/
WORKDIR /usr/app/
RUN pip install -r requirements.txt
COPY crontab /etc/cron.d/crontab
COPY model.py /app/model.py
COPY classifier.pkl /app/classifier.pkl
RUN chmod 0644 /etc/cron.d/crontab

# run crond as main process of container
CMD ["cron", "-f"]