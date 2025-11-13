import os
import re

def fix_mobile_buttons():
    # Directory containing the HTML files
    directory = '.'

    # Pattern to match detail-*.html files
    pattern = re.compile(r'^detail-.*\.html$')

    # The old CSS block to replace
    old_css = r'''@media (max-width: 768px) {
            * {
                box-sizing: border-box;
            }
            
            body {
                padding: 10px;
                margin: 0;
                overflow-x: hidden;
            }
            
            .back-button-fixed {
                position: fixed;
                top: 10px;
                left: 10px;
                padding: 8px 12px;
                font-size: 11px;
                z-index: 1001;
                max-width: calc(100vw - 20px);
                white-space: nowrap;
            }
            
            #prevBtn {    position: fixed;    bottom: 55px;    left: 10px;    z-index: 1000;}#nextBtn {    position: fixed;    bottom: 55px;    right: 10px;    z-index: 1000;}
            
            .nav-button {
                width: 100%;
                padding: 10px 12px;
                font-size: 11px;
                text-align: center;
                white-space: nowrap;
            }
            
            .content, .container, main, article {
                padding-top: 130px !important;
                max-width: 100vw;
                overflow-x: hidden;
            }
            
            h1 {
                font-size: 1.5em !important;
            }
            
            h2 {
                font-size: 1.3em !important;
            }
            
            p, li, div {
                font-size: 14px !important;
                word-wrap: break-word;
            }
        }'''

    # The new CSS block
    new_css = r'''@media (max-width: 768px) {
            * {
                box-sizing: border-box;
            }

            body {
                padding: 10px;
                margin: 0;
                overflow-x: hidden;
            }

            .back-button-fixed {
                position: fixed;
                top: 10px;
                left: 10px;
                padding: 8px 12px;
                font-size: 11px;
                z-index: 1001;
                max-width: calc(100vw - 20px);
                white-space: nowrap;
            }

            #prevBtn {    position: fixed;    bottom: 55px;    left: 10px;    z-index: 1000;}#nextBtn {    position: fixed;    bottom: 55px;    right: 10px;    z-index: 1000;}

            .nav-button {
                padding: 8px 10px;
                font-size: 10px;
                text-align: center;
                white-space: nowrap;
            }

            #prevBtn, #nextBtn {
                width: auto;
                max-width: calc(50vw - 20px);
            }

            .content, .container, main, article {
                padding-top: 130px !important;
                max-width: 100vw;
                overflow-x: hidden;
            }

            h1 {
                font-size: 1.5em !important;
            }

            h2 {
                font-size: 1.3em !important;
            }

            p, li, div {
                font-size: 14px !important;
                word-wrap: break-word;
            }
        }'''

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if pattern.match(filename):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()

                # Replace the old CSS with the new one
                new_content = content.replace(old_css, new_css)

                # Write back if changed
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    print(f"Updated {filename}")
                else:
                    print(f"No changes needed for {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    fix_mobile_buttons()