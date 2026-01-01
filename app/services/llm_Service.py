import asyncio
class LLMService:
    async def generate(self,prompt:str)->str:
        asyncio.sleep(5)
        return f"llm response for: {prompt}"
    