from src.page_objects.register_page import RegisterPage


def test_register(web_drivers):
    register_page = RegisterPage(*web_drivers)
    register_page.register("Miguel","Perex","temp@gmail.com","987654321","654321","654321")
    mensaje = register_page.confirm_register()
    assert "Success" in mensaje, "No se registro"
    register_page.continue_register()

