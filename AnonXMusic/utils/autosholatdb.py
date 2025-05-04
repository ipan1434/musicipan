from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI


autosholat_collection = db['autosholat_chats']

async def add_autosholat(chat_id: int):
    """
    Menambahkan chat_id ke dalam koleksi autosholat_chats untuk mendapatkan notifikasi.
    """
    # Menambahkan chat_id ke database jika belum ada
    await autosholat_collection.update_one(
        {"chat_id": chat_id},
        {"$set": {"chat_id": chat_id}},
        upsert=True
    )

async def remove_autosholat(chat_id: int):
    """
    Menghapus chat_id dari koleksi autosholat_chats untuk menghentikan notifikasi.
    """
    await autosholat_collection.delete_one({"chat_id": chat_id})

async def get_autosholat_chats():
    """
    Mengambil semua chat_id yang terdaftar untuk notifikasi autosholat.
    """
    return await autosholat_collection.find().to_list(None)
