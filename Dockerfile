FROM python:alpine

EXPOSE 80

# Install waitress
RUN pip install waitress

# Install falcon
RUN pip install falcon

# Add demo app
COPY . /app
WORKDIR /app

CMD ["waitress-serve", "--port", "80", "main:api"]
