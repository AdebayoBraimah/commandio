#!/usr/bin/env bash

cwd=$(pwd)
wd=$(dirname $(realpath ${0}))

sphinx-apidoc -o source ../../commandio; make clean; make html

cd ${cwd}
