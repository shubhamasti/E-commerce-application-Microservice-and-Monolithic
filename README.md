## Monolithic E-commerece application

## How to run
Make sure to change mysql password


### Install all requirements
```bash
pip install -r requirements.txt
```


### Run database.sql to initialze database
```bash
mysql -u root -p < database.sql
```


#### Run insert script
```bash
python insertproducts.py
```

#### Run with flask to start application
```bash
python app.py
```