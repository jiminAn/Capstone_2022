import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

#Read excel file into a dataframe
data_xlsx = pd.read_excel(input_file, 'Sheet1', index_col=None)

#Replace all columns having spaces with underscores
data_xlsx.columns = [c.replace(' ', '_') for c in data_xlsx.columns]

#Replace all fields having line breaks with space
df = data_xlsx.replace('\n', ' ',regex=True)

#Write dataframe into tsv
df.to_csv(output_file, sep='\t', encoding='utf-8',  index=False, line_terminator='\r\n')
