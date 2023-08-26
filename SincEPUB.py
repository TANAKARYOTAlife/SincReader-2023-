import os
import zipfile

class SincEPUB:

    def __init__(self):
        if(__name__=='__main__'):
            def_name = 'SincEPUB'
            print('\n===  ' + def_name + ' is functioning.  ===\n')
        else:
            print('\n===  ' + __name__ + ' is functioning.  ===\n')
        self.print_sinc_your_epub()
        self.print_sinc_your_opf()
        
    def sinc_your_epub(self):
        for sinc_current_directory in os.listdir():
            if(sinc_current_directory.endswith('.epub')):
                your_book_epub = sinc_current_directory
                return your_book_epub
            
    def print_sinc_your_epub(self):
        print('==  Your_EPUB  ==')
        print('Your EPUB is ' + self.sinc_your_epub())
        print('==  Your_EPUB  ==\n')
        
    def sinc_zip_extract(self):
        your_book_epub = self.sinc_your_epub()
        your_epub_zip = ['EPUB','META-INF','mimetype']
        sinc_current_directory = os.listdir()
        first_zip_extract = not set(your_epub_zip).isdisjoint(sinc_current_directory)   
        print('=== {} is already extracted:{}  ==='.format(your_book_epub,str(first_zip_extract)))
        if(not first_zip_extract):
            with zipfile.ZipFile(self.sinc_your_epub())as sincbook:
                sincbook.extractall()
                print('===  {} is extracted now.  ==='.format(your_book_epub))
        else:
            print('sinc_zip_extract does not need to work.')
            print('===  {} is already extracted.  ===\n'.format(your_book_epub))

    def sinc_find_opf(self):
        sinc_book_file = os.walk('./')
        for dirpath,dirnames,filenames in sinc_book_file:
            for filename in filenames:
                sinc_book_file_base_extension = os.path.splitext(filename)
                sinc_book_file_base = sinc_book_file_base_extension[0]
                sinc_book_file_extension= sinc_book_file_base_extension[1]
                if(sinc_book_file_extension == '.opf'):
                    sinc_opf_file = sinc_book_file_base + sinc_book_file_extension
                    sinc_opf_path = os.path.join(dirpath,sinc_opf_file)
        return sinc_opf_file , sinc_opf_path

    def print_sinc_your_opf(self):
        print('==  Your Opf file  ==')
        print('Your opf file is ' + self.sinc_find_opf()[0])
        print('Your opf file path is ' + self.sinc_find_opf()[1])
        print('==  Your Opf file  ==\n')
        
    def sinc_read_opf(self):
        sinc_opf_path = self.sinc_find_opf()[1]
        with open( sinc_opf_path ,'r' ) as sinc_opf_file:
            sinc_opf_code = sinc_opf_file.read()
        return sinc_opf_code

if(__name__=='__main__'):
    sinc_book = SincEPUB()
