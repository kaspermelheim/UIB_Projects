import os

path = "C:/Users/Kasper/OneDrive - University of Bergen/Documents/Sem4/INF142/gs3_task10_files/"

def get(num):
    with open(path + f"file{num}.txt", "r") as file:
        return file.read()

def put(content, num):
    with open(path + f"file{num}.txt", "w") as file:
        file.write(content)
        print(f"Wrote to file {num}.")

def delete(num):
    if os.path.exists(path + f"file{num}.txt"):
        os.remove(path + f"file{num}.txt")
        print(f"File {num} has been deleted.")
    else:
        print("The file does not exist")



if __name__ == "__main__":
    print("Enter GET, PUT or DEL depending on what you want to do.")
    done = False
    while(not done):
        cmd = input("> ")
        
        if(cmd == "GET"):
            num = int(input("> "))
            print(get(num))
        elif(cmd == "PUT"):
            num = int(input("> "))
            content = input("> ")
            put(content, num)
        elif(cmd == "DEL"):
            num = int(input("> "))
            delete(num)
        elif(cmd == "END"):
            done = True
        else:
            print("ERROR: Bad command.")
