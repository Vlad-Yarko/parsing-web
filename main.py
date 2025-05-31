from src.parse.olx import OLXParse
from src.parse.kasta import KastaParse
from src.parse.shafa import ShafaParse


with open("src/test_html/olx_content", encoding='utf-8') as file:
    olx_content = file.read()
with open("src/test_html/kasta_content", encoding='utf-8') as file:
    kasta_content = file.read()
with open("src/test_html/shafa_content", encoding='utf-8') as file:
    shafa_content = file.read()


olx = OLXParse(olx_content)
kasta = KastaParse(kasta_content)
shafa = ShafaParse(shafa_content)

olx.parse()
kasta.parse()
shafa.parse()


print("OLX")
print(olx.title, olx.price)
print("OLX")

print("KASTA")
print(kasta.title, kasta.price)
print("KASTA")

print("SHAFA")
print(shafa.title, shafa.price)
print("SHAFA")
