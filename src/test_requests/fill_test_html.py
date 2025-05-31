import asyncio
from request import Request


CONTENT_FOLDER = "src/test_html/"


class HTMLContentWrite:
    def __init__(self, html: str, file_name: str):
        self.html = html
        self.file_name = file_name
        
    def write(self) -> None:
        with open(f"{CONTENT_FOLDER}{self.file_name}_content", mode='w', encoding='utf-8') as file:
            file.write(self.html)
            
            
async def main():
    olx_content = await Request("https://www.olx.ua/d/uk/").request("obyavlenie/orignaln-krosvki-hoka-44-rozmr-IDWBbY6.html")
    shafa_content = await Request("https://shafa.ua/uk/").request("men/obuv/krossovki/186892382-krosivki-cholovichi?from-adv=true")
    kasta_content = await Request("https://kasta.ua/uk/").request("product/23409938:623/")
    return olx_content, shafa_content, kasta_content


olx_content, shafa_content, kasta_content = asyncio.run(main())
            

HTMLContentWrite(olx_content, "olx").write()
HTMLContentWrite(shafa_content, "shafa").write()
HTMLContentWrite(kasta_content, "kasta").write()
