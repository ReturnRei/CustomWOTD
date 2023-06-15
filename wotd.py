import plistlib
import csv
import sys
import os
import logging

logging.basicConfig(level=logging.DEBUG)
entries = []


def copy_open_first_run():
    if os.path.isdir("/Library/Screen Savers/Word of the Dayrr.saver"):
        logging.debug("Modified WOTD exists, proceeding")
    else:
        logging.debug("Modified WOTD does not exist, copying original")
        try:
            os.system("cp -R '/System/Library/Screen Savers/Word of the Day.saver' '/tmp/Word of the Dayrr.saver'")
            os.system("open '/tmp/Word of the Dayrr.saver'")
            print("Rerun script after adding WOTD screensaver")
        except Exception as e:
            print(f"Caught exception: {e}")
        finally:
            exit(1)


def csv_case():
    try:
        csv_file = sys.argv[1]
    except IndexError:
        raise ValueError('Provide csv as argument')

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        entries.extend([row for row in reader if len(row) == 3])


def manage_plist():
    plist_file_path = '/Library/Screen Savers/Word of the Dayrr.saver/Contents/Resources/WordLists/WotD_info_DJR.plist'

    with open(plist_file_path, 'rb') as plist_file:
        plist_content = plistlib.load(plist_file, fmt=None, dict_type=dict)

    if 'DCSWotDEntriesByDate' in plist_content.keys():
        del plist_content['DCSWotDEntriesByDate']
        logging.debug('DCSWotDentriesDate dictionary removed')

    if 'DCSWotDEntries' in plist_content.keys():
        logging.debug('DCSWotDEntries array exists')
    else:
        plist_content['DCSWotDEntries'] = []
        logging.debug('DCSWotDEntries array created')

    if len(plist_content['DCSWotDEntries']) > 0:
        plist_content['DCSWotDEntries'].clear()
        logging.debug('DCSWotDEntries array cleared')

    plist_content['DCSWotDEntries'] = [
        {
            'DCSWotDEntryHeadword': entry[0],
            'DCSWotDEntrySecondaryHeadword': entry[1],
            'DCSWotDEntrySense': entry[2]
        }
        for entry in entries
    ]

    with open(plist_file_path, 'wb') as plist_file:
        plistlib.dump(plist_content, plist_file)
        logging.debug('Screensaver updated')


def main():
    copy_open_first_run()
    csv_case()
    manage_plist()


if __name__ == '__main__':
    main()
