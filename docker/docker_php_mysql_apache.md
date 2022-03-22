# docker php/mysql/apache
  ------


1. Create directory structure
  ```
    php-project
    ├── docker-compose.yml
    ├── Dockerfile
    └── src
        └── index.php
  ```
2. Complete files as below

  docker-compose.yml
  ```yml
  version: '3.1'
  services:
    php:
      build:
        context: .
        dockerfile: Dockerfile
      ports:
        - 80:80
      volumes:
        - ./src:/var/www/html/

    db:
      image: mysql
      command: --default-authentication-plugin=mysql_native_password
      restart: always
      environment:
        MYSQL_ROOT_PASSWORD: example
      volumes:
        - mysql-data:/var/lib/mysql

    adminer:
      image: adminer
      restart: always
      ports:
        - 8080:8080

  volumes:
    mysql-data:
  ```

  Dockerfile
  ```                                  
  FROM php:7.4-apache
  RUN docker-php-ext-install mysqli
  ```

  index.php
  ```php                             
  <?php
      echo "Docker with php8";

      $mysqli = new mysqli("db", "root", "password", "database1");

      $sql = "INSERT INTO user (numero, name) VALUES(001, 'jean')";
      $result = $mysqli->query($sql);
      $sql = "INSERT INTO user (numero, name) VALUES(002, 'frank')";
      $result = $mysqli->query($sql);
      $sql = "INSERT INTO user (numero, name) VALUES(003, 'stan')";
      $result = $mysqli->query($sql);
      $sql = "INSERT INTO user (numero, name) VALUES(004, 'bertand')";
      $result = $mysqli->query($sql);

      $sql = 'SELECT * FROM user';

      if ($result = $mysqli->query($sql)) {
        while ($data = $result->fetch_object()) {
            $users[] = $data;
        }
      }
      foreach ($users as $user) {
        echo "<br>";
        echo $user->numero . " " . $user->name;
        echo "<br>";
      }
    ?>
  ```

3. Launch docker-compose
  ```bash
    docker-compose up -d
  ```
  index.php can be accesed through `localhost:80`

  php adminer can be accesed through `localhost:8080`

4. Create database and table.
  ```
  Structure :

  +---------------------+
  | Tables_in_database1 |
  +---------------------+
  | user                |
  +---------------------+

  +--------+--------------+------+-----+---------+-------+
  | Field  | Type         | Null | Key | Default | Extra |
  +--------+--------------+------+-----+---------+-------+
  | numero | int          | YES  |     | NULL    |       |
  | name   | varchar(255) | NO   |     | NULL    |       |
  +--------+--------------+------+-----+---------+-------+

  ```
  First get into mysql container
  ```bash
  docker exec -it d6b887033d95 mysql -uroot -p
  ```
  then create Database:
  ```sql
  CREATE DATABASE database1;
  USE database1;
  CREATE TABLE IF NOT EXISTS user (numero INT,name VARCHAR(255) NOT NULL);
  ```
