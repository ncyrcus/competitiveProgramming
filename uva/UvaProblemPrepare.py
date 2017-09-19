import os
import shutil
def crearCPP(idUva,nombre):
	dirs=os.listdir(".")
	path_dir=idUva+" - "+nombre
	if path_dir not in dirs:
		os.mkdir(path_dir)
		file=nombre+".cpp"
		arch= open(path_dir+"/"+file,"w")
		arch.write("#include <iostream>\n#include <cstdio>\n#include <vector>\n#include <math>\nusing namespace std;\n\nint main(){\n\n\n\treturn 0;\n}")
		arch.close()
		return path_dir
	else:
		print("La carpeta para este archivo ya ha sido creado")
		return False
def prepareSample(path_dir):
	if  path_dir != False:
		print "ingresa los ejemplos de entrada linea a linea y finaliza ingresando el texto #4523fin2356#"
		arch= open(path_dir+"/sample input.txt","w")
		linea=str(raw_input(""))
		while linea!= "#4523fin2356#":
			arch.write(linea+"\n")
			linea=str(raw_input(""))
		arch.close()
		print "ingresa los ejemplos de salida linea a linea y finaliza ingresando el texto #4523fin2356#"
		arch= open(path_dir+"/sample output.txt","w")
		linea=str(raw_input(""))
		while linea!= "#4523fin2356#":
			arch.write(linea+"\n")
			linea=str(raw_input(""))
		arch.close()
prepareSample(crearCPP("495","Fibonacci Freeze"))