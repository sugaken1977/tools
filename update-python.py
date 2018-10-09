#######
# python-updater
#
# It may not work on Windows.
#######
import subprocess

print("Update start")

print("Updating: pip")

UPDATE_LIST = (subprocess.run(["pip", "list", "-o"],stdout=subprocess.PIPE))
Packages = str(UPDATE_LIST.stdout).split('\\n')
   
# drop 2 lines on update list ( titles and bars )
for i in range(2,len(Packages)-1):
    print("Updating: " + str(Packages[i]).split()[0])
    subprocess.run(["pip", "install", "-U", str(Packages[i]).split(" ")[0]])

print("Update finished.")

