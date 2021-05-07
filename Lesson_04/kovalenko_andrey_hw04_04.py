# Подключим наш модуль.
from Lesson_04 import utils as utils

# Дернем из него данные по валютам.
print(utils.currency_rates("usd"))
print(utils.currency_rates("eur"))
print(utils.currency_rates("gbp"))
