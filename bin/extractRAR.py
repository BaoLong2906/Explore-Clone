import sys
#pip install subprocess.run
import subprocess

#print int(sys.argv[1])+int(sys.argv[2])

#pip install argparse
import argparse
# pip install patool
import patoolib

#patoolib.extract_archive("C:\\Users\\Acer\\Desktop\\HuynhCaoBaoLongLab1.rar", outdir="C:\\Users\\Acer\\Desktop")
print(sys.argv[1])
print(sys.argv[2])
patoolib.extract_archive(sys.argv[1], outdir=sys.argv[2])
