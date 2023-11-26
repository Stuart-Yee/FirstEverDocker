# FirstEverDocker
My very first docker container

Instructions
- Clone repo
- Navigate into `/container1`
- Build image -> `docker build -t {container name} .`
- Run container -> `winpty docker run -it {container name}`

This runs a very basic Python CLI that accepts any input. If the input is `q` or `Q`, the program closes and so does the container.

Optionally, while CLI is running, open another terminal in the `/container` directory and see the running container with `docker ps` or `docker ps -q`

![image](https://github.com/Stuart-Yee/FirstEverDocker/assets/75331586/058945ac-fa13-469c-968d-493d521ca828)
