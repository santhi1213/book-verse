import os
import re

from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "postgresql://bookstore:bookstore@localhost:5432/bookstore"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "dev-jwt-secret-key")
    JWT_ACCESS_TOKEN_EXPIRES = int(os.environ.get("JWT_ACCESS_TOKEN_EXPIRES", 900))
    JWT_REFRESH_TOKEN_EXPIRES = int(os.environ.get("JWT_REFRESH_TOKEN_EXPIRES", 604800))
    CORS_ORIGINS = [
        origin.strip()
        for origin in os.environ.get(
            "CORS_ORIGINS",
            "http://localhost:5172,http://localhost:5173,http://localhost:5174",
        ).split(",")
        if origin.strip()
    ]
    # Origins matched by regex in addition to CORS_ORIGINS.
    CORS_ORIGIN_PATTERNS = []


class DevelopmentConfig(Config):
    DEBUG = True
    # Allow the portals to be opened from any device on the local network
    # (e.g. http://192.168.1.20:5174) without listing every IP in CORS_ORIGINS.
    CORS_ORIGIN_PATTERNS = [
        re.compile(
            r"^http://(localhost|127\.0\.0\.1|10\.\d{1,3}\.\d{1,3}\.\d{1,3}"
            r"|192\.168\.\d{1,3}\.\d{1,3}|172\.(1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3}):\d+$"
        )
    ]


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "TEST_DATABASE_URL",
        "postgresql://bookstore:bookstore@localhost:5432/bookstore_test",
    )


class ProductionConfig(Config):
    DEBUG = False


config_by_name = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
