import asyncio
import httpx
from django.http import JsonResponse

async def async_timer_view(request):
    results = []

    # Loop assíncrono que simula o contador
    for num in range(1, 6):
        await asyncio.sleep(1)  # espera 1 segundo sem travar o servidor
        results.append(f"Contagem: {num}")

    # Requisição assíncrona para demonstrar async HTTP
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/get")
        results.append(f"Status HTTP: {r.status_code}")

    return JsonResponse({"result": results})

# Adicionado para teste de Pull Request

