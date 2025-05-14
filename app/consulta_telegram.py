
from pyrogram import Client
import asyncio
import re
import requests

api_id = 28382442
api_hash = "5f5cede83ecaedef4234fc1bd095a5c"
YANBOT = "Yanbuscabot"

async def consultar_bot(tipo: str, valor: str) -> str:
    comando = f"/{tipo} {valor}"
    async with Client("session", api_id=api_id, api_hash=api_hash) as app:
        await app.send_message(YANBOT, comando)
        await asyncio.sleep(10)
        async for msg in app.get_chat_history(YANBOT, limit=10):
            if msg.text and ("copiar tudo" in msg.text.lower() or "baixar pdf" in msg.text.lower()):
                # Extrai link
                link_match = re.search(r"https://\S+", msg.text)
                if link_match:
                    url = link_match.group(0)
                    if url.endswith(".pdf"):
                        r = requests.get(url)
                        with open("resultado.pdf", "wb") as f:
                            f.write(r.content)
                        return "PDF baixado com sucesso."
                    elif url.endswith(".txt"):
                        r = requests.get(url)
                        with open("resultado.txt", "wb") as f:
                            f.write(r.content)
                        return "TXT baixado com sucesso."
                return msg.text
    return "Nenhuma resposta relevante recebida."
