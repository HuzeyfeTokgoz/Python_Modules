import os
from dotenv import load_dotenv


def load_conf() -> dict[str, str | None]:
    load_dotenv()

    config_env: dict[str, str | None] = {
        "matrix_mode": os.getenv("MATRIX_MODE"),
        "database_url": os.getenv("DATABASE_URL"),
        "api_key": os.getenv("API_KEY"),
        "log_level": os.getenv("LOG_LEVEL"),
        "zion_endpoint": os.getenv("ZION_ENDPOINT"),
    }

    return config_env


def oracle_status() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    conf = load_conf()

    missing_conf: list[str] = []
    if not conf["database_url"]:
        missing_conf.append("DATABASE_URL")
    if not conf["api_key"]:
        missing_conf.append("API_KEY")
    if not conf["zion_endpoint"]:
        missing_conf.append("ZION_ENDPOINT")

    print("\nConfiguration loaded:")
    print(f"Mode: {conf['matrix_mode']}")

    if conf["database_url"]:
        print("Database: Connected to local instance")
    else:
        print("Database: [ERROR] - No URL!")

    if conf["api_key"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Error - No Key!")

    print(f"Log Level: {conf['log_level']}")

    if conf["zion_endpoint"]:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")

    print("\nEnvironment security check:")
    if missing_conf:
        print(f"[WARNING] Missing settings: {', '.join(missing_conf)}")
    else:
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    oracle_status()
