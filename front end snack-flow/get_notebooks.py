import asyncio
from notebooklm import NotebookLMClient
import json

async def main():
    async with await NotebookLMClient.from_storage() as client:
        notebooks = await client.notebooks.list()
        result = []
        for nb in notebooks:
            if "2026-04" in str(nb.created_at) or "Web site design" in nb.title or "AI-Powered Motion Design" in nb.title or "Mastering Modern Web Design" in nb.title:
                try:
                    chat_res = await client.chat.ask(nb.id, "Provide a comprehensive summary of all the key guidelines, notes, and requirements from this notebook that are relevant to designing and building a web project.")
                    result.append({"title": nb.title, "summary": chat_res.answer})
                except Exception as e:
                    print(f"Error querying {nb.title}: {e}")
        
        with open("notebook_summaries.json", "w") as f:
            json.dump(result, f, indent=2)

asyncio.run(main())
