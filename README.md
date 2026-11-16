# General Knowledge Bot Website

This is a website for the [General Knowledge Discord Bot](https://github.com/Piwy-dev/general-knowledge-bot)

## Add the bot to your server

Add the bot to your server by clicking [here](https://discord.com/oauth2/authorize?client_id=803979491373219840&permissions=8&scope=bot%20applications.commands).

## Contributing
### Pre-requisites
Make sure you have created a virtual environment and installed the dependencies.

For this example I will use `uv` (https://github.com/astral-sh/uv) to create a virtual environment, but you can use any other tool you prefer.

```bash
uv venv .venv
. .venv/bin/activate
uv pip install -r requirements.txt
```

### Running the website

First, activate the virtual environment:
```bash
. .venv/bin/activate
```

Then, run the following command to start the website:
```bash
flask run
```

The website will be available at http://localhost:5000/.