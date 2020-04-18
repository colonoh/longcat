# longcat
URL shortener 

## Installation
1. Download and install docker-composer
1. Build with `docker-compose build`
1. Start Docker with `docker-compose up`
1. Django admin can be found at http://0.0.0.0:8000/admin/sluggen

## Notes
To run the tests (and get a code coverage report), run `docker-compose run web coverage run --source='sluggen/' manage.py test`.