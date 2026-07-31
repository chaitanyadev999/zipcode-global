import os

report_file = r'C:\Users\recla\zipcode-global\pages\report.html'

with open(report_file, 'r', encoding='utf-8') as f:
    content = f.read()

old_script = """  const statusSub   = document.getElementById('statusSub');
  const successScreen = document.getElementById('successScreen');

  function showStatus(type, icon, title, sub) {"""

new_script = """  const statusSub   = document.getElementById('statusSub');
  const successScreen = document.getElementById('successScreen');

  // Auto-fill from URL params
  const urlParams = new URLSearchParams(window.location.search);
  const pCountry = urlParams.get('country');
  const pOffice = urlParams.get('office');
  const pPin = urlParams.get('pin');
  
  if (pCountry) {
    const countrySelect = document.getElementById('fCountry');
    for (let i = 0; i < countrySelect.options.length; i++) {
      if (countrySelect.options[i].value === pCountry) {
        countrySelect.selectedIndex = i;
        break;
      }
    }
  }
  
  if (pPin) {
    document.getElementById('fWrongCode').value = pPin;
  }
  
  if (pOffice) {
    document.getElementById('fDetails').value = "Issue regarding: " + pOffice + "\\n\\n";
  }

  function showStatus(type, icon, title, sub) {"""

if old_script in content:
    content = content.replace(old_script, new_script)
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully added auto-fill logic to report.html")
else:
    print("Could not find the script block in report.html")
