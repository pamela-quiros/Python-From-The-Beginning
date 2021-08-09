def unlimited_arguments(*args, **keyword_arg): #* turned it into a tuple.
    print(keyword_arg)
    for argument in keyword_arg.items():
        print(argument)

unlimited_arguments(1,2,3,4,name='Pam', age=23)