import sys

REMOVE_KEYS = ['annote', 'file']

def removeBibKey(content, key):
    skipped = []
    while content.find(key) >= 0:
        start = content.find(key)
        end = start + len(key)
        if content[start-1] != '\n':
            content = content[:start] + content[end:]
            skipped.append(start)
            continue

        i = content[start:].find('{')
        count = 1
        while count > 0:
            i += 1
            if content[start + i] == '{':
                count += 1
            elif content[start + i] == '}':
                count -= 1
        if content[start + i + 1] == ',':
            i += 1
        if content[start - 1] == '\n':
            start -= 1
        end = start + i + 1
        #print 'REMOVING ' + content[start:end + 1]
        content = content[:start] + content[end + 1:]
    skipped.reverse()
    for skip in skipped:
        content = content[:skip] + key + content[skip:]
    return content

bibcontent = ''

with open(sys.argv[1], 'r') as bibfile:
    bibcontent = bibfile.read()

    for key in REMOVE_KEYS:
        bibcontent = removeBibKey(bibcontent, key)

with open(sys.argv[1], 'w') as bibfile:
    bibfile.write(bibcontent)
