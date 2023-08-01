#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd


# In[9]:


def read_files(path, name_file, year_date, type_file):
    _file = f'{path}{name_file}{year_date}.{type_file}'
    colspecs = [
              (2,10),
              (10,12),
              (12,24),
              (27,39),
              (56,69),
              (69,82),
              (82,95),
              (108,121),
              (152,170),
              (170,188),
                      ]
    names = ['data_pregao','Codbid','sigla_acao','nome_acao','preco_abertura','preco_max','preco_min','preco_fechamento','qtd_negocios','volume_negocios']
    df = pd.read_fwf(_file, colspecs = colspecs, names = names, skiprows = 1)
    
    return df
        
    
    


# In[10]:


def filtrar_acao(df):
    df = df [df['Codbid'] == 2]
    df = df.drop(['Codbid'],1)
    return df


# In[11]:


def ajuste_date(df):
    df['data_pregao'] = pd.to_datetime(df['data_pregao'], format = '%Y%m%d')
    return df


# In[12]:


def ajuste_dados(df):
    df['preco_fechamento'] = (df['preco_fechamento']/100).astype(float)
    return df


# In[13]:


def concat_files(path, name_file, year_date, type_file, final_file):
    for i, y in enumerate(year_date):
        df = read_files(path, name_file, y, type_file)
        df = filtrar_acao(df)
        df = ajuste_date(df)
        df = ajuste_dados(df)

        if i == 0:
            df_final = df
        else:
            df_final = pd.concat([df_final, df])

    df_final.to_csv(f'{path}//{final_file}', index=False)


# In[14]:


year_date = ['2022']
path = f'C://Users//isapr//Meu Drive//Colab Notebooks//fianceira//'
name_file = 'COTAHIST_A'
type_file = 'txt'
final_file = 'all_bovespa2022.csv'
concat_files (path, name_file, year_date, type_file, final_file)


# In[ ]:




