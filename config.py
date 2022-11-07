from dataclasses import dataclass
from environs import Env

env = Env()
env.read_env()


@dataclass
class Config:
    token = env.str('BOT_TOKEN')
    payment_token = env.str('PAYMENT_TOKEN')
    admin_ids = list[map[int, env.list('ADMINS')]]


@dataclass
class DBConfig:
    db_password = env.str('DB_PASSWORD')
    db_user = env.str('DB_USER')
    db_name = env.str('DB_NAME')
