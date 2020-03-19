# Instagram JSON Viewer

This script transforms Instagram's data - [that you get via the Data Download Tool](https://www.instagram.com/download/request/) - to a readable format!

## Screenshots

![HTML1](screenshot1.jpg)
![HTML2](screenshot2.jpg)

## Features

- Transforms profile information, media and messages into a more readable html format!
- Creates separate html pages for each chat!
- Easy to use: Just execute the script in json-directory.
- Functions can be imported and tuned to your needs!

## Requirements

- Python (version 3.0 and above)

## Data Download

Here you can download your data: [Instagram](https://www.instagram.com/download/request/)

## Basic Usage

- Back up your instagram data before you run anything!
- Put "instaview.py" into the data directory (e.g. where the all json-files are!)  
  E.g. my downloaded zip-archive was named "micha_birklbauer_20200316.zip", extracted the directory looked like this:
  ```
  +---- micha_birklbauer_20200316
  + direct
  + photos
  + profile
  + stories
  + videos
  | account_history.json
  | autofill.json
  | checkout.json
  | comments.json
  | connections.json
  | contacts.json
  | likes.json
  | media.json
  | messages.json
  | profile.json
  | saved.json
  | searches.json
  | settings.json
  | stories_activities.json
  | instaview.py (PYTHON SCRIPT GOES HERE!)
  ```
- Run "instaview.py" via commandline (recommended) or doubleclick!
- Check "instaview_report.html" in the browser of your choice!

## Advanced Usage

```python
from instaview import *

instaview()
```

**Functions:**
- **read_profile(filename = "profile.json"):**  
  Reads profile information from json file and returns readable and structured html string.
  - **Args:**
    - filename (str): Path to json with profile information. Default: "profile.json".
  - **Return (str):** json converted to html.
- **read_searches(filename = "searches.json"):**  
  Reads search information from json file and returns readable and structured html string.
  - **Args:**
    - filename (str): Path to json with search information. Default: "searches.json".
  - **Return (str):** json converted to html.
- **read_connections(filename = "connections.json"):**  
  Reads connection information from json file and returns readable and structured html string.
  - **Args:**
    - filename (str): Path to json with connection information. Default: "connections.json".
  - **Return (str):** json converted to html.
- **read_media(filename = "media.json"):**  
  Reads media information from json file and returns readable and structured html string.
  - **Args:**
    - filename (str): Path to json with media information. Default: "media.json".
  - **Return (str):** json converted to html.
- **read_comments(filename = "comments.json"):**  
  Reads comment information from json file and returns readable and structured html string.
  - **Args:**
    - filename (str): Path to json with comment information. Default: "comments.json".
  - **Return (str):** json converted to html.
- **read_messages(filename = "messages.json", profile = "profile.json", use_default = True, default_avatar = "DEFAULT", hd = False):**  
  Reads message information from json file and creates separate html files for each chat in new "chat" directory. Links to html pages are returned as concatenated html string together with a list of chat participants.
  - **Args:**
    - filename (str): Path to json with message information. Default: "messages.json".
    - profile (str): Path to json with profile information. Default: "profile.json".
    - use_default (bool): If default avatar should be used or not. Default: True.
    - default_avatar (str): Path to default avatar. Default: Profile Picture from "profile.json".
    - hd (bool): If high definition versions of avatars should be used or not. Default: False.
  - **Return (list):** [formatted html string (str), list of chats and their participants (list of str)].
- **instaview(default_filenames = True, filenames = ["profile.json", "searches.json", "connections.json", "media.json", "comments.json", "messages.json"], title = "", show_credits = True, \*\*kwargs):**  
  Executes all functions and creates an html report including information from all used json files. Returns 0 if everything went correctly.
  - **Args:**
    - default_filenames (bool): If default filenames should be used. Default: True.
    - filenames (list of str): A list with paths to the specific json files in the following order:
      1. Profile information
      2. Search information
      3. Connection information
      4. Media information
      5. Comment information
      6. Message information
      Default: Default filenames for every function (see above).
    - title (valid html as str): What the title of the report should be. Default: "INSTAGRAM DATA + [Date]".
    - show_credits (bool): If credits should be added at the bottom of the report. Default: True.
    - \*\*kwargs: any additional arguments will be passed to "read_messages()" (see above).
  - **Return (int):** 0 if successfully, >0 if unsuccesfull or only partly successful.

## Changes to old release

- Not reliant on R/Markdown/LaTeX anymore!
- HTML instead of PDF!
- PDF can still be created with browser!
- Full emoji/unicode support!
- Separate pages for chats!

## Known Issues

- I didn't include contacts.json since I didn't sync my contacts and therefore had no data available on that. Furthermore account_history.json, autofill.json, checkout.json, likes.json, saved.json, settings.json and stories_activities.json are also not included because I found the information in there is not really useful (e.g. likes.json/saves.json don't include post information etc.)!
- If you have huge amounts of chats avatars might not load correctly because instagram blocks your IP after too many requests. This might also happen if you run the script several times consecutively!
- This is rather experimental since I only had my own data to test this with, there's no guarantee that this also works with your data!

## License

[MIT License](https://github.com/t0xic-m/instagram_data_download_viewer/blob/master/LICENSE.md)

## Download

- ZIP: [DOWNLOAD](https://github.com/t0xic-m/instagram_json_viewer/archive/master.zip)
- TAR.GZ: [DOWNLOAD](https://github.com/t0xic-m/instagram_json_viewer/archive/master.tar.gz)

## Contact

- Website: [Web](https://t0xic-m.github.io/web)
- Website: [GitHub](https://t0xic-m.github.io/)
- Contact: [Mail](mailto:micha.birklbauer@gmail.com)
