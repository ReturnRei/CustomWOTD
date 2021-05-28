## Tweak Word of the day screensaver in MacOs to make your own lists

### TLDR: Copy WOTD to a user directory, mess around with plists, rename the .saver file and install it

In MacOs Big Sur the default Screensavers directory is in `/System/Library/Screen Savers/` which is non writable even with root priviledges (nope for a csrutil disable)

Copy the screensaver to a safe directory `cp -r /System/Library/Screen\ Savers/Word\ of\ the\ Day.saver .`
*I would reccomend a backup of this file*

You can now tweak your .plists as much as you want

Rename The`.saver` file to be able to install

After the install the PATH is `/Library/Screen Savers` you can still mess around with your files here

Different dictionaries use different logic in their .plist and after messing around with dictionary files I realized that the Japanese .plist contains all the data necessary for its functioning within it without the need of messing with words id's in related dictionaries

`Use plutil to convert your plist to friendly formats and play around`

#### In the project there's currently a csv parser I made in ruby and a custom made .plist with words from N4-N3 Vocabulary list (Japanese)

Here's the result ![E1xgpBfXoAQwW-M](https://user-images.githubusercontent.com/50523188/120007580-584ab980-bfda-11eb-9301-3d94862f0b99.jpg)


#### Project in its infancy, I'm posting this as I saw people were struggling with most recent MacOs versions to customize WOTD Screensaver, whether you're tech savy and would like to help me with a clean implementation of this or a language learner and would like to have help to set this up I would love to join our efforts

*PS: I believe this is useful as an addition to an anki deck for SRS learning*
