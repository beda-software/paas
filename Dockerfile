FROM python:2.7-alpine
RUN apk add --no-cache gcc libffi-dev musl-dev openssl-dev
RUN pip install ansible fabric
ENV APP_PATH /app/user
RUN mkdir -p $APP_PATH
ADD . $APP_PATH
WORKDIR $APP_PATH
ENTRYPOINT ["fab"]
