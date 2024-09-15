#dockerdock# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.12.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# Get the Real World example app
#RUN git clone https://github.com/nitishpandey/django-realworld-example-app.git /drf_src

# Set the working directory to /drf
# NOTE: all the directives that follow in the Dockerfile will be executed in
# that directory.
WORKDIR /project/drf_src

RUN ls .

COPY upstox-app upstox-app
COPY fnoappbe fnoappbe
COPY polls polls
COPY requirements.txt .
COPY manage.py .
COPY db.sqlite3 .


# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

VOLUME /drf_src

EXPOSE 8000

#CMD python manage.py makemigrations && python manage.py migrate && 
#CMD python manage.py runserver 0.0.0.0:8000
# CMD ["%%CMD%%"]