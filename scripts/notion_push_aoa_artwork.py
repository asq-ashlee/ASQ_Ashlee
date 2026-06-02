import csv
import json
import os
import re
import sys
from urllib import request, parse

NOTION_TOKEN = os.environ.get("NOTION_TOKEN")
NOTION_VERSION = "2022-06-28"

if not NOTION_TOKEN:
    print("ERROR: NOTION_TOKEN environment variable is not set.")
    sys.exit(1)

HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": NOTION_VERSION,
    "Content-Type": "application/json",
}

API_BASE = "https://api.notion.com/v1"


def notion_request(method, path, body=None):
    url = API_BASE + path
    data = None
    if body is not None:
        data = json.dumps(body).encode("utf-8")
    req = request.Request(url, data=data, method=method, headers=HEADERS)
    try:
        with request.urlopen(req) as resp:
            return json.load(resp)
    except Exception as exc:
        print(f"Notion request failed: {exc}")
        if hasattr(exc, 'read'):
            try:
                print(exc.read().decode('utf-8'))
            except Exception:
                pass
        raise


def search_database(query):
    body = {
        "query": query,
        "filter": {"value": "database", "property": "object"},
    }
    return notion_request("POST", "/search", body)


def create_page(db_id, properties, children=None):
    body = {
        "parent": {"database_id": db_id},
        "properties": properties,
    }
    if children is not None:
        body["children"] = children
    return notion_request("POST", "/pages", body)


def read_artwork_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]


def normalize_tags(value):
    if not value:
        return []
    return [tag.strip() for tag in re.split(r"[;,]", value) if tag.strip()]


def slugify(value):
    if not value:
        return ""
    slug = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE).strip().lower()
    slug = re.sub(r"[-\s]+", "-", slug)
    return slug


def build_artwork_properties(row):
    props = {}
    if row.get("Title"):
        props["Title"] = {"title": [{"text": {"content": row["Title"]}}]}
    props["artwork_id"] = {"rich_text": [{"text": {"content": row["artwork_id"]}}]}
    slug_value = row.get("Slug") or row.get("slug") or slugify(row.get("Title"))
    if slug_value:
        props["Slug"] = {"rich_text": [{"text": {"content": slug_value}}]}
    alt_text = row.get("Alt Text") or row.get("Alt_Text")
    if alt_text:
        props["Alt Text"] = {"rich_text": [{"text": {"content": alt_text}}]}
    if row.get("Status"):
        props["Status (optional later: Sold Date, Sold Via, Collector Notes)"] = {"select": {"name": row["Status"]}}
    if row.get("Category"):
        props["Category"] = {"select": {"name": row["Category"]}}
    if row.get("Orientation"):
        props["Orientation"] = {"select": {"name": row["Orientation"]}}
    if row.get("Size"):
        props["Dimensions"] = {"rich_text": [{"text": {"content": row["Size"]}}]}
    if row.get("Medium"):
        props["Medium"] = {"multi_select": [{"name": row["Medium"]}]}
    if row.get("Source"):
        props["Source"] = {"rich_text": [{"text": {"content": row["Source"]}}]}
    if row.get("Original_Available"):
        props["Original Available"] = {"checkbox": row["Original_Available"].lower() in ["yes", "true", "1"]}
    if row.get("Base_Price"):
        try:
            props["Price (Original)"] = {"number": float(row["Base_Price"])}
        except ValueError:
            pass
    if row.get("Date_Created"):
        date_value = row["Date_Created"].strip()
        if date_value:
            props["Date Created"] = {"date": {"start": date_value}}
    if row.get("Tags"):
        props["Tags"] = {"multi_select": [{"name": tag} for tag in normalize_tags(row["Tags"])]}
    if row.get("Mood"):
        props["Mood"] = {"multi_select": [{"name": tag.strip()} for tag in normalize_tags(row["Mood"])]}
    if row.get("Colors"):
        props["Colors"] = {"multi_select": [{"name": tag.strip()} for tag in normalize_tags(row["Colors"])]}
    if row.get("Image"):
        props["Master File Location"] = {"files": [{"name": os.path.basename(row["Image"]), "type": "external", "external": {"url": row["Image"]}}]}
    if row.get("Primary_Use"):
        props["Primary Use"] = {"select": {"name": row["Primary_Use"]}}
    if row.get("Description"):
        props["Description"] = {"rich_text": [{"text": {"content": row["Description"]}}]}
    if row.get("Story"):
        props["Story"] = {"rich_text": [{"text": {"content": row["Story"]}}]}
    if row.get("Subject"):
        props["Subject"] = {"rich_text": [{"text": {"content": row["Subject"]}}]}
    if row.get("Location"):
        props["Location"] = {"rich_text": [{"text": {"content": row["Location"]}}]}
    if row.get("Time_of_Day"):
        props["Time of Day"] = {"select": {"name": row["Time_of_Day"]}}
    if row.get("Light_Description"):
        props["Light Description"] = {"rich_text": [{"text": {"content": row["Light_Description"]}}]}
    if row.get("Workflow_Status"):
        props["Workflow Status"] = {"select": {"name": row["Workflow_Status"]}}
    return props


