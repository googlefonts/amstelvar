#!/bin/bash

# open terminal, type: sh build.sh
# this version requires newer fonttools to use --output-dir command


printf "Build fonts…\n"

# cd source_roboto || exit


#if ! python "sources/Amstelvar-NewCharset/build-amstelvar.py"

if ! python "build-amstelvar_TEST-TRAVIS-BUILD.py"


    then
        printf "Unable to run pyhon script.  Build canceled." 1>&2
        exit 1
fi


# if ! fontmake -m "source/designspace/test.designspace" -o variable --no-production-names --output-dir './fonts/Test_vf'
#     then
#         printf "Unable to build var font.  Build canceled." 1>&2
#         exit 1
# fi





printf "\nBuild complete"