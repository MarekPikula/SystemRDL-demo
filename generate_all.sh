#!/bin/bash

RUN="poetry run"

poetry install
$RUN peakrdl html example.rdl -o html/
$RUN peakrdl regblock example.rdl -o regblock/
$RUN peakrdl_cheader example.rdl
$RUN desyrdl -i example.rdl -o vhdl/ -f vhdl
$RUN peakrdl uvm example.rdl -o example-uvm.v
$RUN peakrdl markdown example.rdl -o example.md
$RUN peakrdl ip-xact example.rdl -o example.xml
$RUN peakrdl python-simple example.rdl -o example.simple.py
$RUN peakrdl python example.rdl -o python/
