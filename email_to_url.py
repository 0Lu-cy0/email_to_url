#!/usr/bin/env python3
"""Convert an email address to: email | Generator.email URL."""
import subprocess
import sys
from urllib.parse import quote

PREFIX = "https://generator.email"
OUTPUT_FILE = "emails_output.txt"  # Tên file text để lưu kết quả


def convert(email: str) -> str:
    email = email.strip()
    if email.lower().startswith("mailto:"):
        email = email[7:]
    if email.count("@") != 1:
        raise ValueError("Email phai co dang tenhopthu@tenmien.com")
    local, domain = email.rsplit("@", 1)
    if not local or not domain or "." not in domain or " " in email:
        raise ValueError("Dia chi email chua hop le. Vi du: joldinroman@svvdfeghdb.help")
    url = f"{PREFIX}/{quote(domain, safe='.-')}/{quote(local, safe='._+-')}"
    return f"{email} | {url}"


def copy_to_clipboard(text: str) -> bool:
    if sys.platform != "win32":
        return False
    try:
        subprocess.run("clip", input=text, text=True, check=True, shell=True)
        return True
    except Exception:
        return False


def save_to_file(text: str, filename: str = OUTPUT_FILE) -> bool:
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(text + "\n")
        return True
    except Exception as exc:
        print(f"Loi khi ghi file: {exc}")
        return False


def main():
    print("=" * 58)
    print("  Email -> Generator.email URL")
    print(f"  Ket qua duoc luu tai: {OUTPUT_FILE}")
    print("  Output: email | url")
    print("  Nhap q de thoat.")
    print("=" * 58)
    while True:
        try:
            email = input("\nEmail: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nTam biet!")
            break
        if email.lower() in {"q", "quit", "exit"}:
            print("Tam biet!")
            break
        if not email:
            continue
        try:
            result = convert(email)
            print("\n" + result)

            # Ghi ket qua vao file text
            if save_to_file(result):
                print(f"(Da luu vao {OUTPUT_FILE})")

            # Copy ket qua vao clipboard
            if copy_to_clipboard(result):
                print("(Da copy dong ket qua vao clipboard.)")
        except ValueError as exc:
            print(f"Loi: {exc}")


if __name__ == "__main__":
    main()