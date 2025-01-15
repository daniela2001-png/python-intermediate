"""
Sin utilizar la libreria de pandas, crea una clase que permita validar este coportamiento: 

df = Dataframe([{"a": 1}, {"a": 2}])
print(df[df.a > 1] == Dataframe([{"a": 2}])) # Esto debe darte True
"""
class Column:
    def __init__(self, data):
        self.data = data
    
    # is gonna return a list of bools
    def __gt__(self, other):
        return [value > other for value in self.data]


class DataFrame:
    def __init__(self, data):
        self.data = data
        
    def __getitem__(self, condition):
        # condition will be an array of bools
        values_from_attr = []
        for index, row in enumerate(condition):
            # if the actual value is greater than the other value
            if row:
                values_from_attr.append(self.data[index])
        return values_from_attr

    
    def __getattr__(self, name):
        return Column([row[name] for row in self.data if name in row])
        
    
    # is gonna return a bool
    def __eq__(self, other):
        return self.data == other


data = [{"a": 4}, {"a": 2}]

my_df = DataFrame(data)
print(my_df[my_df.a > 1] == DataFrame([{"a": 4}, {"a": 2}]))