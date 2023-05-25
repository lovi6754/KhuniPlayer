from pyrogram import Client, filters

from Bikash import app
from Bikash.utils.bgtmusic.bk import command

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    filters.command("owner")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def owner(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f29396af160a0b94818e4.jpg",
        caption=f"""🥀 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐎𝐰𝐧𝐞𝐫 𝐎𝐟 (𝐋𝐨𝐯𝐞𝐠𝐮𝐫𝐮 𝐒𝐞𝐫𝐯𝐞𝐫), 𝐈𝐟 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬 𝐎𝐫 𝐎𝐭𝐡𝐞𝐫𝐬 𝐋𝐢𝐧𝐤 𝐓𝐡𝐞𝐧 [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/loveguruoo) & 𝐂𝐥𝐢𝐜𝐤 𝐎𝐭𝐡𝐞𝐫'𝐬 𝐁𝐮𝐭𝐭𝐨𝐧 & 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐎𝐫 𝐆𝐫𝐨𝐮𝐩.. 🥀 .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 𝗟𝗼𝘃𝗲𝗴𝘂𝗿𝘂 𝗦𝗲𝗿𝘃𝗲𝗿 🥀", url=f"https://t.me/loveguruoo")
            ],          
            [
                    InlineKeyboardButton(
                        "🥀 𝗠𝗿 𝗟𝗼𝘃𝗲𝗴𝘂𝗿𝘂 🥀", url=f"https://t.me/loveguruo")
                ],
                [
                    InlineKeyboardButton(
                        "🥀 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 🥀", url=f"https://t.me/innocentop"
                    ),
                    InlineKeyboardButton(
                        "🥀 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 🥀", url=f"https://t.me/loveguruoo")
                ]
            ]
        ),
    )
