#!/bin/bash
nuitka3 --recurse-all epitarendu.py
rm -rf epitarendu.build/
rm -rf __pycache__/
mv epitarendu.exe epitarendu
