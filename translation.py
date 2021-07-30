from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
Hello {} 👋

You are warmly welcome to Cortana Youtube Downloader Bot 🤗

In this bot, You can download any youtube video by sending url 😊
"""
    HELP_TEXT = """
<b><u>Link to Media or File</u></b>
➠ මම ඔයාලට youtube ලින්ක් එකක් දැම්මම ඒකට අදාල වීඩියෝ එක video/ document ලෙස ඩවුන්ලෝඩ් කරගන්න පුලුවන් 🙂

<b><u>Set Thumbnail</u></b>
➠ මුලින්ම ඔයාල මට photo එකක් එවන්න ඕන Thumbnail එකක් විදියට Save කරගන්න🙂 නැත්නම් මම වැඩ කරන්නෙ නැ 😐

<b><u>Deleting Thumbnail</u></b>
➠ " /delthumb " මේ command එක මගින් ඔයාල ඇඩ් කරගත්ත Thumbnail එක අයින් කරගන්න පුලුවන් 🙂

<b><u>Show Thumbnail</u></b>
➠ " /showthumb " මේ command එක යැවීමෙන් ඔයාල ඇඩ් කරපු Thumbnail එක බලාගන්න පුලුවන් 🙂 

Thumnail කියන්නෙ File එක ලස්සන කරන්න මම දාන පොටෝ එක හොදේ 🤣🙏

Made by @percy_jackson_4🇱🇰
Support Group : @leosupportx 🇱🇰
Updates Channel : @new_ehi 🇱🇰
"""
    ABOUT_TEXT = """
- **Bot :** `Cortana YouTube Downloader`
- **Creator :** [Master Chief](https://telegram.me/percy_jackson_4)
- **Updates Channel :** [Cortana Updates](https://telegram.me/Cortana_Updates)
- **Support Group :** [Cortana Support 🇱🇰](https://telegram.me/Cortana_BOTS)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram v1.2.0](https://pyrogram.org)
- **Server :** [VPS](https://digitalocean.com)
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Developer🧑‍💻', url='https://telegram.me/percy_jackson_4'),
        InlineKeyboardButton('Rate us ★', url='https://t.me/tlgrmcbot?start=Cortana_YTDLBot-review')
        ],[
        InlineKeyboardButton('Updates Channel 🗣', url='https://telegram.me/Cortana_Updates'),
        InlineKeyboardButton('Support Group 👥', url='https://telegram.me/Cortana_BOTS')
        ],[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
    BLOCK_LIST_TEXT = "මේ URL එක බ්ලොක්😪 ඒනිසා මේක ඩවුන්ලෝඩ් බැ😶 මේ යූසර්නේම් එකෙන් ගිහින් බලන්න පොඩ්ඩක්.\n\nUse @Cortana_ANYDLBot 🇱🇰"
    FORMAT_SELECTION = """<b>Select the desired format:</b> <a href='{}'>file size might be approximate</a>
    
Send your custum thumbnail if required.
You can use /delthumb to delete the auto-generated thumbnail."""
    CHECKING_LINK = "<code>Analysing Your Link\n @Cortana_YTDLBot 🇱🇰</code>⏳"
    BANNED_USER_TEXT = "<code>You are Banned!</code>"
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""
    DOWNLOAD_START = "<code>ඩවුන්ලෝඩ් කිරීම ඇරඹුනා🙂...\n@Cortana_YTDLBot 🇱🇰</code>"    
    UPLOAD_START = "<code>දැන් Telegram එකට අප්ලෝඩ් වෙන ගමන් පොඩ්ඩක් ඉවසන්න ඩාලින් 🥰\nමේ මැසේජ් එක ගොඩක් වෙලා තියෙනවනම් ඒකට හේතුව ඔයා thumbnail image එකක් මට නොදුන්න එක😪\nඒ නිසා මට thumbnail image එකක් යවල ආයෙ ලින්ක් එක දාන්න 😊\n\n@Cortana_ANYDLBot 🇱🇰...</code>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "ඔන්න ඩවුන්ලෝඩ් උනා තත්පර {} ක් ඇතුලත 😏 . \n\nටෙලිග්‍රෑම් එකට අප්ලෝඩ් උනා තත්පර {} ක් ඇතුලත😏"
    RCHD_TG_API_LIMIT = "ඩවුන්ලෝඩ් උනා තත්පර {} ක් ඇතුලත.\nෆයිල් එකේ ප්‍රමාණය: {}\nසමාවෙන්න මට මේ ෆයිල් එක ටෙලිග්‍රෑම් එකට අප්ලෝඩ් කරන්න බැ😪 මොකද ෆයිල් size එක 1.95Gb වලට වඩා මට අප්ලෝඩ් කිරීමට ටෙලිග්‍රෑම් එකෙන් අවසර නැති නිසා😪\nඔයාට යම් කිසි උදව්වක් අවශ්‍යනම් මේ යූසර්නේම් එකට මැසේජ් එකක් දාන්න [Master Chief 🇱🇰](@percy_jackson_4)."
    CUSTOM_CAPTION_UL_FILE = "<b>Join :-</b> @Cortana_Updates 🇱🇰"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    NO_VOID_FORMAT_FOUND = "<code>{}</code>"
    REPORT_SITE_TEXT = "<code>Sorry not uploading in this site here because this site is reporting site.</code>"
    SOMETHING_WRONG = "<code>Something Wrong. Try again.</code>"
    FORCE_SUBSCRIBE_TEXT = "<code>Sorry ඩාලින් ඔයා අපේ චැනල් එක තවම subscribe කරලා නැ ඒනිසා මම තරහයි😠 මාව පාවිච්චි කරන්න ඕන්නම් මෙ පහල බටන් එකෙන් අපේ චැනල් එකට ගිහින් Join වෙලා එන්න 🤗🙏....</code>"
    FREE_USER_LIMIT_Q_SZE = "Sorry Friend, Free users can only 1 request per {} minutes. Please try again after {} seconds later."
