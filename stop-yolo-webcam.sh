#!/bin/bash

cont_name="cont-webcam"
docker compose -p $cont_name down 2> /dev/null
