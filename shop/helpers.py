import uuid
import os
import locale

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('shop/images/product/', filename)


def format_currency_vietnam(number):
     locale.setlocale(locale.LC_ALL, 'vi_VN')
     formatted = locale.format_string("%d",number, grouping=True) +" đ"
     return formatted

def chunked(items, quantity_per_group):
     result = []
     for i in range(0, len(items), quantity_per_group):
         chunk =  items[i:i + quantity_per_group]

         result.append(chunk)
     return result

def get_order_code():
    import random
    import string
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return code