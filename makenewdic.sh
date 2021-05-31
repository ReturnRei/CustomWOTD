#!/bin/bash
cp -r /System/Library/Screen\ Savers/Word\ of\ the\ Day.saver .
cp -r ./Word\ of\ the\ Day.saver Word\ of\ the\ Day.saver.bak
mv Word\ of\ the\ Day.saver ./Word\ of\ the\ Day01.saver

echo "<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>DCSWotDBoldFontName</key>
	<string>TsukuARdGothic-Bold</string>
	<key>DCSWotDDictionaryID</key>
	<string>com.apple.dictionary.ja.Daijirin</string>
	<key>DCSWotDDictionaryName</key>
	<string>スーパー大辞林</string>
	<key>DCSWotDEntries</key>" > WotD_info_DJR.plist
ruby ./ParseCsvPlist.rb >> WotD_info_DJR.plist
echo "	<key>DCSWotDIntendedLanguage</key>
	<string>ja</string>
	<key>DCSWotDRegularFontName</key>
	<string>TsukuARdGothic-Regular</string>
</dict>
</plist>" >> WotD_info_DJR.plist
plutil -convert binary1 WotD_info_DJR.plist
mv WotD_info_DJR.plist ./Word\ of\ the\ Day01.saver/Contents/Resources/WordLists