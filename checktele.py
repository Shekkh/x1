# by: t.me/lllllj

import random
import requests

import telethon
from telethon.sync import functions
from user_agent import generate_user_agent
from help import *
import requests
from user_agent import *
from help import *
from config import *
from threading import Thread
import threading
import asyncio
from telethon import events

a = 'qwrtyuiopassdfghklzxcvbnm'
b = '123456789'
e = 'qwrtyuiopassdfghjklzxcvbnm123456789'

banned = []
with open("banned.txt", "r") as f:
    f = f.read().split()
    banned.append(f)
trys, trys2 = [0], [0]
isclaim = ["off"]
isauto = ["off"]


def check_user(username):
    url = "https://t.me/" + str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    response = requests.get(url, headers=headers)
    if (
        response.text.find(
            'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"'
        )
        >= 0
    ):
        return True
    else:
        return False


def gen_user(choice):
    if choice == "ثلاثي":
        c = random.choices(a)
        d = random.choices(a)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(e)
            s = random.choices(e)
            f = [c[0], "_", d[0], "_", s[0]]
            username = ''.join(f)
        else:
            pass
    elif choice == "مكرر":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(e) for i in range(1))))
        f1 = c+"_"+d+"_"+d
        f2 = c+"_"+d+"_"+c
        f3 = c+"_"+c+"_"+d
        f = f1,f2,f3
        f = random.choice(f)
        username = f
        
        elif choice == "رباعي":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(e) for i in range(1))))
        f1 = c+"_"+d+d+d
        f2 = c+"_"+d+c+c
        f3 = c+"_"+c+d+c
        f4 = c+"_"+c+c+d
        f = f1,f2,f3,f4
        f = random.choice(f)
        username = f
        
        elif choice == "رباعي2":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(e) for i in range(1))))
        f1 = c+d+"_"+d+d
        f2 = c+d+"_"+c+c
        f3 = c+c+"_"+d+c
        f4 = c+c+"_"+c+d
        f = f1,f2,f3,f4
        f = random.choice(f)
        username = f
        
        elif choice == "رباعي3":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(e) for i in range(1))))
        f1 = c+d+d+"_"+d
        f2 = c+d+c+"_"+c
        f3 = c+c+d+"_"+c
        f4 = c+c+c+"_"+d
        f = f1,f2,f3,f4
        f = random.choice(f)
        username = f
        
    elif choice == "رباعي4":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(e) for i in range(1))))
        f1 = c+c+"_"+d+d
        f2 = c+d+"_"+d+c
        f3 = c+d+"_"+c+d
        f = f1,f2,f3
        f = random.choice(f)
        username = f
        
    elif choice == "رباعي5":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(e) for i in range(1))))
        f1 = c+"_"+c+d+d
        f2 = c+"_"+d+d+c
        f3 = c+"_"+d+c+d
        f = f1,f2,f3
        f = random.choice(f)
        username = f

    elif choice == "رباعي6":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(e) for i in range(1))))
        f1 = c+c+d+"_"+d
        f2 = c+d+c+"_"+d
        f3 = c+d+d+"_"+c
        f = f1,f2,f3
        f = random.choice(f)
        username = f

    elif choice == "سداسيات":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(e) for i in range(1))))
        f1 = c+c+c+d+d+d
        f2 = c+c+d+d+d+c
        f3 = c+d+d+d+c+c
        f4 = c+d+c+d+c+d
        f = f1,f2,f3,f4
        f = random.choice(f)
        username = f

    elif choice == "سداسيات2":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(e) for i in range(1))))
        f1 = c+d+c+d+d+c
        f2 = c+d+d+c+c+d
        f3 = c+c+d+d+c+d
        f4 = c+d+c+c+d+d
        f5 = c+c+d+c+d+d
        f = f1,f2,f3,f4,f5
        f = random.choice(f)
        username = f
        
        elif choice == "سداسي":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(e) for i in range(1))))
        f1 = c+c+d+d+d+d
        f2 = c+d+d+d+d+c
        f3 = c+d+c+c+d+d
        f4 = c+c+c+c+d+d
        f = f1,f2,f3,f4
        f = random.choice(f)
        username = f
        
    elif choice == "سداسي2":
        c = str(''.join((random.choice(a) for i in range(1))))
        d = str(''.join((random.choice(e) for i in range(1))))
        f1 = c+d+c+d+d+d
        f2 = c+d+d+c+d+d
        f3 = c+d+c+c+d+c
        f4 = c+c+d+c+d+c
        f5 = c+d+c+c+c+d
        f6 = c+d+d+c+c+c
        f7 = c+c+c+d+d+c
        f = f1,f2,f3,f4,f5,f6,f7
        f = random.choice(f)
        username = f
        
    elif choice == "تيست":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], s[0], "_", c[0], s[0], d[0]]
        username = ''.join(f)
        username = username+'bot'
    else:
        return "error"
    return username


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.الصيد"))
async def _(event):
    await event.edit(
        '''
**-- -- -- -- -- -- -- -- --
 الانواع :
 -- -- -- -- - 
 ثلاثي - s_x_n [ ثلاثي عشوائي ]
 مكرر -   s_x_s [ ثلاثي مكرر ]
 رباعي - s_777 [ رباعي شخطه بدايه ]
 رباعي2 - sx_ss [ رباعي شخطه وسط ]
 رباعي3 - sss_o [ رباعي شخطه خير ]
 رباعي4 - ss_xx [ رباعي شخطه نص ]
 رباعي5 - x_xcc [ رباعي شخطه ابديه ]
 رباعي6 - xxc_c [ رباعي شخطه خير ]
 سداسيات - sssooo [ سداسيات 3 حروف مرتب ]
 سداسيات2 - sxxssx [ سداسي 3 حروف عشوائي ]
 سداسي - ssxxxx [ سداسي حرفين مرتب ]
 تيست - [ تجربه السورس شغال ]
   -- -- -- -- -- 
   طريقه الصيد هيه كالتالي
 - .صيد + نوع الصيد تكتب الاسم 
هوه ينشأ قناة تلقائي ويفحص بيها
 -- -- -- -- -- -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- -- -- -- -- 
مثال: .صيد ثلاثي
 ---------------------------------------------------------------------- — — — —
 الامر:  `.صيد` + النوع
 - يقوم بصيد معرفات عشوائية حسب النوع

 ٴ— — — — — — — — — —
 الامر:   `.حالة الصيد`
 • لمعرفة عدد المحاولات للصيد

@lllllj **

'''
    )

