# Designing a hash function

# Consider strings and sum up the ordinal values of the individual characters in them
def hash_function(text):
    return sum(ord(character) for character in text)


print(hash_function("Lorem"))
print(hash_function("Loren"))
print(hash_function("Loner"))


# Function is string-specific, suffers from poor distribution of hash codes, which tend to form clusters at similar
# input values. A slight change in the input has little effect on the observed output,
# the function remains insensitive to character order in the text.

# To fix the first problem:

def hash_function(key):
    return sum(ord(character) for character in str(key))


print("------1st Fix-----")
print(hash_function("Lorem"))
print(hash_function(True))
print(hash_function(3.14))


# Some objects may not have a textual representation suitable for the code above.
# To fix it trade str() for repr()


def hash_function(key):
    return sum(ord(character) for character in repr(key))


print("------2nd Fix-----")
print(hash_function("3.14"))
print(hash_function(3.14))


# To tackle the issue with anagrams, I'll modify my hash function by taking into consideration the character’s value
# as well as its position within the text


def hash_function(key):
    return sum(index * ord(character) for index, character in enumerate(repr(key), start=1))


print("------3rd Fix-----")
print(hash_function("Tiny"))
print(hash_function("This has a somewhat medium length."))
print(hash_function("This is very long and slow!" * 1_000_000))

# address unbounded growth of the output by taking the modulo (%) of the hash code against a known maximum size (% 100)

print("------4th Fix-----")
print(hash_function("Tiny") % 100)
print(hash_function("This has a somewhat medium length.") % 100)
print(hash_function("This is very long and slow!" * 1_000_000) % 100)

# Next issue of suboptimal distribution of hash codes through clustering and by not taking advantage of all the
# available slots

from hash_distribution import plot, distribute
from string import printable

print("Show the uneven distribution")
print(plot(distribute(printable, 6, hash_function)))

# The two apostrophes added by repr() cause virtually all keys in this example to result in an even hash number,
# leading to one container missing from the histogram

# Avoid this by removing the left apostrophe if it exists
print("hash values before removing left apostrophe")
print(hash_function("a"), hash_function("b"), hash_function("c"))


def hash_function(key):
    return sum(index * ord(character) for index, character in enumerate(repr(key).lstrip("'"), 1))


print("hash values after removing left apostrophe")
print(hash_function("a"), hash_function("b"), hash_function("c"))
print("Distribution after improving the function")
print(plot(distribute(printable, 6, hash_function)))