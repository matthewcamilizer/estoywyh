import sys
sys.dont_write_bytecode = True

import json
with open (input("input file:"), "r", encoding = 'utf-8') as f:
    js_code = f.read()
    start_index = js_code.find('[')
    js_code = js_code[start_index:]
    js_code = js_code.rstrip(';')
    final_file = json.loads(js_code)
while True:
    OP = input("'del' or 'add': ")
    try:
        if (OP == 'del'):
            To_Delete = input("enter Key (spilt by comma): ").split(",")
            for i in final_file:
                for j in To_Delete:
                    del i[j]              
        if (OP == 'add'):
            To_Add = input("enter Key (spilt by comma): ").split(",")
            for i in final_file:
                for j in To_Add:
                    i[j] = ""
        break
    except:
        break
while True:
    Format = input("'js' or 'json: ")
    out_file = input(r"enter your output file: ")
    try:
        if (Format == 'js'):  
            final_file = json.dumps(final_file)
            with open (out_file, "w", encoding = 'utf-8') as f:
                f.write("let allMusic = " + final_file + ";")
        if (Format == 'json'):
            with open (out_file, "w", encoding = 'utf-8') as f:
                json.dump(final_file, f)
        break
    except:
        break