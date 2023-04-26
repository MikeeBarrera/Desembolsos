from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument('window-size=1200x600')
options.add_argument('no-sandbox')
options.add_argument('disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

# Abre la página web
driver.get('ruta/a/tu/pagina/formulario.html')

# Espera a que se cargue el formulario
form = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'form'))
)

# Obtiene el campo de entrada de texto
num_iteraciones_input = form.find_element_by_name('num_iteraciones')

# Espera a que el usuario complete el formulario y haga clic en el botón de enviar
submit_button = form.find_element_by_css_selector('input[type="submit"]')
submit_button.click()

# Espera a que la página se cargue y obtiene el número de iteraciones ingresado por el usuario
num_iteraciones = int(num_iteraciones_input.get_attribute('value'))

# Ejecuta el código el número de veces especificado por el usuario
for i in range(num_iteraciones):
    # Inicia sesión en el sitio web
    # ...

driver.quit()
