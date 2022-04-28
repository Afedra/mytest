[![Coverage Status](https://coveralls.io/repos/github/Afedra/mytest/badge.svg)](https://coveralls.io/github/Afedra/mytest)

## Documentation 
We shall install using the following commands:

python3 -m pip install -r requirements.ini
<!-- Start django project -->
python3 -m django startproject mytest 
<!-- creates django application -->
python3 -m django startapp users
python3 manage.py makemigrations 
python3 manage.py migrate
python3 -m coverage run --source=mytest --omit='*tests*,*migrations*,*admin*,*mytest*' -m py.test -v --tb=native


