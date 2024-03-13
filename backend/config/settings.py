from environs import Env

env = Env()

POSTGRES_USER = env("POSTGRES_USER")
POSTGRES_PASSWORD = env("POSTGRES_PASSWORD")
TEST_POSTGRES_USER = env("TEST_POSTGRES_USER")
TEST_POSTGRES_PASSWORD = env("TEST_POSTGRES_PASSWORD")