def build_product_properties(row, artwork_page_id=None):
    props = {}
    note_parts = []
    if row.get("product_id"):
        note_parts.append(row["product_id"])
    if row.get("notes"):
        note_parts.append(row["notes"])
    if note_parts:
        props["Notes"] = {"rich_text": [{"text": {"content": " | ".join(note_parts)}}]}
    if row.get("product_type"):
        props["Product Type"] = {"select": {"name": row["product_type"]}}
    if row.get("finish"):
        props["Finish"] = {"select": {"name": row["finish"]}}
    if row.get("size_inches"):
        props["Size"] = {"rich_text": [{"text": {"content": row["size_inches"]}}]}
    if row.get("frame_color"):
        props["Frame Color"] = {"select": {"name": row["frame_color"]}}
    if row.get("fulfillment"):
        props["Fulfillment Method"] = {"select": {"name": row["fulfillment"]}}
    if row.get("recommended_retail_price"):
        try:
            props["Price"] = {"number": float(row["recommended_retail_price"])}
        except ValueError:
            pass
    if row.get("status"):
        props["Workflow Status"] = {"select": {"name": row["status"]}}
    if artwork_page_id:
        props["Source Artwork"] = {"relation": [{"id": artwork_page_id}]}
    if row.get("product_type") and row.get("finish") and row.get("size_inches"):
        props["Product Name"] = {"title": [{"text": {"content": f"{row['product_type']} — {row['finish']} — {row['size_inches']}"}}]}
    return props


def create_notion_records(artwork_db_id, product_db_id):
    artwork_rows = read_artwork_csv("ASQ_Freelance/Arts_of_August_System/AOA_datasets/artworks/artwork_records/AOA_ART_0061.csv")
    product_rows = read_artwork_csv("ASQ_Freelance/Arts_of_August_System/AOA_datasets/products/product_records/AOA_PRD_0061.csv")

    if len(artwork_rows) != 1:
        raise ValueError("Expected one artwork row in AOA_ART_0061.csv")

    artwork_properties = build_artwork_properties(artwork_rows[0])
    print("Creating artwork page in Notion...")
    artwork_page = create_page(artwork_db_id, artwork_properties)
    artwork_page_id = artwork_page.get("id")
    print(f"Artwork page created: {artwork_page_id}")

    created_products = []
    for row in product_rows:
        product_properties = build_product_properties(row, artwork_page_id)
        print(f"Creating product record {row.get('product_id')}...")
        product_page = create_page(product_db_id, product_properties)
        created_products.append(product_page.get("id"))
    print(f"Created {len(created_products)} product records.")
    return artwork_page, created_products


def main():
    if len(sys.argv) < 3:
        print("Usage: python notion_push_aoa_artwork.py <artwork_database_id> <product_database_id>")
        sys.exit(1)
    artwork_db_id = sys.argv[1]
    product_db_id = sys.argv[2]
    create_notion_records(artwork_db_id, product_db_id)


if __name__ == "__main__":
    main()
