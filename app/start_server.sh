#bin/bash
#gunicorn -w 4 -b 127.0.0.1:8000 api:app &> /dev/null &
gunicorn -w 4 -b unix:/tmp/resources.sock -m 005 api:app &> /dev/null &
#gunicorn -w 4 -b 0.0.0.0:5000 api:app &> /dev/null &
disown
