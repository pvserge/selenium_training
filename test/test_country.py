from model.country import Country


def test_countries_order(app):
    country_list = app.country.get_country_list_countries_page()
    assert country_list == sorted(country_list, key=Country.get_name)
    for country in country_list:
        if int(country.zones) > 0:
            zones_list = app.country.get_zones_list_edit_country_page(country)
            assert zones_list == sorted(zones_list, key=Country.get_name)


def test_zones_order(app):
    country_list = app.country.get_country_list_geozones_page()
    for country in country_list:
        zones_list = app.country.get_zones_list_edit_zone_page(country)
        print(zones_list)
        assert zones_list == sorted(zones_list, key=Country.get_name)
