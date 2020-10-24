# Congo Project JSON renderer

An application that provides the endpoint for the customizable JSON file for the congo project

## Setup

To setup,

1. You can clone the repository using the link [here](https://github.com/myrdstom/read-file.git)
    ```
    $ git clone https://github.com/myrdstom/Store-Manager
    ```    

2. Download and install python 3.6 or higher

3. Install pip [here](https://pip.pypa.io/en/stable/installing/)

4. Switch to the directory that you have just cloned and set up a virtual-environment
    ```
    $ cd store manager
    $ pip install virtualenv
    $ Linux and MacOS users : virtualenv --python=python3 venv
    $ Windows users: virtualenv venv
    $ Linux and MacOS users: source venv/bin/activate
    $ Windows users: cd venv/scripts/activate  
    ```    
5. Move to the root directory of the project

6. Install all dependencies in the ```requirements.txt``` to finalise setting up the environment.
    ```
    pip install -r requirements.txt   
    ``` 
7. Place the file in the same directory as project directory. The name of the file should be```menuItems.json```

## Build

1. Run the file run.py``` python run.py ``` in the root directory and follow  the prompts

## The endpoint:
| End Point  | Description |
| ------------- | ------------- |
|GET /api/v1/uploads | Returns the JSONified version of the file