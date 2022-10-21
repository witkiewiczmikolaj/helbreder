FROM python:3.8

WORKDIR /helbreder
COPY . .

RUN apt update
RUN pip install --no-cache-dir -r ./env/requirements.txt

RUN echo "deb https://deb.nodesource.com/node_16.x buster main" > /etc/apt/sources.list.d/nodesource.list \
	&& wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - \
	&& apt update \
	&& apt install nodejs \
	&& npm install --global curlconverter

ENTRYPOINT ["./init/init.sh"]
