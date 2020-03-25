A simple configuration for using Flask and Docker Compose, which ticks the following boxes:

- Launch in production mode, with source code baked into the image.
- Launch in development mode with auto reloader enabled, and source code mounted via bind mount.
- Load (secret) environment variables from `.env-prod` or `.env-dev` file respectively.
---

# Usage
## Pre-reqs

You'll need to create the `.env-prod` and `.env-dev` files manually:

    # .env-prod
    FROM_ENV_FILE='Hey this loaded from prod-env!'

    # .env-dev
    FROM_ENV_FILE='Hey this loaded from prod-env!'

The `.gitignore` file contains a line which prevents these from being committed to the repo.

## Prod

`docker-compose.yml` contains the production config and can be run with:

    docker-compose up

## Dev

`docker-compose-dev.yml` contains the development config, in an [overide file](https://docs.docker.com/compose/extends/) This can be run with:

    docker-compose -f docker-compose.yml -f docker-compose-dev.yml up

On Linux you could make an alias with:

    alias docker-compose-dev='docker-compose -f docker-compose.yml -f docker-compose-dev.yml'

Now launching simply becomes:

    docker-compose-dev up

# Background

## Prod 

Some significant parts of the `docker-compose.yml` (prod) file are:

    environment:
      - FLASK_ENV=production
    env_file:
      - .env-prod
    command: gunicorn --bind '0.0.0.0:5000' app:app

In prod, this launches the app with `gunicorn`,  There is no volume mount in this file, so the source code which is run is that which is baked into the image.  Therefor to take account of the latest changes to your code, prior to launching in prod with `docker-compose up` you'll need to do `docker-compose build`

## Dev

Some significant parts of the `docker-compose-dev.yml` (dev) file are:

    environment:
      - FLASK_ENV=development
    env_file:
      - .env-dev
    command: flask run -h 0.0.0.0
    volumes:
      - ./code:/code

These values overide those specified in the prod compose file, so secrets are loaded from the `.env-dev` file instead, and the server runs in dev mode which enables the live reloader.  Because of the volume mount, you can edit the code, and the server should reload when changes happen.