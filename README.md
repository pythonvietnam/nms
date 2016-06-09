# The NMS Project
The NMS Project of Python Vietnam

## Environment
* Linux Ubuntu 
* Python version 3.5
* MySQL
	* sudo apt install python3-dev mysql-server libmysqlclient-dev
	* mysql -u root -p
	* create database nms;
	* grant all on nms.* to 'loitd' identified by '123456a@';
* RabbitMQ
    * rabbitmqctl add_user loitd2 password
    * rabbitmqctl add_vhost vh2
    * rabbitmqctl set_permissions -p vh2 loitd2 ".*" ".*" ".*"
    * /etc/init.d/rabbitmq restart

## Installation
* pip install -r requirements.txt
* pip install -r nms/apps/apps_requirements.txt
* configure database at nms/settings/base.py
* python manage.py makemigrations
* python manage.py migrate
* python manage.py runserver 

## Config django-allauth
* update django_site set `domain`='localhost', `name`='NMS' where id=1;
* insert into socialaccount_socialapp(`provider`, `name`, `client_id`, `secret`, `key`) values ('facebook', 'facebook', 'site_id', 'token_key', '');
* insert into socialaccount_socialapp_sites(`socialapp_id`, `site_id`) values (1, 1);

## Config the apps:
	* nms/apps/core/coreconfig.py (autoreload enabled)
	* nms/apps/agent_vh1.py

## Run the project

### Run the website:
	* python manage.py runserver

### Run the core application:
	* cd nms/apps/core
	* python main.py

### Run the agent:
	* cd nms/apps/agent
	* python agent_vh1.py
