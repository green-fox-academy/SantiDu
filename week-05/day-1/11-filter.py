def myfilter(function, iterable):
    return (element for element in iterable if function(element))