@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.الانواع"))
async def _(event):
    if ispay2[0] == "yes":
        await event.edit(tele_checker2)
    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")

@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.صيد"))
async def hunterusername(event):
    msg = event.text.split()
    choice = str(msg[1])
    try:
        ch = str(msg[2])
        if "@" in ch:
            ch = ch.replace("@", "")
        await event.edit(f"حسناً سيتم بدء الصيد في @{ch} .")
    except:
        try:
            ch = await eighthon(
                functions.channels.CreateChannelRequest(
                    title="صيد معرفات - Hunting IDs",
                    about="تم الصيد المعرف - ID caught",
                )
            )
            ch = ch.updates[1].channel_id
            await event.edit(f"**تم انشاء القناة بنجاح .. سيتم صيد نوع {choice} !**")
        except Exception as e:
            await eighthon.send_message(
                event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**"
            )
    isclaim.clear()
    isclaim.append("on")
    for i in range(19000000):
        username = gen_user(choice)
        if username == "error":
            await event.edit("** يرجى وضع النوع بشكل صحيح**.")
            break
        isav = check_user(username)
        if isav == True:
            try:
                await eighthon(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_message(
                    event.chat_id,
                    f"⌯ تم الصيد اليوزر @{username}",
                )
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                pass
            except Exception as baned:
                if "(caused by UpdateUsernameRequest)" in str(baned):
                    pass
            except telethon.errors.FloodError as e:
                await eighthon.send_message(
                    event.chat_id,
                    f"للاسف تبندت , مدة الباند**-  ({e.seconds}) ثانية .**",
                    event.chat_id,
                    f"للاسف تبندت , مدة الباند**-  ({e.seconds}) ثانية .**",
                )
                break
            except Exception as eee:
                if "the username is already" in str(eee):
                    pass
                else:
                    await eighthon.send_message(
                        event.chat_id,
                        f"""- خطأ مع @{username} , الخطأ :{str(eee)}""",
                    )
                    break
        else:
            pass
        trys[0] += 1
    isclaim.clear()
    isclaim.append("off")
    await event.client.send_message(event.chat_id, "انتهاء الفحص تم صيد معرف #x5")


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.تثبيت"))
async def _(event):
    msg = event.text.split()
    try:
        ch = str(msg[2])
        await event.edit(f"حسناً سيتم بدء التثبيت في**-  @{ch} .**")
    except:
        try:
            ch = await eighthon(
                functions.channels.CreateChannelRequest(
                    title="صيد يوزرات @lllllj ",
                    about="تم الصيد يم @lllllj",
                )
            )
            ch = ch.updates[1].channel_id
            await event.edit(f"**- تم بنجاح بدأ التثبيت**")
        except Exception as e:
            await eighthon.send_message(
                event.chat_id, f"خطأ في انشاء القناة , الخطأ : {str(e)}"
            )
    isauto.clear()
    isauto.append("on")
    username = str(msg[1])

    for i in range(1000000000000):
        isav = check_user(username)
        if isav == True:
            try:
                await eighthon(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_message(
                    event.chat_id,
                    f"- Done : @{username} !\n-  !\n- Hunting Log {trys2[0]}",
                )
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(
                    event.chat_id, f"المعرف **-  @{username} غير صالح . **"
                )
                break
            except telethon.errors.FloodError as e:
                await eighthon.send_message(
                    event.chat_id, f"للاسف تبندت , مدة الباند ({e.seconds}) ثانية ."
                )
                break
            except Exception as eee:
                await eighthon.send_message(
                    event.chat_id,
                    f"""خطأ مع {username} , الخطأ :{str(eee)}""",
                )
                break
        else:
            pass
        trys2[0] += 1

        await asyncio.sleep(1.3)
    isclaim.clear()
    isclaim.append("off")
    await eighthon.send_message(event.chat_id, "**- تم الانتهاء من التثبيت بنجاح**")


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.حالة الصيد"))
async def _(event):
    if "on" in isclaim:
        await event.edit(f"** الصيد وصل لـ({trys[0]}) من المحاولات**")
    elif "off" in isclaim:
        await event.edit("** الصيد  لا يعمل .**")
    else:
        await event.edit("- لقد حدث خطأ ما وتوقف الامر لديك")


@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.حالة التثبيت"))
async def _(event):
    if "on" in isauto:
        await event.edit(f"**- التثبيت وصل لـ({trys2[0]}) من المحاولات**")
    elif "off" in isauto:
        await event.edit("**- التثبيت بالاصل لا يعمل .**")
    else:
        await event.edit("-لقد حدث خطأ ما وتوقف الامر لديك")
@eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.ت (.*)"))
async def _(event):
    if ispay2[0] == "yes":
        trys = 0
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        if msg[0] == "تلقائي":  # تثبيت تلقائي عدد يوزر قناة
            isauto.clear()
            isauto.append("on")
            msg = ("".join(event.text.split(maxsplit=2)[2:])).split(" ", 2)
            username = str(msg[2])
            ch = str(msg[1])
            await event.edit(f"حسناً سأحاول تثبيت `{username}` على `{ch}` , بعدد `{msg[0]}` من المحاولات !")

            @eighthon.on(events.NewMessage(outgoing=True, pattern=r"\.حالة ت "))
            async def _(event):
                if "on" in isauto:
                    msg = await event.edit(f"التثبيت وصل لـ({trys}) من المحاولات")
                elif "off" in isauto:
                    await event.edit("لايوجد تثبيت شغال !")
                else:
                    await event.edit("خطأ")
            for i in range(int(msg[0])):
                if ispay2[0] == 'no':
                    break
                t = Thread(target=lambda q, arg1: q.put(
                    check_user(arg1)), args=(que, username))
                t.start()
                t.join()
                isav = que.get()
                if "Available" in isav:
                    try:
                        await eighthon(functions.channels.UpdateUsernameRequest(
                            channel=ch, username=username))
                        await event.client.send_message(event.chat_id, f'''** 
𝙷𝚄𝙽𝚃𝙸𝙽𝙶 (@{username})
× ᴄʟɪᴄᴋs ↬  {trys}
lD: @Max985 / @P8_PP × @HFFHH **
    ''')
                        break
                    except telethon.errors.rpcerrorlist.UsernameInvalidError:
                        await event.client.send_message(event.chat_id, f"مبند `{username}` ❌❌")
                        break
                    except Exception as eee:

                        await eighthon.send_message(event.chat_id, f'''خطأ مع {username}
    الخطأ :
    {str(eee)}''')
                        if "A wait of" in str(eee):
                            break
                else:
                    pass
                trys += 1

                await asyncio.sleep(0.1)
            trys = ""
            isclaim.clear()
            isclaim.append("off")
            await eighthon.send_message(event.chat_id, "تم الانتهاء من التثبيت التلقائي")
        if msg[0] == "يدوي":  # تثبيت يدوي يوزر قناة
            await event.edit(f"حسناً سأحاول تثبيت `{username}` على `{ch}` !")
            msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
            username = str(msg[0])
            ch = str(msg[1])
            try:
                await eighthon(functions.channels.UpdateUsernameRequest(
                    channel=ch, username=username))
                await event.client.send_message(event.chat_id, f'''**
𝙷𝚄𝙽𝚃𝙸𝙽𝙶 (@{username})
× ᴄʟɪᴄᴋs ↬  {trys}
-- -- -- -- -- -- -- -- -- -- -- -- -- **
    ''')
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(event.chat_id, f"مبند `{username}` ❌❌")
            except Exception as eee:
                await eighthon.send_message(event.chat_id, f'''خطأ مع {username}
    الخطأ :
    {str(eee)}''')

Threads=[] 
for t in range(100):
    x = threading.Thread(target=_)
    le = threading.Thread(target=gen_user)
    x.start()
    le.start()
    Threads.append(x)
    Threads.append(le)
for Th in Threads:
    Th.join()
