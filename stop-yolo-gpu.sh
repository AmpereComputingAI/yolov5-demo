#!/bin/bash

cont_name="cont-gpu-1"
docker compose -p $cont_name down 2> /dev/null

cont_name="cont-gpu-2"
docker compose -p $cont_name down 2> /dev/null

cont_name="cont-gpu-3"
docker compose -p $cont_name down 2> /dev/null

cont_name="cont-gpu-4"
docker compose -p $cont_name down 2> /dev/null
