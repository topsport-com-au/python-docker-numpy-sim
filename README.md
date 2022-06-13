python-docker-project
===

Python & docker Hello, World! application.

### Requirements

* Docker

#### Setup

Copy `.env.example` to `.env`

#### Run
`$docker-compose run --rm app python src/app/main.py 13 32 55`
`$docker-compose run --rm app simulate 13 32 55`

#### Run Tests
`$ docker-compose run --rm app scripts/tests`
