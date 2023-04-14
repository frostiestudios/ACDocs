import subprocess
name=input("Enter New Name:")
subprocess.run(["mkdocs","new", name])
print("done")