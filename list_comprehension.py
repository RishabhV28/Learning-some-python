#[expression for item in iterable]

#Square number in a list
'''
squares=[x**2 for x in range(5)]
print(squares)'''

#filtr only even numbers
'''
evens=[x for x in range(10) if x%2==0]
print(evens)


labels=['even' if x%2==0 else 'odd' for x in range(5)]
print(labels)'''