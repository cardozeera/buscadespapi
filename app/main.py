
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio
from consulta_telegram import consultar_bot

app = FastAPI()

class ConsultaRequest(BaseModel):
    tipo: str  # "cpf3", "nome", "telefone"
    valor: str
    usuario: str = "admin"

@app.post("/consulta")
async def consulta(request: ConsultaRequest):
    try:
        resultado = await consultar_bot(request.tipo, request.valor)
        return {"status": "ok", "resultado": resultado}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
