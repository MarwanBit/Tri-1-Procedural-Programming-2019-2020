#!/bin/bash
cd 
mkdir zoo 
mkdir zoo/reptiles zoo/cats zoo/veldt 
cd zoo/reptiles
touch iguana gator
cd .. 
cd cats
touch lion tiger caracel
cd ..
cd veldt
touch giraffe rhino gazelle
cd 
ls -R zoo 
