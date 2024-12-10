import json
import sys

def update_json(performers_file, mapping_file):
    try:

        with open(performers_file, 'r', encoding='utf-8') as pf:
            performers_data = json.load(pf)
        
        with open(mapping_file, 'r', encoding='utf-8') as mf:
            mapping_data = json.load(mf)

        for performer_data in performers_data:
            if "performance_category" in performer_data:
                original_category = performer_data.get("performance_category")
                if original_category in mapping_data:
                    performer_data["performance_category"] = mapping_data[original_category]
                    print(f"Updated '{original_category}' to '{performer_data['performance_category']}'")
                else:
                    print(f"No mapping found for '{original_category}'")

        with open(performers_file, 'w', encoding='utf-8') as sf:
            json.dump(performers_data, sf, indent=4, ensure_ascii=False)
        print(f"File '{performers_file}' updated successfully.")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python update_json.py <performers_file> <mapping_file>")
        sys.exit(1)
    else:
        performers_file = sys.argv[1]
        mapping_file = sys.argv[2]
        update_json(performers_file, mapping_file)
