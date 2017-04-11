#! /bin/bash -e

sudo pkill gunicorn
cd /projects/dojo-resources/app
gunicorn -w 4 -b unix:/tmp/resources.sock -m 005 api:app --daemon &> /dev/null
cd /projects/dojo-website/app
gunicorn -w 4 -b unix:/tmp/website.sock -m 005 api:app --daemon &> /dev/null
cd /projects/dojo-docs/app
gunicorn -w 4 -b unix:/tmp/docs.sock -m 005 api:app --daemon &> /dev/null

