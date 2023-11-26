# FirstEverDocker
My very first docker container

Instructions
- Clone repo
- Navigate into `/container1`
- Build image -> `docker build -t {container name} .`
- Run container -> `winpty docker run -it {container name}`

This runs a very basic Python CLI that accepts any input. If the input is `q` or `Q`, the program closes and so does the container.