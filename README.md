# Timestamped UUID Generator

A simple API that returns a key-value pair of timestamp and randomly generated UUID.

## Requirement

- Python >= 3.8

## Installation

To install the project, please run the following commands:

`python3 -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`python manage.py migrate`

`python manage.py runserver`

The API URL can be accessed at `127.0.0.1:8000`

## Sample Response

```json
{
  "2022-01-19 21:50:31 937579": "785bc9f6524d4fe3ac8efdde6fcb2706",
  "2022-01-19 21:50:30 764814": "d51fec251cbc49dd8724a7cd399cb1a3",
  "2022-01-19 21:50:29 199668": "d9a880093d35464ab0389c38346ce44b",
  "2022-01-19 21:44:41 140168": "7a2a959c68fc4f8cbf58439ae7871225",
  "2022-01-19 21:44:40 150272": "1afd0edc37bf40a99cf84c93d59d68e8"
}
```
