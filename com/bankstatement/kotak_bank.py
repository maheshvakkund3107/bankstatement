# Import the required Module
import tabula
import pandas as pd

if __name__ == '__main__':
    tabula.convert_into("../resources/mahesh.pdf", "../resources/mahesh.csv", output_format="csv", pages='all')
    data = pd.read_csv('../resources/mahesh.csv')
    print(data)
