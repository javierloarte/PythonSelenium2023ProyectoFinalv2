from src.page_objects.search_page import SearchPage

## Validar agregar un item al carrito de compra

def test_search(web_drivers):
    search_page = SearchPage(*web_drivers)
    search_page.open()
    search_page.search("Nikon")
    search_page.total_search()

