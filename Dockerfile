FROM rhlobo/base-bigtempo

MAINTAINER Roberto Lobo <rhlobo@gmail.com>


# PREPARATING BASE IMAGE
## Setting environment variables
ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive
## Disabling SSH access
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh


# INSTALLING SERVICES
RUN add-apt-repository --yes ppa:nginx/stable &&\
	apt-get --quiet update &&\
	apt-get install --yes --quiet build-essential \
		git \
		software-properties-common \
		python-software-properties \
		python python-dev python-setuptools \
		python-pip \
		nginx \
		supervisor \
		sqlite3 &&\
	pip install uwsgi


# COPY APP FILES
ADD . /home/docker/files/


# CONFIGURATING
## APP CONFIGURATION
ENV PATH /home/docker/files/bin:$PATH
## Configurating NGINX
RUN echo "daemon off;" >> /etc/nginx/nginx.conf &&\
	rm -Rf /etc/nginx/sites-enabled/default &&\
	ln -s /home/docker/files/infra/nginx-app.conf /etc/nginx/sites-enabled/ &&\
	ln -s /home/docker/files/infra/uwsgi_params /etc/nginx/sites-enabled/
## Configurating SUPERVISOR
RUN ln -s /home/docker/files/infra/supervisor-app.conf /etc/supervisor/conf.d/
## Configurating application dependencies
RUN pip install -r /home/docker/files/requirements.txt &&\
	pip install flask-bigtempo


# SERVICE INITIALIZATION
CMD ["supervisord", "-n"]


# EXPOSING SERVICES
EXPOSE 80


# CLEAN UP
## Cleaning up APT
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*