import os

# Function to rename multiple files
def main():
    path="./report/"
    for filename in os.listdir(path):
        if filename.startswith('hindu_'):
            my_dest = f"{filename[6:]}"
            my_source = path + filename
            my_dest = path + my_dest
            #print(my_dest)
            os.rename(my_source, my_dest)

def strip():
    text = 'Privacy Policy'
    print(text.strip())

# Driver Code
if __name__ == '__main__':
    main()
    #strip()