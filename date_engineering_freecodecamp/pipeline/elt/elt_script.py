import subprocess
import sys
import time
import os

def wait_for_postgres(host, max_retries=5, delay_seconds=5):
    """Wait for PostgreSQL to accept connections using pg_isready."""
    for attempt in range(1, max_retries + 1):
        result = subprocess.run(
            ["pg_isready", "-h", host],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            print(f"✅ PostgreSQL at {host} is ready.")
            return True
        else:
            print(f"⏳ Waiting for {host} (attempt {attempt}/{max_retries})")
            if attempt < max_retries:
                time.sleep(delay_seconds)
    print(f"❌ Max retries reached. PostgreSQL at {host} is not available.")
    return False

# --- Read configuration from environment variables ---
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "secret")

SOURCE_HOST = os.getenv("SOURCE_HOST", "source_postgres")
SOURCE_DB = os.getenv("SOURCE_DB", "source_db")

DESTINATION_HOST = os.getenv("DESTINATION_HOST", "destination_postgres")
DESTINATION_DB = os.getenv("DESTINATION_DB", "destination_db")

if not wait_for_postgres(SOURCE_HOST):
    sys.exit(1)

if not wait_for_postgres(DESTINATION_HOST):
    sys.exit(1)

print("🚀 Starting ELT Script...")

source_config = {
    'dbname': SOURCE_DB,
    'user': POSTGRES_USER,
    'password': POSTGRES_PASSWORD,
    'host': SOURCE_HOST
}

destination_config = {
    'dbname': DESTINATION_DB,
    'user': POSTGRES_USER,
    'password': POSTGRES_PASSWORD,
    'host': DESTINATION_HOST
}

# 1. Dump from source
dump_command = [
    'pg_dump',
    '-h', source_config['host'],
    '-U', source_config['user'],
    '-d', source_config['dbname'],
    '-f', 'data_dump.sql',
    '-w'
]

dump_env = os.environ.copy()
dump_env['PGPASSWORD'] = source_config['password']

print("📤 Dumping source database...")
subprocess.run(dump_command, env=dump_env, check=True)
print("✅ Dump completed.")

# 2. Load into destination
load_command = [
    'psql',
    '-h', destination_config['host'],
    '-U', destination_config['user'],
    '-d', destination_config['dbname'],
    '-f', 'data_dump.sql',
    '-a'  # optional
]

load_env = os.environ.copy()
load_env['PGPASSWORD'] = destination_config['password']

print("📥 Loading into destination database...")
subprocess.run(load_command, env=load_env, check=True)
print("✅ Load completed.")

print("🏁 Ending ELT Script...")