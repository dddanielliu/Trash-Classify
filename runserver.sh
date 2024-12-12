#!/bin/bash

# Start a tmux session named "django" and run Django server
tmux new-session -d -s django "cd /root/trash/final/website && python manage.py runserver"
echo "Django tmux session 'django' created and running 'python manage.py runserver'"

# Start another tmux session named "fastapi" and run FastAPI server
tmux new-session -d -s fastapi "cd /root/trash/final/model && uvicorn main:app --host 0.0.0.0 --port 8188 --reload"
echo "FastAPI tmux session 'fastapi' created and running 'uvicorn main:app --host 0.0.0.0 --port 8188 --reload'"
