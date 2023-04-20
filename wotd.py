import plistlib
import csv
import sys
import os

if os.path.isdir("/Library/Screen Savers/Word of the Dayrr.saver"):
    print("Modified WOTD exists, proceeding")
else:
    print("Modified WOTD does not exist, copying original")
    try:
        os.system("cp -R '/System/Library/Screen Savers/Word of the Day.saver' 'Word of the Dayrr.saver'")
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
# open the CSV file and read its contents
with open(csv_file, 'r', encoding='utf-8') as file:
    # create a CSV reader object
    reader = csv.reader(file)
    # loop through each row in the file
    for row in reader:
        # check that the row contains exactly three columns
        if len(row) == 3:
            # add the row as a list of three elements to the rows list
            rows.append(row)
        else:
            # handle rows with incorrect number of columns here
            pass

with open('/Library/Screen Savers/Word of the Dayrr.saver/Contents/Resources/WordLists/WotD_info_DJR.plist', 'rb') as tmpPlist:
    tmpPlistOpen = plistlib.load(tmpPlist, fmt=None, dict_type=dict)
#check for the DCSWotDentriesDate dictionary and removes it if it exists
if 'DCSWotDEntriesByDate' in tmpPlistOpen.keys():
    print('DCSWotDEntriesByDate dictionary exists')
    del tmpPlistOpen['DCSWotDEntriesByDate']
    print('DCSWotDentriesDate dictionary removed')
#check for the DCSWotDEntries array
if 'DCSWotDEntries' in tmpPlistOpen.keys():
    print('DCSWotDEntries array exists')
else:
    tmpPlistOpen['DCSWotDEntries'] = []
    print('DCSWotDEntries array created')    
    # clears the array if not empty
if len(tmpPlistOpen['DCSWotDEntries']) > 0:
    tmpPlistOpen['DCSWotDEntries'].clear()
    print('DCSWotDEntries array cleared')
    #loop through the rows and create a dictionary for each row
    for r in rows:
        #create a dictionary for each row
        tmpDict = {}
        #add the first column to the dictionary as DCSWotDEntryHeadword
        tmpDict['DCSWotDEntryHeadword'] = r[0]
        #add the second column to the dictionary as DCSWotDEntrySecondaryHeadword
        tmpDict['DCSWotDEntrySecondaryHeadword'] = r[1]
        #add the third column to the dictionary as DCSWotDEntryDefinition
        tmpDict['DCSWotDEntrySense'] = r[2]
        #append the dictionary to the DCSWotDEntries array
        tmpPlistOpen['DCSWotDEntries'].append(tmpDict)

# write the modified plist file
with open('/Library/Screen Savers/Word of the Dayrr.saver/Contents/Resources/WordLists/WotD_info_DJR.plist', 'wb') as tmpPlist:
    plistlib.dump(tmpPlistOpen, tmpPlist)
print("New screensaver for you")
