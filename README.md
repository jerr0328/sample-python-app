# sample-python-app
Sample app to show off building a Python/Docker app in Infrabox

## Dev/Tests

Use Docker:

1. Build the Docker image:
    ```bash
    docker build -t test-sample-app -f tests/Dockerfile .
    ```
2. Run the tests:
    ```bash
    docker run -it --rm -v $PWD:/usr/src/app test-sample-app
    ```


## Run application

1. Build the Docker image:
    ```bash
    docker build -t sample-app .
    ```
2. Run the tests:
    ```bash
    docker run -it --rm sample-app
    ```
