import os
from bs4 import BeautifulSoup

def separate_html_assets(html_file_path):
    """
    Separates CSS and JavaScript from an HTML file into separate files and updates the HTML.
    
    :param html_file_path: Path to the input HTML file
    """
    try:
        print(f"Reading HTML file: {html_file_path}")
        # Read the HTML file
        with open(html_file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        print("Parsing HTML content...")
        # Parse the HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Prepare output paths
        base_path, _ = os.path.splitext(html_file_path)
        css_file_path = base_path + '_styles.css'
        js_file_path = base_path + '_scripts.js'

        print(f"Output paths set: CSS -> {css_file_path}, JS -> {js_file_path}")

        # Initialize containers for CSS and JavaScript content
        css_content = []
        js_content = []

        # Extract <style> tags
        print("Extracting <style> tags...")
        for style_tag in soup.find_all('style'):
            css_content.append(style_tag.string or '')
            print(f"Extracted CSS: {style_tag.string}")
            style_tag.decompose()  # Remove the tag from the HTML

        # Extract <script> tags
        print("Extracting <script> tags...")
        for script_tag in soup.find_all('script'):
            if script_tag.string:  # Ensure it's not an external script
                js_content.append(script_tag.string)
                print(f"Extracted JS: {script_tag.string}")
                script_tag.decompose()  # Remove the tag from the HTML

        # Extract inline styles (e.g., <div style="...")
        print("Extracting inline styles...")
        for tag in soup.find_all(style=True):
            inline_style = f"{tag.name} {{ {tag['style']} }}"
            css_content.append(inline_style)
            print(f"Extracted inline style: {inline_style}")
            del tag['style']  # Remove inline style

        # Write CSS content to a new file
        if css_content:
            print("Writing CSS content to file...")
            with open(css_file_path, 'w', encoding='utf-8') as css_file:
                css_file.write('\n'.join(css_content))

            # Link the new CSS file in the HTML
            print("Linking CSS file in HTML...")
            new_link_tag = soup.new_tag('link', rel='stylesheet', href=os.path.basename(css_file_path))
            soup.head.append(new_link_tag)

        # Write JavaScript content to a new file
        if js_content:
            print("Writing JavaScript content to file...")
            with open(js_file_path, 'w', encoding='utf-8') as js_file:
                js_file.write('\n'.join(js_content))

            # Link the new JavaScript file in the HTML
            print("Linking JavaScript file in HTML...")
            new_script_tag = soup.new_tag('script', src=os.path.basename(js_file_path))
            soup.body.append(new_script_tag)

        # Write the updated HTML back to a file
        updated_html_path = base_path + '_updated.html'
        print(f"Writing updated HTML to: {updated_html_path}")
        with open(updated_html_path, 'w', encoding='utf-8') as updated_html_file:
            updated_html_file.write(str(soup.prettify()))

        print(f"CSS saved to: {css_file_path}")
        print(f"JavaScript saved to: {js_file_path}")
        print(f"Updated HTML saved to: {updated_html_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
# Replace 'example.html' with the path to your HTML file
separate_html_assets('index_main_2.html')

