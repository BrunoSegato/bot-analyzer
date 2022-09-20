from os import listdir
from os.path import isfile, join
import pandas as pd


def run():
    file_path = 'jobs/files/'
    export_path = 'jobs/files/export/'
    column_to_keep = ['Data', 'Competição', 'Jogo', 'Resultado']
    files_to_process = [f for f in listdir(file_path) if isfile(join(file_path, f))]
    result_dict = {
        'Competição': None,
        'Total': None,
        'Green': None,
        'Red': None,
        '%_Green': None,
        '%_Red': None
    }

    for file in files_to_process:
        df = pd.read_csv(filepath_or_buffer=f'{file_path}{file}',
                         delimiter=',',
                         encoding='utf-8',
                         names=None,
                         converters={},
                         chunksize=None,
                         header=0)

        column_to_keep_in_df = [c for c in column_to_keep if c in df.columns]
        df = df.drop(labels=df.columns.difference(column_to_keep), axis=1)

        df_green = df[df['Resultado'] == 'green']
        df_red = df[df['Resultado'] == 'red']
        total_greens = {x: y for x, y in df_green['Competição'].value_counts().items()}
        total_reds = {x: y for x, y in df_red['Competição'].value_counts().items()}
        total = {x: y for x, y in df['Competição'].value_counts().items()}

        result_dict['Competição'] = [x for x, y in df['Competição'].value_counts().items()]
        result_dict['Total'] = [total.get(x, 0) for x in df['Competição'].drop_duplicates()]
        result_dict['Green'] = [total_greens.get(x, 0) for x in df['Competição'].drop_duplicates()]
        result_dict['Red'] = [total_reds.get(x, 0) for x in df['Competição'].drop_duplicates()]
        result_dict['%_Green'] = [total_greens.get(x, 0) / total.get(x, 0) for x in df['Competição'].drop_duplicates()]
        result_dict['%_Red'] = [total_reds.get(x, 0) / total.get(x, 0) for x in df['Competição'].drop_duplicates()]

        df = pd.DataFrame(result_dict)
        df.sort_values(by=['Total'], ascending=False).to_csv(f'{export_path}{file}',
                                                             decimal=',',
                                                             sep=';',
                                                             float_format='%.3f')

    return True
