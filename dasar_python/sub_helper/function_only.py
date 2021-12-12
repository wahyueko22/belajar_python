from sub_helper import custom_exception_only as ok



def print_string():
    """The category create URL to be used for creating the product category """
    print ("call function print_string")
    data = {"name":5}
    print(data.get("cumi", 4))
    data.update({"one":7})
    print(data.get("one", 4))
    print(data.get("name", 4))
    kk = []
    kk.append((0,1,2,3,4,{'name': "john"}))
    print(type(kk))
    print(kk[0])

def test_variable():
    x = 5
    print(type(x))
    x = "five"
    print(type(x))

def test_conditional():
    localVar, localInt, age = "ok", 7, 20
    if localVar == "ok":
        print ("testConditional : ok %d " % localInt)
    me = "kid" if age < 10 else "adult"
    print (" age : %d " % age )

def looping_data():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        if x == "banana":
            continue
        print(x)
    for index in range(len(fruits)):
        print (fruits[index])
    for index, _ in enumerate(fruits, start=0):   # Python indexes start at zero
        print (fruits[index])

def list_data_type():
    print ("call list_data_type ")
    list_first = []
    print (len(list_first))
    list_first = ["red", "yellow", "green"]
    list_first.append("pink")
    print (" colour of index 4 : {} {} ".format(list_first[3], "only"))
    list_everything = [5, "yellow", 4.5, True]
    print (" list_everything of 2 : {} ".format(list_everything[1]))

def tuple_data_type():
    print ("call tuple_data_type ")
    tuple_first = ()
    print (len(tuple_first))
    tuple_first = ("red", "yellow", "green")
    print (" colour of 2 : {} {} ".format(tuple_first[1], "only"))
   # tuple_first[0] = "purple"
   # tuple_first[1] = "pink"
    print (" colour of 2 : {} {} ".format(tuple_first[1], "only"))

def dictionary_data_type():
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    print(thisdict)
    print(thisdict["brand"])



def error_hendling_one():
    print ("call error_hendling_one ")
    try:
        error_hendling_exception()
    except ok.BusinessException as BusinessEx:
        print(BusinessEx.message)
        
    except Exception as e :
        print("general error : ", e.args)    
        
    if is_err:
        print(is_err)


def error_hendling_real():
    raise ok.BusinessException("test error dataa")

def error_hendling_exception():
    3/0

def test_map_update():
    vals = {}
    vals.update({'satu':'one', 'dua':'two'})
    print(vals)
    vals.update({'satu':'one', 'dua':'three'})
    print(vals)