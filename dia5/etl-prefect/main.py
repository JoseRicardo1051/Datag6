from tasks.extract import extract
from tasks.transform import transform
from tasks.load import load
from prefect import flow
from tabulate import tabulate


@flow
def main():
    data = extract()
    data_transform = transform(data)
    cabeceras = ['nombre','sexo','pais','fecha_nac']
    print(tabulate(data_transform,headers=cabeceras,tablefmt='grid'))
    load(data_transform)
    
if __name__ == "__main__":
    main()