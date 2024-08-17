#use a lightwaeight python base image
FROM python:3.9-slim-buster

#set the working directory
WORKDIR /app

#Copy requirements.txt and install system dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

#copy rest of the code
COPY . .

#expose port 8000 for the Django development server
EXPOSE 8000

#command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
