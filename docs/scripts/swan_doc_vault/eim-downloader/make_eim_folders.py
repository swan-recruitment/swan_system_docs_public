import os
import re
from pathlib import Path

# >>> CHANGE THIS if needed
BASE_PATH = r"G:\Shared drives\Swan Accounts\PAYE\guides\New folder"

# (code, title)
ENTRIES = [
    ("EIM00010", "Data protection"),
    ("EIM00100", "About this manual"),
    ("EIM00500", "Employment income: contents"),
    ("EIM11200", "Incentive award schemes: contents"),
    ("EIM11300", "Accommodation provided by reason of employment: contents"),
    ("EIM11800", "PAYE special types of payment: contents"),
    ("EIM12800", "Termination payments and benefits: contents"),
    ("EIM15000", "Employer-financed and non-approved retirement benefits schemes: contents"),
    ("EIM15500", "Value Added Tax: inter-relation with earnings and expenses: contents"),
    ("EIM16000", "Vouchers and credit tokens: contents"),
    ("EIM20000", "The benefits code: benefits and expenses payments: contents"),
    ("EIM22700", "Van and van fuel benefit from 2005/06; heavy goods vehicles: contents"),
    ("EIM23000", "The benefits code: car and car fuel benefit: contents"),
    ("EIM26100", "The benefits code: beneficial loans: contents"),
    ("EIM30000", "The benefits code: scholarships provided for members of the family or household of a director or employee: contents"),
    ("EIM30050", "Dispensations: contents"),
    ("EIM30200", "Exemption for amounts which would otherwise be deductible: contents"),
    ("EIM30500", "Deductions: directors' and officers' liabilities: contents"),
    ("EIM31200", "Employees using own vehicles for work: mileage allowance payments, AMAPs, MAR, passenger payments: contents"),
    ("EIM31500", "Employee Car Ownership Schemes (ECOS): contents"),
    ("EIM31600", "Deductions from general earnings: contents"),
    ("EIM31800", "Deductions: travel expenses: general: contents"),
    ("EIM32400", "Deductions: expenses other than travel: contents"),
    ("EIM33000", "Seafarers’ Earnings Deduction: introduction: contents"),
    ("EIM34000", "Special rules for employees travelling to work outside the United Kingdom: contents"),
    ("EIM35000", "Travelling expenses: Non-resident and qualifying new resident employees working in the United Kingdom: contents"),
    ("EIM36500", "Deductions from earnings: capital allowances: introduction: arrangement of guidance: contents"),
    ("EIM40000", "The scope of the charge to tax on general earnings: contents"),
    ("EIM42200", "Employment income: basis of assessment for general earnings: arrangement of guidance: contents"),
    ("EIM42700", "Waivers of remuneration and salary sacrifice: contents"),
    ("EIM42800", "Residence and domicile: contents"),
    ("EIM43500", "Globally mobile employees: contents"),
    ("EIM44000", "Optional remuneration arrangements: Contents"),
    ("EIM45000", "Employment income provided through third parties: overview, general approach: contents"),
    ("EIM50000", "Tax treatment of particular occupations: contents A to Ce"),
    ("EIM60000", "Tax treatment of particular occupations: C to J"),
    ("EIM65799", "Tax treatment of particular occupations: L to R"),
    ("EIM70199", "Tax treatment of particular occupations: S to Z: contents"),
    ("EIM74000", "Assessments, appeals and other procedures"),
    ("EIM75000", "The taxation of pension income: contents"),
    ("EIM76000", "Social security benefits: contents"),
    ("EIM77000", "Appendices"),
]

# ---- Helpers (Windows-safe names) ----
INVALID = r'[<>:"/\\|?*\x00-\x1F]'  # invalid in Windows
TRAILING = r'[\. ]+$'               # no trailing dots/spaces on Windows

def slugify_title(title: str) -> str:
    # replace spaces with underscores, remove colons, keep hyphens
    t = title.replace(" ", "_").replace(":", "")
    t = re.sub(INVALID, "-", t)           # replace any invalid character
    t = re.sub(TRAILING, "", t)           # strip invalid trailing chars
    return t

def main():
    base = Path(BASE_PATH)
    base.mkdir(parents=True, exist_ok=True)

    for code, title in ENTRIES:
        folder = base / f"{code}-{slugify_title(title)}"
        folder.mkdir(exist_ok=True)

        # README.txt with nice human title on first line
        readme = folder / "README.txt"
        if not readme.exists():
            readme.write_text(
                f"{code} — {title}\n\nThis folder was auto-created for the EIM manual entry.",
                encoding="utf-8",
            )

        print(f"✓ {folder}")

if __name__ == "__main__":
    main()
