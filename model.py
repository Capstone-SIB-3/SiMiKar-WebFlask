import numpy as np
import pandas as pd
from sklearn.utils import resample 
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder

jobs = pd.read_csv('./techloker.csv')

jobs.drop('link',axis=1,inplace= True)
jobs.drop('nama_perusahaan',axis=1,inplace= True)
jobs.drop('lokasi_perusahaan',axis=1,inplace= True)

print('Banyak data: ', len(jobs.jenis_pekerjaan.unique()))
print('Jenis Pekerjaan : ', jobs.jenis_pekerjaan.unique())

# Membersihkan missing value dengan fungsi dropna()
jobs_clean = jobs.dropna()
jobs_clean

# Mengurutkan jobs berdasarkan kemampuan kemudian memasukkannya ke dalam variabel fix_jobs
fix_jobs = jobs_clean.sort_values('kemampuan', ascending=True)
fix_jobs

# Membuat dictionary untuk data ‘jenis_pekerjaan’, ‘kemampuan’
jobs_new = pd.DataFrame({
    'Jenis_Pekerjaan': jenis_jobs,
    'Kemampuan': kemampuan_jobs
})
jobs_new