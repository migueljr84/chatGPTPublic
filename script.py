import requests
import json
from colorama import Fore, Back, Style
import datetime
import time
import os


class bcolors:
	OKGREEN = '\033[32m'
	FAIL = '\033[31m'
	ENDC = '\033[0m'
	HEADER = '\033[35m'
	OKBLUE = '\033[34m'
	WARNING = '\033[33m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

vWatermarkReturn = ""
vExportReturn = ""
vExportHistory = "false"
vImportHistory = "false"

print ("")
print ("--------------------------------------------------------------------------------------------------")
print ("Iniciando o job...")
print ("")

data = datetime.datetime.now()
dia = ("0" + str(data.day)) if (len(str(data.day)) == 1) else str(data.day)
mes = ("0" + str(data.month)) if (len(str(data.month)) == 1) else str(data.month)
ano = str(data.year)
hora = ("0" + str(data.hour)) if (len(str(data.hour)) == 1) else str(data.hour)
minuto = ("0" + str(data.minute)) if (len(str(data.minute)) == 1) else str(data.minute)
segundo = ("0" + str(data.second)) if (len(str(data.second)) == 1) else str(data.second)

vWatermarkFile = "HML_MARK_"+dia+mes+ano+"_"+hora+minuto+segundo+".txt"
vExportFile = "HML_INC_"+dia+mes+ano+"_"+hora+minuto+segundo+".zip"


print ("Watermark gerada com " + vWatermarkFile)
print ("vExportFile gerada com " + vExportFile)
print ("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -")
print ("")


print ("")
print ("Execução do job finalizada")
print ("--------------------------------------------------------------------------------------------------")
