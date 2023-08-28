# Grinta Backend Test

## Local Setup
1. Clone repository 
    ```
    git clone  https://github.com/khaled5321/grinta.git
    ```
2. Create virtual environment
    ```
    python3 -m venv venv
    ```
3. Activate virtual environment
    ```
    ./env/bin/activate or ./venv/scripts/activate.ps1
    ```
4. Install requirements
    ```
    pip install -r requirements.txt
    ```
5. Migrate to database
    ```
    python manage.py migrate
    ```
6. Run server
    ```
    python manage.py runserver
    ```
---

> To run cronjob
> ```
> python manage.py runtask process_scheduled_payments
> ```
> To register cronjob with crontab
> ```
> python manage.py installtasks
> ```