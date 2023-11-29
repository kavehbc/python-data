import multiprocessing
import concurrent.futures
import pandas as pd
import numpy as np
import calendar
import math


def multicore_process(d):

    for index, row in d.iterrows():
        period = str(row["Period"])
        pk = row["pk"]
        
        year, month = period.split(".")
        day = calendar.monthrange(int(year), int(month))[1]

        heavy_math = math.log((int(year) ** int(month)) * day)

        d.loc[d["pk"] == pk, 'heavy_math'] = heavy_math

    # return the chunk!
    return d

    
def parallelize_dataframe(df, func, n_cores=4):
   
    # calculate the chunk size as an integer
    df_chunks = np.array_split(df, n_cores)
    
    pool = multiprocessing.Pool(processes=n_cores)
    df = pd.concat(pool.map(multicore_process, df_chunks))
    
    pool.close()
    pool.join()
    return df


def parallelize_dataframe_future(df, func, n_cores=4):

    # calculate the chunk size as an integer
    df_chunks = np.array_split(df, n_cores)
    
    pool = concurrent.futures.ProcessPoolExecutor(max_workers = n_cores)
    df = pd.concat(pool.map(multicore_process, df_chunks))
    
    return df
    