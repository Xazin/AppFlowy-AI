# AppFlowy-AI

## Installation

### Prerequisites

- Python 3.x

### Setup

1. Install all required Python packages using the following command:
```shell
pip install -r requirements.txt
```

2. Copy the .env.example file to .env and update the values to match your local environment:
```shell
cp .env.example .env
```

## Development
You can run `./run pip3:outdated` to get a list of outdated dependencies based on what you currently
have installed. Once you've figured out what you want to update, go make those updates in your
`requirements.txt`


### Run Python Test:
1. Install pytest (if not already installed):
```shell
pip3 install pytest
```
2. Execute the tests:
```shell
./run test
```

### Run Client API Test
Ensure that you have configured the .env file with the correct values and that the server is running before executing the tests.
1. start the local development server:
```shell
./run start_server
````
2. Run the tests:
```shell
cd libs/appflowy-ai-client && cargo test
```

## Code Quality Tools

### Linting the code base:
install prerequisites:
```shell
pip install flake8 isort black
```

```sh
# You should get no output (that means everything is operational).
./run lint
```

### Sorting Python imports:

```sh
./run format:imports
```

### Formatting the code base:

```sh
# You should see that everything is unchanged (it's all already formatted).
./run format
```
