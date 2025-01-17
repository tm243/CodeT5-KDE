#!/bin/bash

wget https://www.opendocstring.com/downloads/weights/codet5instr/kde-cpp-qml-instructions-2023-11-07-13.tar.gz
rm -Rf api/trained/*
tar -xzvf kde-cpp-qml-instructions-2023-11-07-13.tar.gz -C api/

