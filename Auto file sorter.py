import os, shutil

# Define the path
path = r"/Users/dikshant/Downloads/spring 2024/art & craft of writting/"

# Print the path to verify
print("Path:", path)

if os.path.exists(path):
    # List all items in the directory
    file_name = os.listdir(path)
    
floder_name = ['docx files','pdf files']

for loop in range (0,2):
# Check if the directory exists and making new floder according to file types in the floder
    if not  os.path.exists(path + floder_name[loop]):
        #file_name = os.listdir(path)
        print (path + floder_name[loop])
        os.makedirs (path + floder_name[loop])
    else:
        print(f"The directory does not exist: {path}")
        

for file in file_name:
    if ".docx" in file and not os.path.exists(path + "docx files/" + file):
        shutil.move(path + file, path + "docx file/" + file)
for file in file_name:
    if ".pdf" in file and not os.path.exists(path + "pdf files/" + file):
        shutil.move(path + file, path + "pdf file/" + file)
