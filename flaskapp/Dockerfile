FROM python:3.9
COPY . /app
WORKDIR /app
#RUN python3 -m venv myenv
#RUN source myenv/bin/activate

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]