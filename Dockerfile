FROM python:3

RUN apt update && \
    apt install pipx -y && \
    pipx ensurepath


RUN pipx install poetry && \
    echo "$(pipx get-poetry)" >> ~/.profile
# Load the profile to make poetry available in the current session
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app
COPY  . /app
RUN poetry install

WORKDIR /app/yuhu_challenge


