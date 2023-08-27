from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("⩩ بدء استخراج الجلسة ☆.", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="⩩ الصفحة الرئيسية ☆.", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(
                "●○𝚂𝙴𝚉𝙰𝚁○●", url="https://t.me/UIU_II"
            )
        ],
        [
            InlineKeyboardButton("طريقة استخدام البوت ☆", callback_data="help"),
            InlineKeyboardButton("حول ⩩", callback_data="about"),
        ],
        [InlineKeyboardButton("َժٍᥱُ᥎", url="https://t.me/UIU_II")],
    ]

    START = """
📟¦اهلا بـك عزيـزي 📬 {},
⚡¦يـمكنك استـخـراج الـتـالـي
♻️¦تيرمـكـس تليثون للحسـابـات🏂
♻️¦تيرمـكـس تليثون للبوتــات🤖
🎧¦بايـروجـرام مـيوزك للحسابات🙋🏼‍♂️
🗽¦بايـروجـرام مـيوزك احدث اصدار🎊
🎧¦بايـروجـرام مـيوزك للبوتات🤖
- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس لتشغيل تلـيثون والبايروجرام لتشغيل سـورس اغــاني تم انشـاء هـذا البـوت بواسطـة

بواسطـة : زيـــــــٌن اݪــتأࢪيخ 🚸 !
    """

    HELP = """
 **الأوامر المتاحة**

/about - لحول البوت
/help - لمساعدتك
/start - لبدء البوت 
/repo - لإعطاء ريبو البوت
/generate - لاستخراج الجلسات 
/cancel - لإلغاء الاستخراج 
/restart - لترسيت البوت
"""

    # About Message
    ABOUT = """
**حول البوت** 
●○━━━━‌‌‏𝚂𝙴𝚉𝙰𝚁━━━━○●
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
⩩ انا بوت استخراج جلسات من سورس ســــيزر
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
قناة السورس : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/UIU_II)
لغة البرمجة : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)
اللغة : [ᴘʏᴛʜᴏɴ](www.python.org)
َժٍᥱُ᥎ : @p_m_4
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
●○━━━━‌‌‏𝚂𝙴𝚉𝙰𝚁━━━━○●
    """

    # Repo Message
    REPO = """
⋖━━❲𖣂❳━━●○𝚂𝙴𝚉𝙰𝚁○●━━❲𖣂❳━━⋗
⩩ انا بوت استخراج جلسات خاص بسورس ســــيزر
●○━━━━‌‌‏𝚂𝙴𝚉𝙰𝚁━━━━○●

⩩ السورس [●○𝚂𝙴𝚉𝙰𝚁○●](https://t.me/UIU_II)

●○━━━━‌‌‏𝚂𝙴𝚉𝙰𝚁━━━━○●
إذا كان لديك أي سؤال ، فراسل » المطور » [َժٍᥱُ᥎] @p_m_4
⋖━━❲𖣂❳━━●○𝚂𝙴𝚉𝙰𝚁○●━━❲𖣂❳━━⋗
   """
