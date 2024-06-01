# file manipulation system----
def create ( file_name) :
    f = open(f'{file_name}.txt','w')
    f.close()

def append ( file_name, input_data) :
 f = open(f'{file_name}.txt','a')
 f.write(f' {input_data}')
 f.close()

def read ( file_name) :
 f = open(f'{file_name}.txt','r')
 text = f.read()
 print(text)
 f.close()


print("Welcome in File manipulation program\n\n")

print("01 : create a new file\n02 : Write in file\n03 : read the file\n\n")

file_name = ""

key = int(input("Press key : "))

match key : 
  
  case 1: 
    file_name = input("[+] Enter your file name : ")
    print("[+] Creating a file .....")
    create(file_name)
    

  case  2 : 
    input_data = input("Enter your data : ")
    append(file_name,input_data)
    print("[+] data Saved Successfully")

  case 3:
    print("[+] open File ....")
    read(file_name)  