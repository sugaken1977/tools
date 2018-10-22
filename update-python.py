#!/path of python3
#######
# python-updater
#
# It may not work on Windows.
# You need python3 and pip to run this script.
#
# just run this script with no arguments.
#
# % python3 update-python.py
#
#######
import subprocess

# if you want to update npm, delete [#] below 2lines.

#print("Updating: npm")
#subprocess.run(["npm", "update"])

# if you want to update brew, delete [#] below 6 lines.

#print("Updating: brew")
#subprocess.run(["brew", "update"])
#print("Updating: brew")
#subprocess.run(["brew", "upgrade", "--clean"])
#print("Clreanup: brew")
#subprocess.run(["brew", "cleanup"])

# python update

print("Update start")

print("Updating: pip")

UPDATE_LIST = (subprocess.run(["pip", "list", "-o"],stdout=subprocess.PIPE))
Packages = str(UPDATE_LIST.stdout).split('\\n')
   
# drop 2 lines on update list ( titles and bars )
for i in range(2,len(Packages)-1):
    print("Updating: " + str(Packages[i]).split()[0])
    subprocess.run(["pip", "install", "-U", str(Packages[i]).split(" ")[0]])

print("Update finished.")

