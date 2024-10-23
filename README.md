# How to use google bigtable.

## Quick Setup

~~~
docker run --name=bigtable -dp 127.0.0.1:8086:8086 --rm -e BIGTABLE_EMULATOR_HOST=localhost:8086 -ti google/cloud-sdk:alpine gcloud beta emulators bigtable start --host-port=0.0.0.0:8086
~~~ 

~~~
docker exec bigtable sh -c "echo project = project-id > ~/.cbtrc  && echo instance = quickstart-instance >> ~/.cbtrc"
docker exec bigtable sh -c "gcloud components install cbt"
~~~



