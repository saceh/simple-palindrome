#!/usr/bin/env bash

pythonExe=/usr/bin/python
pythonScript=palindrome.py

inputStr=$1

usage (){
   echo "Usage : $0 <string>"
}

if [[ -z $inputStr ]] || [[ $# -gt 1 ]]
then
   usage
   exit 1
else
   $pythonExe $pythonScript $inputStr
fi

exit 0


