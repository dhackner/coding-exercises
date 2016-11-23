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


def final_answer_products(array):
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


def products_with_division(array):
    try:
        idx_of_0 = array.index(0)
    except ValueError:
        total_product = reduce(lambda x, y: x*y, array)
        return [total_product / element for element in array]
    else:
        # If there is exactly one 0, then there still exists a product when that
        # index is being excluded, otherwise it's all 0's
        product = reduce(lambda x, y: x*y, array[:idx_of_0]+array[idx_of_0 + 1:])
        prefix = [0] * idx_of_0
        post_count = len(array) - idx_of_0 - 1  # -1 because of product
        postfix = [0] * post_count
        return prefix + [product] + postfix

try:
    products_with_division(None)
    assert False
except Exception:
    pass
try:
    products_with_division([])
    assert False
except Exception:
    pass
try:
    products_with_division([1])
    assert False
except Exception:
    pass

assert set(products_with_division([1, 7, 3, 4])) == set([84, 12, 28, 21])  # Example case
assert set(products_with_division([7, 3, 4])) == set([12, 28, 21])  # Checking for an off by 1 error
assert set(products_with_division([3, 4])) == set([3, 4])  # Checking for an off by 1 error
# Learning: Don't forget the 0 case with math
assert set(products_with_division([0, 1, 2])) == set([2, 0, 0])  # Single-0 case
assert set(products_with_division([0, 1, 0])) == set([0, 0, 0])  # Multi-0 case
print 'OK'
