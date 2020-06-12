import pandas


class PandasExcelReader():
    def __init__(self, filename):
        self.filename = filename

    def Read(self):
        _target = pandas.read_excel(self.filename)
        t = []
        for i, j in _target.iterrows():
            serialNumber = i + 1
            name = j['NAME']
            _id = j['ID']
            _values = (serialNumber, name, _id)
            query = "INSERT INTO test (serial, name, id) values('%s', '%s', '%s')" % (
                _values)
            # print(query)
            t.append(query)
        
        return t


result = PandasExcelReader('h.xlsx')
d = result.Read()
print(d)


for i in d:
    print(i)
