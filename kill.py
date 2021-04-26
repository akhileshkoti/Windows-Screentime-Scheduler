import psutil
name="pythonw.exe"
for proc in psutil.process_iter():
	if(proc.name()==name):
		proc.kill()
