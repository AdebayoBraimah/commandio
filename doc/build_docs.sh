#!/usr/bin/env bash

cwd=$(pwd)
wd=$(dirname $(realpath ${0}))

sphinx-apidoc -o source ../../commandio

# Remove test associated files
rm source/*test*

make clean; make html

cd ${cwd}
