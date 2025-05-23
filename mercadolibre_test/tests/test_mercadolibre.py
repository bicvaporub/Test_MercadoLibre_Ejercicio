from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_busqueda_playstation(driver):
    wait = WebDriverWait(driver, 15)

    # 1. Ir al sitio principal
    driver.get("https://www.mercadolibre.com")

    # 2. Seleccionar México
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#MX"))).click()

    # 3. Buscar "playstation 5"
    search_input = wait.until(EC.presence_of_element_located((By.NAME, "as_word")))
    search_input.send_keys("playstation 5")
    search_input.submit()

    # 4. Filtrar por condición "Nuevo"
    xpath_nuevo = "//h3[text()='Condición']/../descendant::span[text()='Nuevo']"
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_nuevo)))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_nuevo))).click()

    # 5. Filtrar por ubicación "Ciudad de México"
    xpath_cdmx = "//h3[text()='Ubicación']/../descendant::span[text()='Distrito Federal']"
    filtro_cdmx = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_cdmx)))
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", filtro_cdmx)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_cdmx))).click()

    # 6. Ordenar por "Mayor precio"
    classname_dropdown_ordenar = "andes-dropdown__trigger"
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, classname_dropdown_ordenar)))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, classname_dropdown_ordenar))).click()

    xpath_mayor_precio = "//span[text()='Mayor precio']"
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_mayor_precio)))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_mayor_precio))).click()

    # 7. Obtener y mostrar los primeros 5 productos
    css_selector_items = "ol.ui-search-layout li.ui-search-layout__item"
    WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, css_selector_items)))
    print("\nPrimeros 5 productos:")
    productos_validos = []

    for i in range(1, 7):
        try:
            xpath_item = f"(//ol[contains(@class,'ui-search-layout')]//li[contains(@class,'ui-search-layout__item')])[{i}]"
            item = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_item)))

            title_elem = item.find_element(By.CSS_SELECTOR, "h3.poly-component__title-wrapper a.poly-component__title")
            price_elem = item.find_element(By.CSS_SELECTOR, "div.poly-price__current span.andes-money-amount__fraction")

            title = title_elem.text.strip()
            price = price_elem.text.strip()

            if title and price:
                productos_validos.append(f"{title} - {price}")

        except Exception as e:
            print(f"[{i}] Error al obtener producto: {e}")
            continue

    for idx, producto in enumerate(productos_validos, 1):
        print(f"{idx}. {producto}")
#No está encontrando el primer elemento para obtener su titulo y precio, por eso extendí el bucle hasta 7, para obtener 5 elementos