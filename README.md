# Gunzpedia API usage
## Requirements
```
python3
django
django-cors-headers
djangorestframework
```

Install python3, clone/download this repository. Navigate to the root of `Gunzpedia` and run `pip install -r requirements.txt`. 

## Usage
To run, execute the following command: `python manage.py runserver`

The following urls are now accessible:
```
localhost:8000/api/
localhost:8000/api/players/
localhost:8000/api/clans/
localhost:8000/api/clan_members/
localhost:8000/admin/
```

To create an administrative account, you must run the following command: `python manage.py createsuperuser`, then follow the prompt accordingly.
