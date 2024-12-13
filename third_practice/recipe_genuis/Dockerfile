FROM python:3.12

ENV DJANGO_SETTINGS_MODULE=recipe_genuis.settings

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN pip install pytest 
RUN pytest

CMD ["gunicorn", "-b", "0.0.0.0:8000", "recipe_genuis.wsgi"]