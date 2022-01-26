import gdown

google_path = 'https://drive.google.com/uc?id='
file_id = '1HSO38hLSYEJJ_U9_w0o2kpI3ouq03k3u'
output_name = 'wellness_data.xlsx'
gdown.download(google_path+file_id,output_name,quiet=False)