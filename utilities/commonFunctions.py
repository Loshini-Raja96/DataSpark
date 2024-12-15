def check_dtypes(columns):
    col=columns.dtypes
    print(col)
    return col

def check_nullSum(data):
    na=data.isnull().sum()
    print(na)
    return na

def update_null(null_type,dataset):
    fill=dataset.fillna(null_type,inplace=True)
    print(fill)
    return fill    