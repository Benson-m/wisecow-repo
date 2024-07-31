FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y fortune-mod cowsay netcat

ENV PATH="/usr/games:${PATH}"

WORKDIR /usr/src/app

COPY wisecow.sh .

RUN chmod +x wisecow.sh

# Expose the port the app runs on
EXPOSE 4499

# Run the script
CMD ["./wisecow.sh"]