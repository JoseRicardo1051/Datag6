from prefect import task

@task
def extract():
    extract_data = ['a','b','c']
    return extract_data