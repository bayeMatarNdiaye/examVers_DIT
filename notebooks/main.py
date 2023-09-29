import pandas as pd

def load(path) :

    data = pd.read_csv(path)
    print(data.info())
    print('Street',data['Street'].unique())
    print('LotShape',data['LotShape'].unique())
    print('Alley',data['Alley'].unique())
    print('Foundation',data['Foundation'].unique())
    print('CentralAir',data['CentralAir'].unique())
    print('PoolArea',data['PoolArea'].unique())
    return data

def red(data) :
    x = data[['MSSubClass', 'LotArea', 'Street', 'LotShape', 'LandContour', 'HouseStyle', 'OverallQual', 'OverallCond', 'YearBuilt', 'Foundation', 'CentralAir', 'GrLivArea', 'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'GarageCars', 'PoolArea', 'YrSold']]
    return x

def clean(x) :
    street = {'Pave': 0,'Grvl': 1}
    x.Street = [street[item] for item in x.Street]

    lot = {'Reg' : 0, 'IR1' : 1, 'IR2' : 2, 'IR3' : 3}
    x.LotShape = [lot[item] for item in x.LotShape]

    land = {'Lvl' : 0, 'Bnk' : 1, 'Low' : 2, 'HLS' : 3}
    x.LandContour = [land[item] for item in x.LandContour]

    house = {'2Story' : 0, '1Story' : 1, '1.5Fin' : 2, '1.5Unf' : 3, 'SFoyer' : 4, 'SLvl' : 5, '2.5Unf' : 6, '2.5Fin' : 7}
    x.HouseStyle = [house[item] for item in x.HouseStyle]

    fond = {'PConc' : 0, 'CBlock' : 1, 'BrkTil' : 2, 'Wood' : 3, 'Slab' : 4, 'Stone' : 5}
    x.Foundation = [fond[item] for item in x.Foundation]

    air = {'N': 0,'Y': 1}
    x.CentralAir = [air[item] for item in x.CentralAir]

    return x

def summary_stats(data):
    
    summary = data.describe()
    
    print("Statistiques sommaires des données :")
    return summary

if __name__ == '__main__' :

    data = load('train.csv')
    data_reduce = red(data)
    cleaned = clean(data)
    stats = summary_stats(cleaned)
    print(stats)
