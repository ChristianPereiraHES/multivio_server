#
# Multivio docker build
#
FROM debian:stretch-slim
MAINTAINER Johnny Mariéthoz <Johnny.Mariethoz@rero.ch>

# Node.js, bower, less, clean-css, uglify-js, requirejs
RUN apt-get update
RUN apt-get -qy upgrade --fix-missing --no-install-recommends

# Install dependencies
RUN apt-get -qy install --fix-missing --no-install-recommends \
    g++ cmake make git python3 python3-dev python3-pip python3-setuptools\
    fontconfig libfontconfig1-dev zlib1g-dev libpng-dev lib32z1-dev\
    libjpeg-dev libtiff-dev libopenjp2-7-dev \
    libapache2-mod-wsgi apache2 wget unzip 

RUN pip3 install Cython
RUN pip3 install pillow
WORKDIR /code

# Poppler
RUN git clone git://git.freedesktop.org/git/poppler/poppler 

WORKDIR /code/poppler

RUN mkdir -p /code/poppler/build && cd /code/poppler/build \
	&& cmake -Wno-dev -D ENABLE_XPDF_HEADERS=True ../ \
    	&& make -j 2 install

# make libpoppler globally available
RUN ldconfig /usr/local/lib

# Multivio server
COPY . /code/multivio
WORKDIR /code/multivio

# Basic Python
RUN pip3 install --upgrade pip setuptools \
	#install multivio
	&& pip install --global-option=build_ext .

# apache
RUN mkdir -p /var/log/multivio /var/tmp/multivio /var/www/multivio/server \
    && cp tools/multivio_server.py /var/www/multivio/server \
    && cp tools/mvo_config_apache.py /var/www/multivio/server/mvo_config.py \
    && chown www-data:www-data /var/log/multivio /var/tmp/multivio /var/www/multivio \
    && cp tools/multivio.conf /etc/apache2/sites-available/ \
    && a2ensite multivio

# apache sript
RUN cp scripts/httpd-foreground /usr/local/bin \
    && chmod a+x /usr/local/bin/httpd-foreground

WORKDIR /var/www/multivio/client
RUN wget http://demo.multivio.org/multivio/client_1.0.0.zip \
    && unzip client_1.0.0.zip \
    && mv client_1.0.0/* . \
    && rm -fr client_1.0.0 client_1.0.0.zip \
    && chown -R www-data:www-data /var/www/multivio/client


CMD ["httpd-foreground"]
