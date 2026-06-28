#!/usr/bin/env python3
"""
Student Record Management System
--------------------------------
A menu-driven application that demonstrates:
  - CSV / JSON file handling
  - Custom exceptions  &  try / except / finally
  - Logging user actions and errors
  - Input validation
  - CRUD operations (Add, View, Search, Update, Delete)
"""

import os
import csv
import json
import logging
import re
import sys
from datetime import datetime

logging.basicConfig(
    filename="student_system.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)

CSV_FILE = "students.csv"
JSON_FILE = "students.json"

class StudentNotFoundError(Exception):
    """Raised when a student registration number does not exist."""
    pass

class InvalidRegNoError(Exception):
    """Raised when a registration number format is invalid."""
    pass

class DuplicateStudentError(Exception):
    """Raised when trying to add a student with an existing reg_no."""
    pass

class ValidationError(Exception):
    """Raised when user input fails validation."""
    pass

def _ensure_files_exist():
    """Create empty CSV and JSON files if they don't exist."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["reg_no", "name", "email", "program"])
        log.info("Created students.csv with headers.")

    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, "w") as f:
            json.dump({}, f)
        log.info("Created students.json (empty).")


def _read_csv():
    """Return list of dicts from CSV.  Returns [] on error."""
    rows = []
    try:
        with open(CSV_FILE, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        log.warning("CSV file not found — returning empty list.")
    except Exception as e:
        log.error(f"Error reading CSV: {e}")
    return rows


def _write_csv(rows):
    """Overwrite CSV with the given list of dicts."""
    try:
        with open(CSV_FILE, "w", newline="") as f:
            if rows:
                writer = csv.DictWriter(f, fieldnames=rows[0].keys())
                writer.writeheader()
                writer.writerows(rows)
            else:
                writer = csv.writer(f)
                writer.writerow(["reg_no", "name", "email", "program"])
    except Exception as e:
        log.error(f"Error writing CSV: {e}")
        raise


def _read_json():
    """Return dict parsed from JSON file."""
    try:
        with open(JSON_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        log.warning("JSON file not found — returning empty dict.")
        return {}
    except json.JSONDecodeError as e:
        log.error(f"Invalid JSON file: {e}")
        return {}


def _write_json(data):
    """Write dict to JSON file."""
    try:
        with open(JSON_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        log.error(f"Error writing JSON: {e}")
        raise

REG_NO_PATTERN = re.compile(r"^\d{2}-\d{4}$")
EMAIL_PATTERN  = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
PHONE_PATTERN  = re.compile(r"^\+?\d{10,15}$")


def validate_reg_no(reg_no):
    """Raise InvalidRegNoError if format is wrong."""
    if not REG_NO_PATTERN.match(reg_no.strip()):
        raise InvalidRegNoError(
            "Registration number must be in format XX-XXXX (e.g. 23-1102)."
        )
    return reg_no.strip().upper()


def validate_email(email):
    """Raise ValidationError if email format is wrong."""
    if not EMAIL_PATTERN.match(email.strip()):
        raise ValidationError("Invalid email address format.")
    return email.strip()


def validate_phone(phone):
    """Raise ValidationError if phone format is wrong."""
    if phone.strip() and not PHONE_PATTERN.match(phone.strip()):
        raise ValidationError("Phone must be 10-15 digits, optionally starting with +.")
    return phone.strip()


def validate_required(value, field_name):
    """Raise ValidationError if value is empty."""
    if not value.strip():
        raise ValidationError(f"{field_name} cannot be empty.")
    return value.strip()


def add_student():
    """Add a new student record (CSV core + JSON details)."""
    print("\n--- Add New Student ---")
    try:
        reg_no = input("Registration No. (XX-XXXX): ").strip()
        reg_no = validate_reg_no(reg_no)

        existing = _read_csv()
        if any(r["reg_no"].upper() == reg_no.upper() for r in existing):
            raise DuplicateStudentError(
                f"Student '{reg_no}' already exists."
            )

        name    = validate_required(input("Full Name: "), "Name")
        email   = validate_email(input("Email: "))
        program = validate_required(input("Program: "), "Program")

        print("\n  -- Additional Details (saved to JSON) --")
        address  = input("Address: ").strip()
        phone    = validate_phone(input("Contact No.: "))
        guardian = input("Guardian Name: ").strip()
        g_phone  = validate_phone(input("Guardian Contact: "))
        notes    = input("Notes: ").strip()

        existing.append({
            "reg_no": reg_no,
            "name": name,
            "email": email,
            "program": program,
        })
        _write_csv(existing)

        json_data = _read_json()
        json_data[reg_no] = {
            "address": address,
            "contact_no": phone,
            "guardian_name": guardian,
            "guardian_contact": g_phone,
            "notes": notes,
        }
        _write_json(json_data)

        log.info(f"ADDED student '{reg_no}' — {name}")
        print(f"✔ Student '{reg_no}' added successfully.")

    except (InvalidRegNoError, ValidationError, DuplicateStudentError) as e:
        print(f"✘ {e}")
        log.warning(f"ADD rejected — {e}")
    except Exception as e:
        print(f"✘ Unexpected error: {e}")
        log.error(f"ADD student failed: {e}")
    finally:
        input("\nPress Enter to continue...")


def view_all_students():
    """Display every student record with JSON details merged."""
    print("\n--- All Students ---")
    try:
        rows = _read_csv()
        if not rows:
            print("  (No student records found.)")
            log.info("VIEW ALL — no records.")
            return

        json_data = _read_json()
        for r in rows:
            reg = r["reg_no"]
            extra = json_data.get(reg, {})
            print(f"\n  [{reg}] {r['name']}")
            print(f"       Program : {r['program']}")
            print(f"       Email   : {r['email']}")
            if extra.get("contact_no"):
                print(f"       Phone   : {extra['contact_no']}")
            if extra.get("address"):
                print(f"       Address : {extra['address']}")
            if extra.get("guardian_name"):
                print(f"       Guardian: {extra['guardian_name']} ({extra.get('guardian_contact', 'N/A')})")
            if extra.get("notes"):
                print(f"       Notes   : {extra['notes']}")
            print("       " + "-" * 35)

        log.info(f"VIEW ALL — displayed {len(rows)} student(s).")
    except Exception as e:
        print(f"✘ Error displaying records: {e}")
        log.error(f"VIEW ALL failed: {e}")
    finally:
        input("\nPress Enter to continue...")


def search_student():
    """Search for a student by registration number."""
    print("\n--- Search Student ---")
    try:
        reg_no = validate_reg_no(input("Enter Registration No.: "))

        rows = _read_csv()
        match = None
        for r in rows:
            if r["reg_no"].upper() == reg_no.upper():
                match = r
                break

        if not match:
            raise StudentNotFoundError(f"No student found with reg_no '{reg_no}'.")

        json_data = _read_json()
        extra = json_data.get(match["reg_no"], {})

        print(f"\n  [{match['reg_no']}] {match['name']}")
        print(f"       Program : {match['program']}")
        print(f"       Email   : {match['email']}")
        if extra.get("contact_no"):
            print(f"       Phone   : {extra['contact_no']}")
        if extra.get("address"):
            print(f"       Address : {extra['address']}")
        if extra.get("guardian_name"):
            print(f"       Guardian: {extra['guardian_name']} ({extra.get('guardian_contact', 'N/A')})")
        if extra.get("notes"):
            print(f"       Notes   : {extra['notes']}")

        log.info(f"SEARCH — found '{reg_no}'.")
    except (InvalidRegNoError, StudentNotFoundError) as e:
        print(f"✘ {e}")
        log.warning(f"SEARCH — {e}")
    except Exception as e:
        print(f"✘ Unexpected error: {e}")
        log.error(f"SEARCH failed: {e}")
    finally:
        input("\nPress Enter to continue...")


def update_student():
    """Update core (CSV) and/or additional (JSON) fields for a student."""
    print("\n--- Update Student ---")
    try:
        reg_no = validate_reg_no(input("Enter Registration No. of student to update: "))

        rows = _read_csv()
        idx = None
        for i, r in enumerate(rows):
            if r["reg_no"].upper() == reg_no.upper():
                idx = i
                break

        if idx is None:
            raise StudentNotFoundError(f"No student found with reg_no '{reg_no}'.")

        student = rows[idx]
        print(f"\n  Updating: [{student['reg_no']}] {student['name']}")
        print("  (Press Enter to keep current value.)")

        name = input(f"  Name    [{student['name']}]: ").strip()
        if name:
            student["name"] = validate_required(name, "Name")

        email = input(f"  Email   [{student['email']}]: ").strip()
        if email:
            student["email"] = validate_email(email)

        program = input(f"  Program [{student['program']}]: ").strip()
        if program:
            student["program"] = validate_required(program, "Program")

        rows[idx] = student
        _write_csv(rows)

        json_data = _read_json()
        extra = json_data.get(reg_no, {})

        print("\n  -- Additional Details (press Enter to keep) --")
        addr = input(f"  Address [{extra.get('address', '')}]: ").strip()
        if addr:
            extra["address"] = addr

        phone = input(f"  Contact [{extra.get('contact_no', '')}]: ").strip()
        if phone:
            extra["contact_no"] = validate_phone(phone)

        guardian = input(f"  Guardian [{extra.get('guardian_name', '')}]: ").strip()
        if guardian:
            extra["guardian_name"] = guardian

        g_phone = input(f"  G. Contact [{extra.get('guardian_contact', '')}]: ").strip()
        if g_phone:
            extra["guardian_contact"] = validate_phone(g_phone)

        notes = input(f"  Notes [{extra.get('notes', '')}]: ").strip()
        if notes:
            extra["notes"] = notes

        json_data[reg_no] = extra
        _write_json(json_data)

        log.info(f"UPDATED student '{reg_no}'.")
        print(f"✔ Student '{reg_no}' updated successfully.")

    except (InvalidRegNoError, StudentNotFoundError, ValidationError) as e:
        print(f"✘ {e}")
        log.warning(f"UPDATE rejected — {e}")
    except Exception as e:
        print(f"✘ Unexpected error: {e}")
        log.error(f"UPDATE failed: {e}")
    finally:
        input("\nPress Enter to continue...")


def delete_student():
    """Remove a student from both CSV and JSON."""
    print("\n--- Delete Student ---")
    try:
        reg_no = validate_reg_no(input("Enter Registration No. of student to delete: "))

        rows = _read_csv()
        new_rows = [r for r in rows if r["reg_no"].upper() != reg_no.upper()]

        if len(new_rows) == len(rows):
            raise StudentNotFoundError(f"No student found with reg_no '{reg_no}'.")

        print(f"\n  You are about to delete: [{reg_no}] "
              f"{next(r['name'] for r in rows if r['reg_no'].upper() == reg_no.upper())}")
        confirm = input("  Type 'YES' to confirm: ").strip()
        if confirm != "YES":
            print("  Deletion cancelled.")
            log.info(f"DELETE cancelled for '{reg_no}'.")
            return

        _write_csv(new_rows)

        json_data = _read_json()
        json_data.pop(reg_no, None)
        _write_json(json_data)

        log.info(f"DELETED student '{reg_no}'.")
        print(f"✔ Student '{reg_no}' deleted permanently.")

    except (InvalidRegNoError, StudentNotFoundError) as e:
        print(f"✘ {e}")
        log.warning(f"DELETE rejected — {e}")
    except Exception as e:
        print(f"✘ Unexpected error: {e}")
        log.error(f"DELETE failed: {e}")
    finally:
        input("\nPress Enter to continue...")


def generate_summary():
    """Print a quick stats summary to screen and log."""
    print("\n--- System Summary ---")
    try:
        rows = _read_csv()
        json_data = _read_json()

        print(f"  CSV records       : {len(rows)}")
        print(f"  JSON entries      : {len(json_data)}")
        print(f"  Fully matched     : {sum(1 for r in rows if r['reg_no'] in json_data)}")
        print(f"  CSV-only orphans  : {len(rows) - sum(1 for r in rows if r['reg_no'] in json_data)}")
        log.info(f"SUMMARY — {len(rows)} CSV, {len(json_data)} JSON entries.")
    except Exception as e:
        print(f"✘ Error generating summary: {e}")
        log.error(f"SUMMARY failed: {e}")
    finally:
        input("\nPress Enter to continue...")

def menu():
    """Display the main menu and dispatch user choices."""
    _ensure_files_exist()

    while True:
        print("\n" + "=" * 50)
        print("     STUDENT RECORD MANAGEMENT SYSTEM")
        print("=" * 50)
        print("  1.  Add a new student")
        print("  2.  View all students")
        print("  3.  Search student by Reg. No.")
        print("  4.  Update student details")
        print("  5.  Delete a student record")
        print("  6.  System summary")
        print("  7.  Exit")
        print("=" * 50)

        try:
            choice = input("  Enter your choice (1-7): ").strip()
            if choice == "1":
                add_student()
            elif choice == "2":
                view_all_students()
            elif choice == "3":
                search_student()
            elif choice == "4":
                update_student()
            elif choice == "5":
                delete_student()
            elif choice == "6":
                generate_summary()
            elif choice == "7":
                print("\n  Goodbye!")
                log.info("System exited by user.")
                break
            else:
                print("  Invalid choice. Please enter 1-7.")
        except KeyboardInterrupt:
            print("\n\n  Interrupted. Exiting.")
            log.warning("System interrupted by user (Ctrl+C).")
            break
        except Exception as e:
            print(f"\n  Unexpected error: {e}")
            log.error(f"Menu loop error: {e}")


if __name__ == "__main__":
    menu()
