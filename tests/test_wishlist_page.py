from src.page_objects.wishlist_page import WishlistPage

## Validar remover un item de la wishlist
def test_wishlist(web_drivers):
    wishlist_page = WishlistPage(*web_drivers)
    wishlist_page.open()
    wishlist_page.wishlist_logim("tempv1@gmail.com","654321")
    wishlist_page.wishlist_remove()
