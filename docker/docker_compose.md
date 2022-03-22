# docker compose
  ------


#### 1. Simple example
  ```yml
    version: 3.7
    services:
      web:
        image: nginx
        ports:
          - "8000:80"
  ```
  This  file creates a service named "web" based on nginx image, redirect all request from local port 8000 to port 80 in the container.


#### 2. Less simple example
  ```yml
    version: 3.7
    services:
      app: # first service
        build:  # use a custom build based on Dockerfile
          context: ./ # context set a the current directory
          dockerfile: Dockerfile
        image: travellist # service based on "travellist" image
        container_name: travellist-app # name of the service
        restart: unless-stopped #mean that the container will restart unless it is stopped
        working_dir: /var/www # application located in this dir
        volumes:
          - ./:/var/www # we are sharing current dir in host with working dir in container
        networks:
          - travellist
      nginx: # second service
        image: nginx:1.17-alpine # based on nginx image
        container_name: travellist-nginx
        restart: unless-stopped
        ports:
          - 8000:80
        volumes:
          - ./:/var/www
          - .docker-compose/nginx:/etc/nginx/conf.d
        networks:
          -travellist
      db: # third service (mysql)
        image: mysql:5.7
        container_name: travellist-db
        restart: unless-stopped
        environment: # defining environment variable
          MYSQL_DATABASE: ${DB_DATABASE} # come from dot env file from app
          MYSQL_ROOT_PASSWORD: ${DB_PASSWORD}
          MYSQL_PASSWORD: ${DB_PASSWORD}
          MYSQL_USER: ${DB_USERNAME}
          SERVICE_TAGS: dev
          SERVICE_NAME: MYSQL_USER
        volumes:
          - ./docker-compose/mysql:/docker-entrypoint-initdb.d
        networks:
          - travellist
  ```
  ```
    # Dockerfile
    FROM php:7.4-fpm
    ARG uid=1000
    ARG user=perthuis
    RUN apt-get update && apt-get install -y \
      git \
      curl \
      libpng-dev \
      libonig-dev \
      libxml2-dev \
      zip \
      unzip \
    RUN apt-get clean && rm -rf /var/lib/apt/lists/*
    RUN docker-php-ext-install pdo_mysql mbstring exif pcntl bcmath gd

    RUN useradd -G www-data, root -u $uid -d /home/$user $useradd
    RUN mkdir -p /home/$user/.composer && chown -R $user:$user /home/$user
    COPY --from=composer:lastest /usr/bin/composer /usr/bin/composer
    WORKDIR /var/www
    USER $user

  ```
