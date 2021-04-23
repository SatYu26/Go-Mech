import pandas as pd

data = {'Names':  ['Shubham', 'Raj', 'Agrawal'],
        'Branch': ['IT', 'EEE', 'ECE'],
        'Marks': ['50', '80', '100'],
        }

mongoImport = pd.DataFrame(
    data, columns=['Names', 'Branch', 'Marks'])
