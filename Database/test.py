from users import Database
import asyncio
from gtts import gTTS


async def test():
    db = Database()
    await db.create_pool()
    await db.create_table_beginner()
    # words = await db.select_words_by_unit(unit=2)
    # for word in words:
    #     print(word[1])
    #     myobj = gTTS(text=word[1], lang="en", slow=False)
    #     myobj.save(word[1] + " - " + word[2] + ".mp3")
    # print(words)
    en_word = await db.select_file_ids_by_unit(2)
    print(en_word)



loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(test())
