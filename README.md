# AdventureReader

## How To Run

In `AdventureReader` folder:
```
pip install -r requirements.txt -U
```

In `app` folder:
```
python manage.py migrate
python manage.py runserver
```

## About Project:

Platform for writing and reading interactive stories. All stories are divided in story-nodes, that branch further into new nodes. The whole idea of project is to allow multiple users to write one story that can be branched out. Keep in mind that once the node is extended it *cannot* be changed anymore.
