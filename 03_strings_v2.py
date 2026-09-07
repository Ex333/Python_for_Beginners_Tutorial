from pathlib import Path

filename = "december_production_raport.xlsx"
print(filename)

print(filename.find("production"))
print(filename.lower().find("Production".lower()))
print(filename.replace("production", "finance"))
print(filename)
filename = filename.replace("production", "finance")
print(filename)
print(filename.find("ce"))
print(filename.find("ce", 3))
print("**" * 10)

password = "Password"
password = password.replace("a", "4").replace("s", "$").replace("o", "0")
print(password)

drive ="C:\\"
folder = "reports\\"
filename = "november_productaion_raport"
extension = ".xlsx"
full_path = drive + folder + filename + extension 
print(full_path)

drive1 = Path("C:/")
folder1 = "reports"
filename1 = "november_production_repor"
extension1  = ".xlsx"

full_path1  = drive1 / folder1 / (filename1 + extension1)
print(full_path1)