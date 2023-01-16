# To start

```shell
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
# To run app
flask --app app/main run
# How to get and init api key
1) Go to https://fdc.nal.usda.gov/api-key-signup.html
2) Fill the form and get api key
3) Use .env.example to create a .env file and insert
 your api key
```