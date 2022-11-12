import os, sys, csv, traceback
import requests
from random import random
import asyncio

def print_html(listfile):
    """
        -i [listfile] :
        
            Reads csv file specified by listfile,
            expecting the format 
                name;url
            makes an asynchronous request to the url, 
            if the request takes longer than 3 seconds,
            "Skipping" is displayed, 
            otherwise the raw html returned is displayed in the format:

            [HTML] "[name]"
    """

    async def async_get(url):
        
        # block for a moment to check timeout behaviour
        
        # value = 2.3 + random()
        # print(f'blocking for {value}')
        # await asyncio.sleep(value)

        response = requests.get(url)

        if response.status_code == 200:
            return response.text[:30]
        else :
            return "(unsuccessful status_code)" 

    async def scan_url_list(listfile):
        with open(listfile, newline='') as csvfile:
            url_list = csv.reader(csvfile, delimiter=';')
            for row in url_list:
                if row:
                    (name,url) = row
                    try:
                        html = await asyncio.wait_for(async_get(url), timeout=3)
                    except asyncio.TimeoutError:
                        print(f'Skipping {url}')
                    else :
                        print(f'HTML \"{name}\"\n{html}\n')

    asyncio.run(scan_url_list(listfile))

if __name__=="__main__":
    
    cmds = {
            '-i' : print_html,
            }

    def print_help():
        """ 
        -h :
        
            print this help message\n   

        """
        helpstr = """\"download.py\": a script to print html of url list in csv. Run with:\
                \n\npython download.py <option> [args...]\n\n\
options:\n"""
        helpstr += '\n'.join([  v.__doc__ +'\n' for (k,v) in cmds.items()])
        print(helpstr)
    
    cmds['-h'] = print_help

    try :
        assert len(sys.argv)>1, "Error - No command specified.\n"
        assert sys.argv[1] in cmds.keys(), "Error - Not a valid option.\n"
        if sys.argv[1]=='-i':
            assert len(sys.argv)==3, "Error - Invalid option arguments {}\n".format(str(sys.argv[1:]))
        if sys.argv[1]=='-h':
            assert len(sys.argv)==2, "Error - Invalid option arguments {}\n".format(str(sys.argv[1:]))
        
        cmds[sys.argv[1]](*sys.argv[2:])
    except Exception as e:
        print(e)
        traceback.print_exc()
        print_help()

