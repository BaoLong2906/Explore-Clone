import os
import sys
#pip install subprocess.run
import subprocess

#print int(sys.argv[1])+int(sys.argv[2])

#pip install argparse
import argparse
# pip install patool
import patoolib

#patoolib.extract_archive("C:\\Users\\Acer\\Desktop\\HuynhCaoBaoLongLab1.rar", outdir="C:\\Users\\Acer\\Desktop")
f = open(sys.argv[1],'r')
nameFile = os.path.basename(f.name)

print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[2] + nameFile +".rar")
#patoolib.create_archive(sys.argv[2] + nameFile +".rar" , sys.argv[1])
patoolib.create_archive(nameFile +".rar",(sys.argv[1],))
