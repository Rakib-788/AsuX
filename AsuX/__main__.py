import importlib
import logging

from telegram import Update

from AsuX import rani
from AsuX.modules import ALL_MODULES


def main():
    rani.run_polling(
        timeout=15,
        drop_pending_updates=True,
        allowed_updates=Update.ALL_TYPES,
        stop_signals=None,
    )


FORMAT = "[ᴀsᴜx] %(message)s"

if __name__ == "__main__":
    logging.basicConfig(
        handlers=[logging.FileHandler("logs.txt"), logging.StreamHandler()],
        level=logging.INFO,
        format=FORMAT,
        datefmt="[%X]",
    )
    logging.getLogger("ptbcontrib.postgres_persistence.postgrespersistence").setLevel(
        logging.INFO
    )
    for module in ALL_MODULES:
        importlib.import_module("AsuX.modules." + module)
    main()
    print("ᴏ ғᴜ*ᴋ  ᴡʜᴇɴ ᴛᴜʀɴ ᴏɴ ᴍᴇ ᴀɢᴀɪɴ 🤔")
