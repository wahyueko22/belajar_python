from sub_helper  import function_only, class_only

def call_class():
    p1 = class_only.Person("John", 36)
    p2 = class_only.Person("John two", 37)
    print(p1.name)
    print(p1.age)
   
    class_only.Person.class_var = "updateeeee"
    p1.myfunc()
    print(p1.class_var)
    print(p2.class_var)
    #inheritance
    child1 = class_only.Student("wahyu", 50)
    print(child1.name)
    child1.myfunc()
    d = class_only.D()
    d.x()
    print(class_only.D.mro())
    #multiple inheritance
    td = class_only.TextDescriber('row row row your boat')
    print('--------')
    print(td.tokens)
    print(td.vocab)
    print(td.word_count)
    #getter setter
    mark = class_only.Geeks()
    mark.age = 19
    print(mark.age)

def main():
    print("Hello World!")
    """
    function_only.print_string()
    function_only.test_variable()
    function_only.test_conditional()
    function_only.looping_data()
    function_only.list_data_type()
    function_only.tuple_data_type()
    function_only.dictionary_data_type()
    
    function_only.error_hendling_one()
    """
    function_only.test_map_update()
    #call_class()

if __name__ == "__main__":
    main()

