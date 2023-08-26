import os
import sys
sys.dont_write_bytecode = True
import re
import webbrowser
from SincEPUB import SincEPUB

class SincReader:

    sinc_book = SincEPUB()
    sinc_opf_code = sinc_book.sinc_read_opf()
    sinc_opf_path =  sinc_book.sinc_find_opf()[1]
    sinc_opf_directory_path = os.path.dirname(sinc_opf_path)

    def __init__(self):
        if(__name__=='__main__'):
            def_name = 'SincReader'
            print( '===  ' + def_name + ' is functioning.  ===\n')
    
    def sinc_opf_spine(self):
        sinc_opf_code = SincReader.sinc_opf_code
        sinc_spine_itself_search = re.search( '(.*?)<spine(.*?)>(.|\s)*?</spine>' , sinc_opf_code )
        sinc_spine_itself = sinc_spine_itself_search.group()
        sinc_spine_itemref_list = re.findall('<itemref.*?/>' , sinc_spine_itself , re.DOTALL)
        sinc_spine_idref_list = []
        sinc_spine_idref_name_list = []
        for sinc_spine_itemref in sinc_spine_itemref_list:
            sinc_spine_idref_search = re.search('idref="(.*?)"' , sinc_spine_itemref)
            sinc_spine_idref = sinc_spine_idref_search.group()
            sinc_spine_idref_name = sinc_spine_idref.replace('idref=','')
            sinc_spine_idref_list.append(sinc_spine_idref)
            sinc_spine_idref_name_list.append(sinc_spine_idref_name)
        return sinc_spine_itself , sinc_spine_idref_list , sinc_spine_idref_name_list

    def sinc_opf_manifest(self):
        sinc_opf_code = SincReader.sinc_opf_code
        sinc_manifest_itself_search = re.search('(.*?)<manifest(.*?)>(.|\s)*?</manifest>', sinc_opf_code )
        sinc_manifest_itself = sinc_manifest_itself_search.group()
        sinc_manifest_item_list = re.findall('<item.*?/>' , sinc_manifest_itself , re.DOTALL)
        sinc_manifest_id_list = []
        sinc_manifest_id_name_list = []
        for sinc_manifest_item in sinc_manifest_item_list:
            sinc_manifest_id_search = re.search('id="(.*?)"' , sinc_manifest_item)
            sinc_manifest_id = sinc_manifest_id_search.group()
            sinc_manifest_id_name = sinc_manifest_id.replace('id=','')
            sinc_manifest_id_name_list.append(sinc_manifest_id_name)
            sinc_manifest_id_list.append(sinc_manifest_id)
        return sinc_manifest_itself , sinc_manifest_item_list , sinc_manifest_id_list , sinc_manifest_id_name_list

    def print_sinc_opf_spine(self):
        sinc_spine_itself = self.sinc_opf_spine()[0]
        sinc_spine_idref_list = self.sinc_opf_spine()[1]
        print('==  Your spine  ==')
        print(sinc_spine_itself)
        print('==  Your spine  ==\n')
        print('==  Your idref in itemref  ==')
        for sinc_spine_idref in sinc_spine_idref_list:
            print(sinc_spine_idref)
        print('==  Your idref in itemref  ==\n')

    def print_sinc_opf_manifest(self):
        sinc_manifest_itself = self.sinc_opf_manifest()[0]
        sinc_manifest_item_list = self.sinc_opf_manifest()[1]
        sinc_manifest_id_list = self.sinc_opf_manifest()[2]
        print('==  Your manifest  ==')
        print(sinc_manifest_itself)
        print('==  Your manifest  ==\n')
        print('==  Your item list  ==')
        print('\n'.join(sinc_manifest_item_list))
        print('==  Your item list  ==\n')
        print('==  Your id in item  ==')
        for sinc_manifest_id in sinc_manifest_id_list:
            print(sinc_manifest_id)
        print('==  Your id in item  ==\n')
        
    def sinc_read_href(self):
        sinc_spine_idref_name_list = self.sinc_opf_spine()[2]
        sinc_manifest_id_name_list = self.sinc_opf_manifest()[3]
        sinc_manifest_item_list = self.sinc_opf_manifest()[1]
        sinc_same_id_idref_list = set(sinc_spine_idref_name_list) & set(sinc_manifest_id_name_list)
        sinc_html_list = []
        print('==  Your html  ==')
        print('Sinc Reader will read these htmls.')
        print(sinc_same_id_idref_list)
        print('==  Your html  ==\n')
        print('==  Your html path  ==')    
        for sinc_manifest_item in sinc_manifest_item_list:
            for sinc_same_id_idref in sinc_same_id_idref_list:
                is_sinc_html = bool(re.search( sinc_same_id_idref , sinc_manifest_item ))
                if(is_sinc_html):
                    sinc_html_search = re.search('href="(.*?)"',sinc_manifest_item)
                    sinc_html_list.append(sinc_html_search.group())
        print('==  Your html path  ==\n')
        return sinc_html_list
        
    def print_sinc_read_href(self):
        print('==  Your href  ==')
        print('==  Your href  ==\n')

    def sinc_html_path(self):
        sinc_opf_directory_path = SincReader.sinc_opf_directory_path
        sinc_html_list = self.sinc_read_href()
        sinc_read_html_path_list = []
        for sinc_html_path in sinc_html_list:
            b = sinc_html_path.replace('"','').replace('href=','')
            sinc_html_path =  os.path.join(sinc_opf_directory_path,b)
            print(sinc_html_path)
            sinc_read_html_path_list.append(sinc_html_path)
        return sinc_read_html_path_list

    def sinc_html_make(self):
        sinc_read_html_path_list = self.sinc_html_path()
        sinc_opf_path = SincReader.sinc_opf_path
        sinc_opf_directory_path = SincReader.sinc_opf_directory_path
        sinc_html = os.path.join(sinc_opf_directory_path,'book','sinc_html.html')
        print(sinc_html)
        with open(sinc_html,'w',encoding='utf-8')as sinc_original_html:
            for sinc_read_html_path in sinc_read_html_path_list:
                with open(sinc_read_html_path , 'r' , encoding='utf-8')as sinc_one_html:
                    sinc_original_html.write(sinc_one_html.read())
        return sinc_html

    def sinc_html_read(self):
        sinc_html = self.sinc_html_make()
        print(sinc_html)
        sinc_html_path = os.path.join(os.getcwd(),sinc_html)
        print(type(sinc_html_path))
        webbrowser.get()
        webbrowser.open(sinc_html_path,new=1,autoraise=True)
        

if(__name__ == '__main__'):
    sinc_reader = SincReader()
    sinc_reader.print_sinc_opf_spine()
    sinc_reader.print_sinc_opf_manifest()
    sinc_reader.sinc_read_href()
    sinc_reader.sinc_html_path()
    sinc_reader.sinc_html_make()
    sinc_reader.sinc_html_read()