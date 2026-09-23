from fastapi import APIRouter

from app.modelos.cliente import Cliente

router = APIRouter(
    prefix="/clientes"
)

@router.get("/", response_model=list[Cliente])
async def listar_clientes():

    clientes_list = [Cliente(nome="Glauber", email="glauber@batista.com", telefone="123456789"),
                     Cliente(nome="João", email="joao@batista.com", telefone="123456789")]
    return clientes_list
