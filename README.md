# My_shop
## To install and run:
1. git pull
2. copy .env.sample file to .env file( create ourself )
3. docker-compose build
4. docker-compose up
5. docker exec -it my_shop_app_1 bash:
   1. python manage.py createsuperuser
   2. python manage.py migrate

docker required. To install visit official site
