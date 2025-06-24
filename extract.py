import os
import re
import yaml

import re

def extract_info_from_text(text):
    fitxa_match = re.search(r"Fitxa\s+(\d+/\d+)", text)
    versio_match = re.search(r"Darrera versió:\s*([0-9.]+)", text)
    titol_match = re.search(r"Títol\s+(.*?)(?=\s+Resposta)", text, re.DOTALL)
    resposta_match = re.search(r"Resposta\s+(.*)", text, re.DOTALL)

    return {
        "Fitxa": fitxa_match.group(1) if fitxa_match else "",
        "Darrera versió": versio_match.group(1) if versio_match else "",
        "Títol": titol_match.group(1).strip() if titol_match else "",
        "Resposta": resposta_match.group(1).strip() if resposta_match else ""
    }

def process_directory(directory):
    all_entries = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()
                info = extract_info_from_text(text)
                all_entries.append(info)
    return all_entries

# Main process
directory = "downloaded_pages"
output_file = "optimot.yml"

data = process_directory(directory)

# Write to YAML
with open(output_file, 'w', encoding='utf-8') as f:
    yaml.dump(data, f, allow_unicode=True, sort_keys=False)

print(f"YAML file written to {output_file} with {len(data)} entries.")

