# AppFlowy-AI

## Installation
Install all the required packages using the following command:
```shell
pip install -r requirements.txt
```

copy `.env.example` to `.env` and update the values in the file.


## Development 
You can run `./run pip3:outdated to get a list of
outdated dependencies based on what you currently have installed. Once you've
figured out what you want to update, go make those updates in your
`requirements.txt`

### Run the tests:
```shell
pip3 install pytest
./run test
```

### Linting the code base:

```sh
# You should get no output (that means everything is operational).
./run lint
```

### Sorting Python imports in the code base:

```sh
./run format:imports
```

### Formatting the code base:

```sh
# You should see that everything is unchanged (it's all already formatted).
./run format
```
