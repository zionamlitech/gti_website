def test_var_args(f_arg, *argv):
    print ("first principal of the school is:", f_arg)
    for arg in argv:
        print ("first Headmaster Academic of the school is :", arg)
        print ("first Headmaster Academic of the school is :", arg[1])
        print ("first Headmaster Academic of the school is :", arg[2])
        print ("first Headmaster Academic of the school is :", arg[3])

test_var_args('Mr Nyarko','Assist head','eggs','test')