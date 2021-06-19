##All code boxxes of section 2.3
class Table:
    total_tables = 0

    def __init__(self, wood_used, year):
        self.wood_used = wood_used
        self.year = year
        Table.total_tables = Table.total_tables + 1
        print('Table made of {} wood has been created.'.format(self.wood_used))

    def setGuarantee(self,guarantee):
        self.guarantee = 25

t1 = Table('Ebony',2020)
##############################
class Table:
    total_tables = 0

    def __init__(self, wood_used, year):
        self.wood_used = wood_used
        self.year = year
        Table.total_tables = Table.total_tables + 1
        print('Table made of {} wood has been created.'.format(self.wood_used))

    def setGuarantee(self,guarantee):
        self.guarantee = 25

t1 = Table('Ebony',2020)
print(t1.__dict__)
###########################
class Table:
    total_tables = 0

    def __init__(self, wood_used, year):
        self.wood_used = wood_used
        self.year = year
        Table.total_tables = Table.total_tables + 1
        print('Table made of {} wood has been created.'.format(self.wood_used))

    def setGuarantee(self,guarantee):
        self.guarantee = guarantee

t1 = Table('Ebony',2020)
print("Attributes before calling setGaurantee() method.",t1.__dict__)
t1.setGuarantee(25)
print("Attributes after calling setGaurantee() method.",t1.__dict__)
#########################

class Table:
    total_tables = 0

    def __init__(self, wood_used, year):
        self.wood_used = wood_used
        self.year = year
        Table.total_tables = Table.total_tables + 1
        print('Table No.{} : Table made of {} wood has been created.'.format(Table.total_tables,self.wood_used))

    def setGuarantee(self,guarantee):
        self.guarantee = guarantee

t1 = Table('Ebony',2020)
t2 = Table('Teak',2019)
t3 = Table('Mango wood',2018)
