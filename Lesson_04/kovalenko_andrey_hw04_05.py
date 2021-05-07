if __name__ == '__main__':
    from utils import currency_rates
    import sys

pair = sys.argv[1]
dict_data = currency_rates(pair)
print(f'{dict_data.get(pair)} {dict_data.get("timestamp")}')
