import string,sys
sys.dont_write_bytecode=True

def clean(a:string)
    translator = str.maketrans('', '', string.punctuation + string.whitespace)
    cleaned_a = a.translate(translator)

    return cleaned_a
