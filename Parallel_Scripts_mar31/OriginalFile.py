import subprocess
import time

x=subprocess.Popen(["python","file1.py"])
time.sleep(10)
y=subprocess.Popen(["python","file2.py"])
#x.kill()
time.sleep(1)
y.kill()
print("--------------------------Done------------------------")
exit()