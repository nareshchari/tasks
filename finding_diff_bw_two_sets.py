def finding_diff_bw_two_sets(*args):
    a,b=args
    print(f"finding difference a with b: {a.difference(b)}")
    print(f"finding difference b with a: {b.difference(a)}")



if __name__ == "__main__":
    a,b = {1,2,3,4,5},{2,3,5,7,8}
    finding_diff_bw_two_sets(a,b)
    c,d = {'a',True,(1,2)},{'b',False,True,(1,2)}
    finding_diff_bw_two_sets(c,d)
    # not posible with sets of lists cuz list is mutable so not hashable
    # not posible with sets of dictionaries cuz dict is mutable so not hashable
    # posible once are numbers(int,float),set,tuple,True,bytes,bytearray
    e,f={bytes([1,2]),"hello","john"},{'hello','jessy',bytes([1,5])}
    finding_diff_bw_two_sets(e,f)
    # not posible
    # g,h = {1,([1,2],3),'joseph',"rana"},{"rana",({'a':'b'},4,5),6}
    # finding_diff_bw_two_sets(g,h)















    # not posible set of lists
    """because:
                Sets require their items to be hashable. Out of types predefined by Python only the immutable ones,
                such as strings, numbers, and tuples, are hashable. Mutable types, such as lists and dicts, are not
                hashable because a change of their contents would change the hash and break the lookup code.

                Since you're sorting the list anyway, just place the duplicate removal after the list is already
                sorted. This is easy to implement, doesn't increase algorithmic complexity of the operation, and
                doesn't require changing sublists to tuples
    """
#
