import re

page = re.compile(r'Page (\d+)')
page_number = 0

page_info = re.compile(r' (\d.\d\d\d\d\d)  (\d.\d\d\d\d\d)  (\d.\d\d\d\d\d)  (\d.\d\d\d\d\d) CMYK')

color_pages = []

if __name__ == '__main__':
    with open('ghostscript-check.txt', 'r') as gs_check:
        for line in gs_check:
            page_match = page.match(line)
            info_match = page_info.match(line
                                         )
            if page_match:
                page_number = page_match.group(1)
            elif info_match:
                if info_match.group(1) != '0.00000' or info_match.group(2) != '0.00000' or info_match.group(3) != '0.00000':
                    color_pages.append(page_number)
    print('Color Pages (including grey):')
    print(', '.join(color_pages))
