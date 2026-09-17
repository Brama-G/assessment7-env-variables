"""
Reads Jenkins-injected environment variables and validates
the application's version/name metadata.
"""
import os
import sys

def check_app_info():
    app_name = os.environ.get("APP_NAME", "")
    app_version = os.environ.get("APP_VERSION", "")

    print(f"Detected APP_NAME    : {app_name}")
    print(f"Detected APP_VERSION : {app_version}")

    if not app_name:
        print("ERROR: APP_NAME is not set.")
        sys.exit(1)
    if not app_version:
        print("ERROR: APP_VERSION is not set.")
        sys.exit(1)

    # Basic semantic versioning check (X.Y.Z)
    parts = app_version.split(".")
    if len(parts) != 3 or not all(p.isdigit() for p in parts):
        print(f"ERROR: APP_VERSION '{app_version}' is not in X.Y.Z format.")
        sys.exit(1)

    print(f"{app_name} v{app_version} - version metadata is valid.")

if __name__ == "__main__":
    check_app_info()
