# Я хотів створити атоматині ключі , щоб не було необхідності
# вписувати імена кожного з ключів

cities = {'kyiv':
              {'country': 'ukraine',
               'population': '40 mil.',
               'river': 'dnipro'},
          'berlin':
              {'country': 'germany',
               'population': '4 mil.',
               'river': 'spree'},
          'Kropyvnytskyi':
              {'country': 'ukraine',
               'population': '260000.',
               'river': 'ingul'},
          }

for citi_name, citi_info in cities.items():
    print(f"\nCiti: {citi_name.title()}")

for infokey in citi_info.keys():
    print(infokey.title())
for riverkey in citi_info.keys():
    print(riverkey.title())

    # info = f"{citi_info[infokey]} {citi_info['population']}"
    # river = citi_info['river']

    # print(f"\tFull name: {info.title()}")
    # print(f"\tLocation: {river.title()}")
