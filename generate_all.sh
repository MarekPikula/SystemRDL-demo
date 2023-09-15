#!/bin/bash

RUN="poetry run"

poetry install

# HDL/IP
$RUN desyrdl -i example.rdl -o vhdl/ -f vhdl
$RUN peakrdl regblock example.rdl -o regblock/
$RUN peakrdl uvm example.rdl -o example-uvm.v
$RUN peakrdl ip-xact example.rdl -o example.xml

# Documentation
$RUN peakrdl html example.rdl -o html/
$RUN peakrdl markdown example.rdl -o example.md

# Software
$RUN peakrdl_cheader example.rdl
$RUN peakrdl halcpp example.rdl -o cpp/
$RUN peakrdl python-simple example.rdl -o example.simple.py
$RUN peakrdl python example.rdl -o python/
