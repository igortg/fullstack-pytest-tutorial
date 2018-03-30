# Full-stack pytest tutorial

Sample project showcasing how to use [pytest](https://docs.pytest.org) on all layers
of a full-stack project.

### Installing

    git clone https://github.com/igortg/fullstack-pytest-tutorial.git
    cd fullstack-pytest-tutorial\toh-server
    pip install -r requirements.txt
    export PYTHONPATH=$PWD
    cd toh-ui
    npm install
    

### Running back-end tests

    pytest toh-server
    
### Running end-to-end tests

    cd toh-ui
    npm install
    npm run all
    cd ..
    
    pytest e2e  

**Talk at Python Sul**

https://gitpitch.com/igortg/fullstack-pytest-tutorial/pythonsul-talk
