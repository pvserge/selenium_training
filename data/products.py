from generator.product import ProductGenerator


def get_random_product():
    return ProductGenerator().generate_product()

product = get_random_product()

testdata = [product]
