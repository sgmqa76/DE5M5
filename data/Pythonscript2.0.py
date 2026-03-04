import pandas as pd 

def sayHello():
    print("Hello")

def sayHello_v2(name="Default"):
    print("Hello", name)

def addnumbers(a,b):
    answer = a + b
    return answer

def fileLoader():
    books = pd.read_csv("03_Library Systembook.csv")
    customers = pd.read_csv("03_Library SystemCustomers.csv")

    books.columns = books.columns.str.strip()
    customers.columns = customers.columns.str.strip() 
    
    return books, customers

def duplicateCheck(df):
    return df.drop_duplicates()

def naCheck(df):
    return df.dropna()

def dataCleaner(books):
    books["Book checkout"]=books["Book checkout"].astype(str).str.replace('"', '', regex=False).str.strip()
    return books

def dataEnrich():
    # Creates a new col to work out the "Time on loan". ie the difference between the date checked out and date checked in.
    pass

#Stretch
def writesToSQL():
    pass

print("Ended")