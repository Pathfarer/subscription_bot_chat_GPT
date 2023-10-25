import openai


async def get_image_url(promt, number):
    image_resp = await openai.Image.acreate(prompt=promt, n=number, size="512x512")
    return [item['url'] for item in image_resp["data"]]
