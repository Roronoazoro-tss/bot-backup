class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7481211733"
    sudo_users = "1496149228", "2022832277", "6925950092", "8134602296", "5877629357", "7481211733", "7152534468"
    GROUP_ID = -1002337505439

    TOKEN = "6832094998:AAFr9ukEpdTJ--LyasNV95yD_5X-_wQRdU0"
    mongo_url = "mongodb+srv://naruto:hinatababy@cluster0.rqyiyzx.mongodb.net/"
    PARTNER = "7370569442", "6861852788", "7378476666"
    PHOTO_URL = ["https://files.catbox.moe/7vr2im.jpg", "https://files.catbox.moe/7vr2im.jpg"]
    SUPPORT_CHAT = "-1002337505439"
    UPDATE_CHAT = "-1002337505439"
    BOT_USERNAME = "Catch_your_harem_bot"
    CHARA_CHANNEL_ID = "-1002337505439"
    api_id = 22451491
    api_hash = "28e74942125f7e4968398ea651cd417b"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
