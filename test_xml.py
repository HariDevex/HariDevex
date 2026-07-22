import xml.etree.ElementTree as ET
import sys

def check_svg(filename):
    try:
        tree = ET.parse(filename)
        print(f"✅ {filename} is valid XML/SVG!")
    except Exception as e:
        print(f"❌ {filename} XML Error: {e}")

if __name__ == "__main__":
    for f in sys.argv[1:]:
        check_svg(f)
