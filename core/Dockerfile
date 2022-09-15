FROM python:3.8

WORKDIR /helbreder
COPY . .

RUN apt update
RUN pip3 install -r ./env/requirements.txt

ENTRYPOINT ["./init/init.sh"]