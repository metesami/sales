FROM python:3.9

#working directory in container
WORKDIR /app

COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script into the container
COPY transfer_sales_data.py .

# run the Python script
CMD ["python", "transfer_sales_data.py"]
