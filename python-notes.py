'''
Notes :
    List Methods :
        append()	Adds an element at the end of the list
        insert()	Adds an element at the specified position
        pop()	Removes the element at the specified position

        clear()	Removes all the elements from the list
        copy()	Returns a copy of the list
        count()	Returns the number of elements with the specified value
        extend()	Add the elements of a list (or any iterable), to the end of the current list

        index()	Returns the index of the first element with the specified value
            x = [1,2,3]
            x.index(2) => 1

        removing :
            remove()	Removes the first item with the specified value
            x = [1,2,3]
            x.remove(1) => [2,3]
            del x[0]

        reverse()	Reverses the order of the list

        Sorting :
            sort() sorts in ascending order
            def sortFunc(elem):
                return elem;
            sort(key=sortFunc,reverse = false)	Sorts the list

        Filter :
            result = [el for el in A if el > 5]
            result = [el for el in A if el not in subset_of_A]

        Mapping :
            result = [el * 2 for el in A]
            result = map(lambda el: el*2, A)

        Array to Set :
            result = set(A)

        Merging arrays :
            l1 = [1, 2, 3]
            l2 = [4, 5, 6]
            joined_list = [*l1, *l2] => [1, 2, 3, 4, 5, 6]
            joined_list = l1 + l2 => [1, 2, 3, 4, 5, 6]
            l1.extend(l2) => [1, 2, 3, 4, 5, 6]
            list(chain(l1,l2)) => [1, 2, 3, 4, 5, 6]
        Slicing :
            x = "123456789"
            x[:2] => [1,2]
            x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
            x[0:10] => [1,2,3,4,5,6,7,8,9,10]
            x[1:10] => [2,3,4,5,6,7,8,9,10]
            x[-1] => x[20]

    HashMaps : {}
        clear()	Removes all the elements from the dictionary
        copy()	Returns a copy of the dictionary
        fromkeys()	Returns a dictionary with the specified keys and values
        get()	Returns the value of the specified key
        items()	Returns a list containing a tuple for each key value pair
        keys()	Returns a list containing the dictionary's keys
        pop()	Removes the element with the specified key
        popitem()	Removes the last inserted key-value pair
        setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
        update()	Updates the dictionary with the specified key-value pairs
        values()	Returns a list of all the values in the dictionary
    Sets :
        add()	Adds an element to the set
        clear()	Removes all the elements from the set
        copy()	Returns a copy of the set
        difference()	Returns a set containing the difference between two or more sets
        difference_update()	Removes the items in this set that are also included in another, specified set
        discard()	Remove the specified item
        intersection()	Returns a set, that is the intersection of two other sets
        intersection_update()	Removes the items in this set that are not present in other, specified set(s)
        isdisjoint()	Returns whether two sets have a intersection or not
        issubset()	Returns whether another set contains this set or not
            x = {"a", "b", "c"}
            y = {"f", "e", "d", "c", "b", "a"}

            z = x.issubset(y) => true

        issuperset()	Returns whether this set contains another set or not
            z = y.issuperset(x) => true

        pop()	Removes an element from the set
        remove()	Removes the specified element
        symmetric_difference()	Returns a set with the symmetric differences of two sets
        symmetric_difference_update()	inserts the symmetric differences from this set and another
        union()	Return a set containing the union of sets
        update()	Update the set with the union of this set and others

    For Loops :
        for x in range(6(from 0 to 5)):
        for x in range(2(start), 30(max), 3(step)):
        for x in arr: (X is the array element)
        for x in range(len(arr)): (from 0 to length - 1)

    Ifs :
        if key not in hashMap: == if not hashMap.get(i):
        if x !=/is not y :

    Swap :
        x = 5
        y = 10
        x, y = y, x

    Strings:
        capitalize()	Converts the first character to upper case
        casefold()	Converts string into lower case
        center()	Returns a centered string
        count()	Returns the number of times a specified value occurs in a string
        encode()	Returns an encoded version of the string
        endswith()	Returns true if the string ends with the specified value
        expandtabs()	Sets the tab size of the string
        find()	Searches the string for a specified value and returns the position of where it was found
        format()	Formats specified values in a string
        format_map()	Formats specified values in a string
        index()	Searches the string for a specified value and returns the position of where it was found
        isalnum()	Returns True if all characters in the string are alphanumeric
        isalpha()	Returns True if all characters in the string are in the alphabet
        isdecimal()	Returns True if all characters in the string are decimals
        isdigit()	Returns True if all characters in the string are digits
        isidentifier()	Returns True if the string is an identifier
        islower()	Returns True if all characters in the string are lower case
        isnumeric()	Returns True if all characters in the string are numeric
        isprintable()	Returns True if all characters in the string are printable
        isspace()	Returns True if all characters in the string are whitespaces
        istitle()	Returns True if the string follows the rules of a title
        isupper()	Returns True if all characters in the string are upper case
        join()	Joins the elements of an iterable to the end of the string
        ljust()	Returns a left justified version of the string
        lower()	Converts a string into lower case
        lstrip()	Returns a left trim version of the string
        maketrans()	Returns a translation table to be used in translations
        partition()	Returns a tuple where the string is parted into three parts
        replace()	Returns a string where a specified value is replaced with a specified value
        rfind()	Searches the string for a specified value and returns the last position of where it was found
        rindex()	Searches the string for a specified value and returns the last position of where it was found
        rjust()	Returns a right justified version of the string
        rpartition()	Returns a tuple where the string is parted into three parts
        rsplit()	Splits the string at the specified separator, and returns a list
        rstrip()	Returns a right trim version of the string
        split()	Splits the string at the specified separator, and returns a list
        splitlines()	Splits the string at line breaks and returns a list
        startswith()	Returns true if the string starts with the specified value
        strip()	Returns a trimmed version of the string
        swapcase()	Swaps cases, lower case becomes upper case and vice versa
        title()	Converts the first character of each word to upper case
        translate()	Returns a translated string
        upper()	Converts a string into upper case
        zfill()	Fills the string with a specified number of 0 values at the beginning
    Important :
        x++ => x += 1
        (str2[j] if j < len(str2) else None)  // prevent out of index
        temp = states.copy()

'''
words = ['i','i','love','love','k'] => [('i',2),('love',2),('k',1)]
collections.Counter(words).items() #counting the words in arr and storing it in tuple
## storing based on count
## (-) => for reverse
## x[1] => for count
## x[0] for characters
sorter(collections.Counter(words).items(),lambda x: (-x[1],x[0]))

def getRestArr(arr1,arr2):
    tmp = list(arr1)
    i = j = 0;
    while i < len(tmp) and j < len(arr2):
        if tmp[i] == arr2[j]:
            del tmp[i]
            j += 1
            continue
        i += 1
    return ''.join(tmp)
'''
Detecting :
Typically, all the problems that require to maximize or minimize certain quantity or counting problems
 that say to count the arrangements under certain condition or certain probability problems can be solved by using Dynamic Programming.
All dynamic programming problems satisfy the overlapping subproblems property and most of the classic dynamic problems
 also satisfy the optimal substructure property.
 Once, we observe these properties in a given problem, be sure that it can be solved using DP.
DP Template:

    Goal :
    State:
    BaseCase:
    Recurrence:
    Order of iteration:
'''
