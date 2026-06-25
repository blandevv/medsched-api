from src.core.config import Settings


def test_database_url_is_built_correctly() -> None:
    settings = Settings(
        secret_key="secret",
        db_host="localhost",
        db_port=5432,
        db_name="test_db",
        db_user="test_user",
        db_password="test_password",
        jwt_secret_key="jwt_secret_key",
    )

    assert (
        settings.database_url
        == "postgresql+asyncpg://test_user:test_password@localhost:5432/test_db"
    )
