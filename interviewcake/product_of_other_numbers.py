# 2 - https://www.interviewcake.com/question/python/product-of-other-numbers

# No division allowed

# Algorithm: O(n2) - for each element, return product(list - element)
# O(2n) - [a, b, c, d] - for 'b', it is a*c*d. i.e. all to the left * all to
# the right. Make a list for each direction where for a given index, the value
# is the product of all values to the left/right of it. On the construction of
# the rightwards list, for each index, return the current product value * the
# value from the leftwards list.


def first_pass_products(array):
    if array is None or len(array) < 2:
        raise Exception()
    else:
        left_products = [1]
        right_product = 1
        for element in array:
            left_products.append(left_products[-1] * element)
        for index in range(len(array) - 1, -1, -1):  # Reverse
            yield left_products[index] * right_product
            right_product *= array[index]


def products(array):
    if array is None or len(array) < 2:
        raise Exception()
    else:
        products = []
        product = 1
        for element in array:
            products.append(product)
            product *= element
        index = len(array) - 1
        product = 1
        for index in range(len(array) - 1, -1, -1):
            products[index] *= product
            product *= array[index]
        return products

try:
    products(None)
    assert False
except Exception:
    pass
try:
    products([])
    assert False
except Exception:
    pass
try:
    products([1])
    assert False
except Exception:
    pass

assert set(products([1, 7, 3, 4])) == set([84, 12, 28, 21])  # Example case
assert set(products([7, 3, 4])) == set([12, 28, 21])  # Checking for an off by 1 error
assert set(products([3, 4])) == set([3, 4])  # Checking for an off by 1 error
# Learning: Don't forget the 0 case with math
assert set(products([0, 1, 2])) == set([2, 0, 0])  # 0 case
print 'OK'
