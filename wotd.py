import plistlib
import csv
import sys
import os
import logging

if os.path.isdir("/Library/Screen Savers/Word of the Dayrr.saver"):
    logging.debug("Modified WOTD exists, proceeding")
else:
    logging.debug("Modified WOTD does not exist, copying original")
    try:
        os.system("cp -R '/System/Library/Screen Savers/Word of the Day.saver' 'Word of the Dayrr.saver'") # Need to do some mktemp-like stuff here
        os.system("open 'Word of the Dayrr.saver'")
        print("Rerun script after adding WOTD screensaver")
    except:
        print("Check for original WOTD path")
    finally:
        exit(1)

rows = []
try:
    csv_file = sys.argv[1]
except IndexError:
    print('Provide csv as argument')
    exit(1)

with open(csv_file, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) == 3:
            rows.append(row)
        else:
            # !=3 to be implemented
            pass

with open('/Library/Screen Savers/Word of the Dayrr.saver/Contents/Resources/WordLists/WotD_info_DJR.plist', 'rb') as tmpPlist:
    tmpPlistOpen = plistlib.load(tmpPlist, fmt=None, dict_type=dict)

if 'DCSWotDEntriesByDate' in tmpPlistOpen.keys():
    del tmpPlistOpen['DCSWotDEntriesByDate']
    logging.debug('DCSWotDentriesDate dictionary removed')

if 'DCSWotDEntries' in tmpPlistOpen.keys():
    logging.debug('DCSWotDEntries array exists')
else:
    tmpPlistOpen['DCSWotDEntries'] = []
    logging.debug('DCSWotDEntries array created')

if len(tmpPlistOpen['DCSWotDEntries']) > 0:
    tmpPlistOpen['DCSWotDEntries'].clear()
    logging.debug('DCSWotDEntries array cleared')

for r in rows:
    tmpDict = {}
    tmpDict['DCSWotDEntryHeadword'] = r[0]
    tmpDict['DCSWotDEntrySecondaryHeadword'] = r[1]
    tmpDict['DCSWotDEntrySense'] = r[2]
    tmpPlistOpen['DCSWotDEntries'].append(tmpDict)

with open('/Library/Screen Savers/Word of the Dayrr.saver/Contents/Resources/WordLists/WotD_info_DJR.plist', 'wb') as tmpPlist:
    plistlib.dump(tmpPlistOpen, tmpPlist)

print("New screensaver for you")
