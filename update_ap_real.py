import json

filepath = r"C:\Users\recla\Downloads\pincode-dataindia\andhra-pradesh.json"
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Loaded {len(data)} records.")

ap_map = {
  "Srikakulam": "Srikakulam", "Tekkali": "Srikakulam", "Palasa": "Srikakulam",
  "Bobbili": "Vizianagaram", "Vizianagaram": "Vizianagaram", "Cheepurupalle": "Vizianagaram",
  "Parvathipuram": "Parvathipuram Manyam", "Palakonda": "Parvathipuram Manyam",
  "Rampachodavaram": "Alluri Sitharama Raju", "Paderu": "Alluri Sitharama Raju",
  "Bheemunipatnam": "Visakhapatnam", "Visakhapatnam": "Visakhapatnam",
  "Anakapalli": "Anakapalli", "Narasipatnam": "Anakapalli",
  "Kakinada": "Kakinada", "Peddapuram": "Kakinada",
  "Kothapeta": "Dr. B. R. Ambedkar Konaseema", "Amalapuram": "Dr. B. R. Ambedkar Konaseema", "Ramachandrapuram": "Dr. B. R. Ambedkar Konaseema",
  "Rajahmundry": "East Godavari", "Kovvur": "East Godavari",
  "Narasapuram": "West Godavari", "Bhimavaram": "West Godavari",
  "Eluru": "Eluru", "Jangareddigudem": "Eluru", "Nuzvid": "Eluru",
  "Machilipatnam": "Krishna", "Gudivada": "Krishna", "Vuyyuru": "Krishna",
  "Tiruvuru": "NTR District", "Vijayawada": "NTR District", "Nandigama": "NTR District",
  "Guntur": "Guntur", "Tenali": "Guntur",
  "Bapatla": "Bapatla", "Repalle": "Bapatla", "Chirala": "Bapatla",
  "Settenapalli": "Palnadu", "Narasaraopet": "Palnadu", "Gurazala": "Palnadu",
  "Markapur": "Prakasam", "Kanigiri": "Prakasam", "Ongole": "Prakasam",
  "Nellore": "SPS Nellore", "Kandukur": "SPS Nellore", "Kavali": "SPS Nellore",
  "Kurnool": "Kurnool", "Pattikonda": "Kurnool", "Adoni": "Kurnool",
  "Nandyal": "Nandyal", "Atmakur": "Nandyal", "Dhone": "Nandyal",
  "Anantapur": "Ananthapuram", "Guntakal": "Ananthapuram", "Kalyanadurg": "Ananthapuram",
  "Penukonda": "Sri Sathya Sai", "Dharmavaram": "Sri Sathya Sai", "Kadiri": "Sri Sathya Sai", "Puttaparthi": "Sri Sathya Sai",
  "Kadapa": "YSR Kadapa", "Badvel": "YSR Kadapa", "Jammalamadugu": "YSR Kadapa", "Pulivendula": "YSR Kadapa",
  "Rayachoti": "Annamayya", "Madanapalle": "Annamayya", "Rajampeta": "Annamayya",
  "Chittoor": "Chittoor", "Nagari": "Chittoor", "Palamaner": "Chittoor", "Kuppam": "Chittoor",
  "Tirupati": "Tirupati District", "Srikalahasti": "Tirupati District", "Gundur": "Tirupati District", "Sullurpeta": "Tirupati District"
}

updated_count = 0
for r in data:
    if 'divisionname' in r:
        div = r['divisionname'].replace(' Division', '').strip()
        if div in ap_map:
            r['district'] = ap_map[div]
            updated_count += 1

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, separators=(',', ':'))

print(f"Updated {updated_count} records.")
