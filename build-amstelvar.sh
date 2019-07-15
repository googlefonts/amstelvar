#!/bin/bash

# open terminal, type: sh build.sh


printf "Build fonts…\n"


if ! python "build-amstelvar.py"


    then
        printf "Unable to run pyhon script.  Build canceled." 1>&2
        exit 1
fi





printf "\nBuild complete"