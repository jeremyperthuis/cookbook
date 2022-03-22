# docker basic
  ------

  ```bash

  # Get image (example with postgres):
  docker pull postgres

  # List images
  docker images

  # Delete all images
  docker rmi $(docker images -q)

  # List active containers
  docker container ls
  # List all containers
  docker container ls -a

  # Stop container
  docker stop CONTAINER_ID
  # Stop all containers
  docker stop $(docker ps -a -q)

  # Delete container
  docker container rm CONTAINER_ID
  # Delete all containers
  docker rm $(docker ps -a -q)

  # Get into containers
  docker exec -it CONTAINER_ID bash


  # Copy file into (stopped) container
  docker cp path/to/file CONTAINER_ID:/path
  ```
