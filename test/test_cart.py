

def test_add_products_to_cart(app):
    amount_of_product = 3
    for i in range(amount_of_product):
        app.product.add_first_product_to_cart()
    app.product.delete_products_from_cart()
    assert not app.product.is_summary_table_exists()
