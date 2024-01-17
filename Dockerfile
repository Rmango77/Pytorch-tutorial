FROM python:3.8

EXPOSE 8501


COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY src /src/

CMD streamlit run /src/app.py
