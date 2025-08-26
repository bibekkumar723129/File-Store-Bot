# ────────────────────────────────────────────────────────────────

# ✅ THIS PROJECT IS DEVELOPED AND MAINTAINED BY @trinityXmods (TELEGRAM)
# 🚫 DO NOT REMOVE OR ALTER THIS CREDIT LINE UNDER ANY CIRCUMSTANCES.

# ⭐ FOR MORE HIGH-QUALITY OPEN-SOURCE BOTS, FOLLOW US ON GITHUB.
# 🔗 OFFICIAL GITHUB: https://github.com/Trinity-Mods
# 📩 NEED HELP OR HAVE QUESTIONS? REACH OUT VIA TELEGRAM: @velvetexams

# ────────────────────────────────────────────────────────────────

from pyrogram import __version__
from bot import Bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import PRICE1, PRICE2, PRICE3, PRICE4, PRICE5, UPI_ID, UPI_IMAGE_URL, SCREENSHOT_URL

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ More Bots: <a href='https://t.me/UniformMovies'>Uɴɪғᴏʀᴍ Mᴏᴠɪᴇs</a>\n○ Language: <a href='https://www.python.org/'>Python 3</a>\n○ Fueled By: <a href='https://t.me/AdultsVideoLink'>Aᴅᴜʟᴛs Vɪᴅᴇᴏ Lɪɴᴋ</a>\n○ Server: <a href='https://www.ubuntu.com/'>Private VPS</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
    elif data == "buy_prem":
        await query.message.edit_text(
            text= (
    f"👋 <b>Wᴇʟᴄᴏᴍᴇ, @{query.from_user.username}!</b>\n\n"
    f"🌟 <b>Pʀɪᴍᴇ Mᴇᴍʙᴇʀsʜɪᴘ Pʟᴀɴs:</b>\n\n"
    f"💫 <b>{PRICE1}</b> — <i>7 Dᴀʏs Aᴄᴄᴇss</i>\n"
    f"💫 <b>{PRICE2}</b> — <i>1 Mᴏɴᴛʜ Aᴄᴄᴇss</i>\n"
    f"💫 <b>{PRICE3}</b> — <i>3 Mᴏɴᴛʜs Aᴄᴄᴇss</i>\n"
    f"💫 <b>{PRICE4}</b> — <i>6 Mᴏɴᴛʜs Aᴄᴄᴇss</i>\n"
    f"💫 <b>{PRICE5}</b> — <i>1 Yᴇᴀʀ Aᴄᴄᴇss</i>\n\n"
    f"💵 <b>Uᴘɪ ID:</b> <code>{UPI_ID}</code>\n\n"
    f"📸 <a href='{UPI_IMAGE_URL}'>Cʟɪᴄᴋ Hᴇʀᴇ ᴛᴏ Sᴄᴀɴ Qʀ Cᴏᴅᴇ</a>\n\n"
    f"🧾 <b>🔐 Aꜰᴛᴇʀ Pᴀʏᴍᴇɴᴛ:</b> Sᴇɴᴅ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ.\n\n"
    f"💬 <b>Nᴇᴇᴅ Hᴇʟᴘ?</b> <a href='https://t.me/DadyIsCalling'>Cᴏɴᴛᴀᴄᴛ DadyIsCalling</a>"
),
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [   
                    [
                        InlineKeyboardButton("ꜱᴇɴᴅ ᴘᴀʏᴍᴇɴᴛ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ 📸", url=(SCREENSHOT_URL))
                    ],
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )

# ────────────────────────────────────────────────────────────────

# ✅ THIS PROJECT IS DEVELOPED AND MAINTAINED BY @trinityXmods (TELEGRAM)
# 🚫 DO NOT REMOVE OR ALTER THIS CREDIT LINE UNDER ANY CIRCUMSTANCES.

# ⭐ FOR MORE HIGH-QUALITY OPEN-SOURCE BOTS, FOLLOW US ON GITHUB.
# 🔗 OFFICIAL GITHUB: https://github.com/Trinity-Mods
# 📩 NEED HELP OR HAVE QUESTIONS? REACH OUT VIA TELEGRAM: @velvetexams

# ────────────────────────────────────────────────────────────────  
