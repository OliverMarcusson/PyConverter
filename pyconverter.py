from PIL import Image
import os

# Methods usable in other programs
class Converter:
    def list_files(dir, extension):
        list = []
        filenames = []
        for filename in os.listdir(dir): # Lists everything in the targeted directory.
            filenames.append(filename)
            file = os.path.join(dir, filename)
            # checking if it is a file
            if os.path.isfile(file) and file.endswith(extension):
                list.append(file)
        
        return list, filenames
                
    def convert(dest_dir, png, new_name):
        png = Image.open(png, 'r')
        png.save(f"{dest_dir}{new_name}.ico",format='ICO')
       
# Main Program 
def main():
    # assign directories
    directory = 'png'
    dest_directory = './ico/'
    
    pngs = Converter.list_files(directory, '.png')[0]
    filenames = Converter.list_files(directory, '.png')[1]
    print(pngs)
    for i in range(len(pngs)):    
        Converter.convert(dest_directory, pngs[i], filenames[i])
        print(f"{filenames[i]}.ico Generated!")

if __name__ == '__main__':
    main()



         
