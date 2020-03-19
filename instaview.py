#!/usr/bin/env python3

# INSTAGRAM JSON VIEWER
# 2020 (c) Micha Johannes Birklbauer
# https://github.com/t0xic-m/
# micha.birklbauer@gmail.com

import urllib.request as ur
import datetime
import json
import os

# template html
# largely taken and adapted from w3schools.com
# -> https://www.w3schools.com/howto/howto_css_fixed_sidebar.asp
# -> https://www.w3schools.com/howto/howto_css_chat.asp
html_template = \
"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Instagram Data Report">
<meta name="author" content="Micha Birklbauer">

<title>Instagram Data Report</title>

<style>
body {
  font-family: "Times New Roman", Times, serif;
}

.sidenav {
  height: 100%;
  width: 160px;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  background-color: #fff;
  overflow-x: hidden;
  padding-top: 20px;
}

.sidenav a {
  padding: 6px 8px 6px 16px;
  text-decoration: none;
  font-size: 25px;
  color: #111;
  display: block;
}

.sidenav a:hover {
  color: #f1f1f1;
}

.main {
  margin-left: 160px;
  font-size: 25px;
  padding: 0px 10px;
}

.main img {
  max-width: 500px;
  width: 100%;
}

.main audio {
  max-width: 500px;
  width: 100%;
}

.main video {
  max-width: 500px;
  width: 100%;
}

@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {font-size: 18px;}
}

.container {
  border: 2px solid #000;
  background-color: #ffffff;
  border-radius: 5px;
  padding: 10px;
  margin: 10px 0;
}

.darker {
  border-color: #000;
  background-color: #66b3ff;
}

.container::after {
  content: "";
  clear: both;
  display: table;
}

.container img {
  max-width: 500px;
  width: 100%;
}

.container img.left {
  float: left;
  max-width: 60px;
  width: 100%;
  margin-right: 20px;
  border-radius: 50%;
}

.container img.right {
  float: right;
  max-width: 60px;
  width: 100%;
  margin-left: 20px;
  border-radius: 50%;
}

.container audio {
  max-width: 500px;
  width: 100%;
}

.container video {
  max-width: 500px;
  width: 100%;
}

.time-right {
  float: right;
  color: #000;
}

.time-left {
  float: left;
  color: #000;
}
</style>
</head>
<body>

"""

# template sidebar html
sidebar_template = \
"""
<div class="sidenav">
    <a href="#profile">Profile Information</a>
    <a href="#searches">Searches</a>
    <a href="#connections">Profile Connections</a>
    <a href="#media">Media</a>
    <a href="#stories">Stories</a>
    <a href="#photos">Photos</a>
    <a href="#pictures">Profile Pictures</a>
    <a href="#videos">Videos</a>
    <a href="#direct">Direct Messages Media</a>
    <a href="#comments">Comments</a>
    <a href="#mediacomments">Media Comments</a>
    <a href="#livecomments">Live Comments</a>
    <a href="#storycomments">Story Comments</a>
    <a href="#messages">Messages</a>

"""

# patting myself on the shoulder for this one uwu
credits = \
"""
<h2 id="#credits">Credits</h2>

    <p>
        Report created with Micha Birklbauer's <a href="https://github.com/t0xic-m/instagram_json_viewer">Instagram JSON Viewer</a>.
    </p>
"""

# reading profile information and converting it to html string
# default filenames and arguments should be fine for all functions if script is in the right directory
def read_profile(filename = "profile.json"):

    html_string = "<h2 id=\"profile\">Profile Information</h2>\n\t<ul>\n"

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        f.close()

    for item in data:
        html_string = html_string + "\t\t<li><b>" + str(item) + ":</b> " + str(data[item]) + "</li>\n"

    html_string = html_string + "\t</ul>\n<hr>\n"

    return html_string

# reading search information and converting it to html string
def read_searches(filename = "searches.json"):

    html_string = "<h2 id=\"searches\">Profile Searches</h2>\n\t<ul>\n"

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        f.close()

    counter = 1
    for item in data:
        html_string = html_string + "\t\t<li><b>Search " + str(counter) + ":</b>\n\t\t\t<ul>\n"
        for subitem in item:
            html_string = html_string + "\t\t\t\t<li><b>" + str(subitem) + ":</b> " + str(item[subitem]) + "</li>\n"
        html_string = html_string + "\t\t\t</ul>\n\t\t</li>\n"
        counter = counter + 1

    html_string = html_string + "\t</ul>\n<hr>\n"

    return html_string

# reading connection information and converting it to html string
def read_connections(filename = "connections.json"):

    html_string = "<h2 id=\"connections\">Profile Connections</h2>\n\t<ul>\n"

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        f.close()

    blocked_users = data["blocked_users"]
    restricted_users = data["restricted_users"]
    follow_requests_sent = data["follow_requests_sent"]
    followers = data["followers"]
    following = data["following"]
    following_hashtags = data["following_hashtags"]
    dismissed_suggested_users = data["dismissed_suggested_users"]

    html_string = html_string + "<h3>Blocked Users</h3>\n\t<ul>\n"

    if len(blocked_users) == 0:
        html_string = html_string + "\t\t<li>None</li>\n"
    else:
        for item in blocked_users:
            html_string = html_string + "\t\t<li>" + str(item) + " <b>blocked since</b> " + str(blocked_users[item]) + "</li>\n"

    html_string = html_string + "\t</ul>\n\n<h3>Restricted Users</h3>\n\t<ul>\n"

    if len(restricted_users) == 0:
        html_string = html_string + "\t\t<li>None</li>\n"
    else:
        for item in restricted_users:
            html_string = html_string + "\t\t<li>" + str(item) + " <b>restricted since</b> " + str(restricted_users[item]) + "</li>\n"

    html_string = html_string + "\t</ul>\n\n<h3>Requested Following</h3>\n\t<ul>\n"

    if len(follow_requests_sent) == 0:
        html_string = html_string + "\t\t<li>None</li>\n"
    else:
        for item in follow_requests_sent:
            html_string = html_string + "\t\t<li>" + str(item) + " <b>request sent</b> " + str(follow_requests_sent[item]) + "</li>\n"

    html_string = html_string + "\t</ul>\n\n<h3>Following Users</h3>\n\t<ul>\n"

    if len(following) == 0:
        html_string = html_string + "\t\t<li>None</li>\n"
    else:
        for item in following:
            html_string = html_string + "\t\t<li>" + str(item) + " <b>followed since</b> " + str(following[item]) + "</li>\n"

    html_string = html_string + "\t</ul>\n\n<h3>Following Hashtags</h3>\n\t<ul>\n"

    if len(following_hashtags) == 0:
        html_string = html_string + "\t\t<li>None</li>\n"
    else:
        for item in following_hashtags:
            html_string = html_string + "\t\t<li>" + str(item) + " <b>followed since</b> " + str(following_hashtags[item]) + "</li>\n"

    html_string = html_string + "\t</ul>\n\n<h3>Followers</h3>\n\t<ul>\n"

    if len(followers) == 0:
        html_string = html_string + "\t\t<li>None</li>\n"
    else:
        for item in followers:
            html_string = html_string + "\t\t<li>" + str(item) + " <b>has followed since</b> " + str(followers[item]) + "</li>\n"

    html_string = html_string + "\t</ul>\n\n<h3>Dismissed Suggested Users</h3>\n\t<ul>\n"

    if len(dismissed_suggested_users) == 0:
        html_string = html_string + "\t\t<li>None</li>\n"
    else:
        for item in dismissed_suggested_users:
            html_string = html_string + "\t\t<li>" + str(item) + " <b>dismissed on</b> " + str(dismissed_suggested_users[item]) + "</li>\n"

    html_string = html_string + "\t</ul>\n<hr>\n"

    return html_string

# reading media information and converting it to html string
def read_media(filename = "media.json"):

    html_string = "<h2 id=\"media\">Media</h2>\n\t<ul>\n"

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        f.close()

    stories = data["stories"]
    photos = data["photos"]
    profile = data["profile"]
    videos = data["videos"]
    direct = data["direct"]

    html_string = html_string + "<h3 id=\"stories\">Stories</h3>\n\t<ul>\n"

    if len(stories) == 0:
        html_string = html_string + "\t\t<li>None</li>\n"
    else:
        for item in stories:
            html_string = html_string + "\t\t<li>\n"

            if len(item["caption"]) == 0:
                caption = "None"
            else:
                caption = item["caption"]

            html_string = html_string + "\t\t\t<b>Caption:</b> " + str(caption) + "<br>\n\t\t\t<b>Taken at:</b> " + str(item["taken_at"]) + "<br>\n"

            if str(item["path"]).split(".")[-1] == "mp4":
                html_string = html_string + "\t\t\t<video controls>\n"
                html_string = html_string + "\t\t\t\t<source src=\"" + str(item["path"]) + "\" type=\"video/mp4\">\n"
                html_string = html_string + "\t\t\t</video>\n"
            else:
                html_string = html_string + "\t\t\t<img src=\"" + str(item["path"]) + "\" alt=\"Caption: " + str(caption).replace("\"", "'") + "\">\n"

            html_string = html_string + "\t\t</li>\n"

    html_string = html_string + "\t</ul>\n\n<h3 id=\"photos\">Photos</h3>\n\t<ul>\n"

    if len(photos) == 0:
        html_string = html_string + "\t\t<li>None</li>\n"
    else:
        for item in photos:
            html_string = html_string + "\t\t<li>\n"

            if len(item["caption"]) == 0:
                caption = "None"
            else:
                caption = item["caption"]

            html_string = html_string + "\t\t\t<b>Caption:</b> " + str(caption) + "<br>\n\t\t\t<b>Taken at:</b> " + str(item["taken_at"]) + "<br>\n"
            html_string = html_string + "\t\t\t<img src=\"" + str(item["path"]) + "\" alt=\"Caption: " + str(caption).replace("\"", "'") + "\">\n"

            html_string = html_string + "\t\t</li>\n"

    html_string = html_string + "\t</ul>\n\n<h3 id=\"pictures\">Profile Pictures</h3>\n\t<ul>\n"

    if len(profile) == 0:
        html_string = html_string + "\t\t<li>None</li>\n"
    else:
        for item in profile:
            html_string = html_string + "\t\t<li>\n"

            if len(item["caption"]) == 0:
                caption = "None"
            else:
                caption = item["caption"]

            html_string = html_string + "\t\t\t<b>Caption:</b> " + str(caption) + "<br>\n\t\t\t<b>Taken at:</b> " + str(item["taken_at"]) + "<br>\n"
            html_string = html_string + "\t\t\t<img src=\"" + str(item["path"]) + "\" alt=\"Caption: " + str(caption).replace("\"", "'") + "\">\n"

            html_string = html_string + "\t\t</li>\n"

    html_string = html_string + "\t</ul>\n\n<h3 id=\"videos\">Videos</h3>\n\t<ul>\n"

    if len(videos) == 0:
        html_string = html_string + "\t\t<li>None</li>\n"
    else:
        for item in videos:
            html_string = html_string + "\t\t<li>\n"

            if len(item["caption"]) == 0:
                caption = "None"
            else:
                caption = item["caption"]

            html_string = html_string + "\t\t\t<b>Caption:</b> " + str(caption) + "<br>\n\t\t\t<b>Taken at:</b> " + str(item["taken_at"]) + "<br>\n"

            html_string = html_string + "\t\t\t<video controls>\n"
            html_string = html_string + "\t\t\t\t<source src=\"" + str(item["path"]) + "\" type=\"video/mp4\">\n"
            html_string = html_string + "\t\t\t</video>\n"

            html_string = html_string + "\t\t</li>\n"

    html_string = html_string + "\t</ul>\n\n<h3 id=\"direct\">Direct Messages Media</h3>\n\t<ul>\n"

    if len(direct) == 0:
        html_string = html_string + "\t\t<li>None</li>\n"
    else:
        for item in direct:
            html_string = html_string + "\t\t<li>\n"

            html_string = html_string + "\t\t\t<b>Taken at:</b> " + str(item["taken_at"]) + "<br>\n"

            if str(item["path"]).split(".")[-1] == "mp4":
                html_string = html_string + "\t\t\t<video controls>\n"
                html_string = html_string + "\t\t\t\t<source src=\"" + str(item["path"]) + "\" type=\"video/mp4\">\n"
                html_string = html_string + "\t\t\t</video>\n"
            elif str(item["path"]).split(".")[-1] == "m4a":
                html_string = html_string + "\t\t\t<audio controls>\n"
                html_string = html_string + "\t\t\t\t<source src=\"" + str(item["path"]) + "\" type=\"audio/mpeg\">\n"
                html_string = html_string + "\t\t\t</audio>\n"
            else:
                html_string = html_string + "\t\t\t<img src=\"" + str(item["path"]) + "\" alt=\"Caption: " + str(caption).replace("\"", "'") + "\">\n"

            html_string = html_string + "\t\t</li>\n"

    html_string = html_string + "\t</ul>\n<hr>\n"

    return html_string

# reading comment information and converting it to html string
def read_comments(filename = "comments.json"):

    html_string = "<h2 id=\"comments\">Comments</h2>\n\t<ul>\n"

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        f.close()

    media_comments = data["media_comments"]
    live_comments = data["live_comments"]
    story_comments = data["story_comments"]

    html_string = html_string + "<h3 id=\"mediacomments\">Media Comments</h3>\n\t<ul>\n"

    if len(media_comments) == 0:
        html_string = html_string + "\t\t<li>None</li>\n"
    else:
        for item in media_comments:
            html_string = html_string + "\t\t<li>\n"
            html_string = html_string + "\t\t\t<b>Post Owner:</b> " + str(item[2]) + "<br>\n\t\t\t<b>Commented on:</b> " + str(item[0]) + "<br>\n\t\t\t<b>Comment:</b> " + str(item[1]) + "\n"
            html_string = html_string + "\t\t</li>\n"

    html_string = html_string + "\t</ul>\n\n<h3 id=\"livecomments\">Live Comments</h3>\n\t<ul>\n"

    try:
        if len(live_comments) == 0:
            html_string = html_string + "\t\t<li>None</li>\n"
        else:
            for item in live_comments:
                html_string = html_string + "\t\t<li>\n"
                html_string = html_string + "\t\t\t<b>Live Owner:</b> " + str(item[2]) + "<br>\n\t\t\t<b>Commented on:</b> " + str(item[0]) + "<br>\n\t\t\t<b>Comment:</b> " + str(item[1]) + "\n"
                html_string = html_string + "\t\t</li>\n"
    except:
        pass

    html_string = html_string + "\t</ul>\n\n<h3 id=\"storycomments\">Story Comments</h3>\n\t<ul>\n"

    try:
        if len(story_comments) == 0:
            html_string = html_string + "\t\t<li>None</li>\n"
        else:
            for item in story_comments:
                html_string = html_string + "\t\t<li>\n"
                html_string = html_string + "\t\t\t<b>Story Owner:</b> " + str(item[2]) + "<br>\n\t\t\t<b>Commented on:</b> " + str(item[0]) + "<br>\n\t\t\t<b>Comment:</b> " + str(item[1]) + "\n"
                html_string = html_string + "\t\t</li>\n"
    except:
        pass

    html_string = html_string + "\t</ul>\n<hr>\n"

    return html_string

# reading message information and converting it to html string (only links)
# also creates "chat" subdirectory in current directory
# creates chat html pages in "chat" subdirectory
# for args refer to README.md
# there are no input checks, incorrect inputs will lead to crashes!
# so be careful if you don't want things to go sideways
def read_messages(filename = "messages.json", profile = "profile.json", use_default = True, default_avatar = "DEFAULT", hd = False):

    try:
        os.mkdir("chat")
    except Exception as e:
        print("ERROR creating directory 'chat'!")
        print(e)

    chat_list = []

    html_string = "<h2 id=\"messages\">Messages</h2>\n\n<ul>\n"

    with open(profile, "r", encoding="utf-8") as f:
        data = json.load(f)
        f.close()

    username = str(data["username"])

    if not use_default and default_avatar != "DEFAULT":
        profile_pic_url = str(default_avatar)
    else:
        profile_pic_url = str(data["profile_pic_url"])

    def get_avatar(username, default = profile_pic_url, hd = hd):

        ig_url = "https://instagram.com/" + username + "/?__a=1"
        try:
            data = ur.urlopen(ig_url).read()
            json_data = json.loads(data)
            if hd:
                avatar = str(json_data["graphql"]["user"]["profile_pic_url_hd"])
            else:
                avatar = str(json_data["graphql"]["user"]["profile_pic_url"])
        except Exception as e:
            avatar = default
            print("WARNING - error getting avatar!")
            print(e)

        return avatar

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        f.close()

    for item in data:
        participants = item["participants"]

        # getting avatars might not work if u send to many requests to instagram
        # if avatars are not shown correctly in chat, run script again at a different time
        # or change IP address if u can
        avatars = {}
        for participant in participants:
            avatars[participant] = str(get_avatar(participant))

        chat_list.append(participants)

        conversation = item["conversation"]

        html_chat_string = "<h3 id=\"" + str("".join(participants)) + "\">" + str(", ".join(participants)) + "</h3>\n\n"

        for message in conversation:
            if message["sender"] == username:
                html_chat_string = html_chat_string + "<div class=\"container darker\">\n"
                html_chat_string = html_chat_string + "\t<img src=\"" + str(avatars[message["sender"]]) + "\" alt=\"" + str(message["sender"]).upper() + "\" class=\"right\" style=\"width:100%;\">\n"
            else:
                html_chat_string = html_chat_string + "<div class=\"container\">\n"
                html_chat_string = html_chat_string + "\t<img src=\"" + str(avatars[message["sender"]]) + "\" alt=\"" + str(message["sender"]).upper() + "\" class=\"left\" style=\"width:100%;\">\n"

            if "media_share_url" in message:
                content = "\t<p>\n\t\t<img src=\"" + str(message["media_share_url"]) + "\"IMAGE\">\n\t\t<br>\n\t\t<b>Media Owner:</b> " + str(message["media_owner"]) + "<br>\n"
                content = content + "\t\t<b>Media Caption:</b> " + str(message["media_share_caption"]) + "<br>\n"
                if "text" in message:
                    content = content + "\t\t<br><b>Text:</b> " + str(message["text"]) + "\n"
                html_chat_string = html_chat_string + content + "\t</p>\n"
            elif "voice_media" in message:
                if message["voice_media"] == "Media unavailable.":
                    content = "\t<p>\n\t\t<b>Voice Message:</b> Media unavailable.<br>\n"
                else:
                    content = "\t<p>\n\t\t<b>Voice Message:</b>\n\t\t<br>\n\t\t\t<audio controls>\n\t\t\t\t<source src=\""
                    content = content + str(message["voice_media"]) + "\" type=\"audio/mpeg\">\n\t\t\t</audio>\n\t\t<br>\n"
                if "text" in message:
                    content = content + "\t\t<br><b>Text:</b> " + str(message["text"]) + "\n"
                html_chat_string = html_chat_string + content + "\t</p>\n"
            elif "media" in message:
                if message["media"].split("?")[0].split(".")[-1] == "mp4":
                    content = "\t<p>\n\t\t<b>Video:</b>\n\t\t<br>\n\t\t\t<video controls>\n\t\t\t\t<source src=\""
                    content = content + str(message["media"]) + "\" type=\"video/mp4\">\n\t\t\t</video>\n\t\t<br>\n"
                elif message["media"].split("?")[0].split(".")[-1] == "m4a":
                    content = "\t<p>\n\t\t<b>Voice Message:</b>\n\t\t<br>\n\t\t\t<audio controls>\n\t\t\t\t<source src=\""
                    content = content + str(message["media"]) + "\" type=\"audio/mpeg\">\n\t\t\t</audio>\n\t\t<br>\n"
                else:
                    content = "\t<p>\n\t\t<b>Image:</b>\n\t\t<br>\n\t\t\t<img src=\"" + str(message["media"]) + "\" alt=\""
                    content = content + str(message["media"]) + "\">\n\t\t<br>\n"
                if "text" in message:
                    content = content + "\t\t<br><b>Text:</b> " + str(message["text"]) + "\n"
                html_chat_string = html_chat_string + content + "\t</p>\n"
            elif "story_share" in message:
                content = "\t<p>\n\t\t<b>Story Share:</b> " + str(message["story_share"]) + "<br>\n"
                if "text" in message:
                    content = content + "\t\t<br><b>Text:</b> " + str(message["text"]) + "\n"
                html_chat_string = html_chat_string + content + "\t</p>\n"
            elif "link" in message:
                content = "\t<p>\n\t\t<b>Link:</b> <a href=\"" + str(message["link"]) + "\"> " + str(message["link"]) + "</a><br>\n"
                if "text" in message:
                    content = content + "\t\t<br><b>Text:</b> " + str(message["text"]) + "\n"
                html_chat_string = html_chat_string + content + "\t</p>\n"
            else:
                if "text" in message:
                    content = "\t<p>\n\t\t<b>Text:</b> " + str(message["text"]) + "\n"
                else:
                    content = "\t<p>\n"
                html_chat_string = html_chat_string + content + "\t</p>\n"

            if message["sender"] == username:
                html_chat_string = html_chat_string + "\t<span class=\"time-left\">" + str(message["created_at"]) + "</span>\n</div>\n\n"
            else:
                html_chat_string = html_chat_string + "\t<span class=\"time-right\">" + str(message["created_at"]) + "</span>\n</div>\n\n"

        html_chat_string = html_chat_string + "<hr>\n"
        ext_filename = "chat/" + str(len(chat_list)) + ".html"
        with open(ext_filename, "w", encoding="utf-8") as f:
            content = html_template + "<h2 id=\"messages\">Messages</h2>\n\n" + html_chat_string + "</body></html>"
            f.write(content)
            f.close()
        html_string = html_string + "<li><a href=\"" + str(ext_filename) + "\" target=\"_blank\">" + str(", ".join(participants)) + "</a></li>\n"

    html_string = html_string + "</ul>\n"

    return [html_string, chat_list]

# main function = executes all previous functions and concatenates html string to html file
# title can be changed as title = "<h1>YOUR TITLE HERE</h1>\n" (should be html)
# for args refer to README.md again
# needless to say that there are no input checks here either, incorrect inputs will lead to crashes!
# so be careful if you don't want things to go sideways
def instaview(default_filenames = True, filenames = ["profile.json", "searches.json", "connections.json", "media.json", "comments.json", "messages.json"], title = "", show_credits = True, **kwargs):

    result = 0

    if title == "":
        title = "<h1>INSTAGRAM DATA [" + str(datetime.datetime.today().strftime('%Y-%m-%d'))+ "]</h1>\n"

    if default_filenames:
        try:
            chat_string, chat_list = read_messages(**kwargs)
        except Exception as e:
            chat_string, chat_list = ["", []]
            result = result + 32
            print("ERROR reading messages!")
            print(e)

        if show_credits:
            sidebar = sidebar_template + "\t<a href=\"#credits\">Credits</a>\n</div>\n"
        else:
            sidebar = sidebar_template + "</div>\n"

        end_html = "\n</div>\n</body>\n</html>"

        try:
            a = read_profile()
        except Exception as e:
            a = ""
            result = result + 1
            print("ERROR reading profile!")
            print(e)
        try:
            b = read_searches()
        except Exception as e:
            b = ""
            result = result + 2
            print("ERROR reading searches!")
            print(e)
        try:
            c = read_connections()
        except Exception as e:
            c = ""
            result = result + 4
            print("ERROR reading connections!")
            print(e)
        try:
            d = read_media()
        except Exception as e:
            d = ""
            result = result + 8
            print("ERROR reading media!")
            print(e)
        try:
            e = read_comments()
        except Exception as e:
            e = ""
            result = result + 16
            print("ERROR reading comments!")
            print(e)

        if show_credits:
            complete_html = html_template + sidebar + "<div class=\"main\">\n\n" + title + a + b + c + d + e + chat_string + credits + end_html
        else:
            complete_html = html_template + sidebar + "<div class=\"main\">\n\n" + title + a + b + c + d + e + chat_string + end_html

        with open("instaview_report.html", "w", encoding="utf-8") as f:
            f.write(complete_html)
            f.close()

    else:
        try:
            chat_string, chat_list = read_messages(filename = filenames[5], **kwargs)
        except Exception as e:
            chat_string, chat_list = ["", []]
            result = result + 32
            print("ERROR reading messages!")
            print(e)

        if show_credits:
            sidebar = sidebar_template + "\t<a href=\"#credits\">Credits</a>\n</div>\n"
        else:
            sidebar = sidebar_template + "</div>\n"

        end_html = "\n</div>\n</body>\n</html>"

        try:
            a = read_profile(filenames[0])
        except Exception as e:
            a = ""
            result = result + 1
            print("ERROR reading profile!")
            print(e)
        try:
            b = read_searches(filenames[1])
        except Exception as e:
            b = ""
            result = result + 2
            print("ERROR reading searches!")
            print(e)
        try:
            c = read_connections(filenames[2])
        except Exception as e:
            c = ""
            result = result + 4
            print("ERROR reading connections!")
            print(e)
        try:
            d = read_media(filenames[3])
        except Exception as e:
            d = ""
            result = result + 8
            print("ERROR reading media!")
            print(e)
        try:
            e = read_comments(filenames[4])
        except Exception as e:
            e = ""
            result = result + 16
            print("ERROR reading comments!")
            print(e)

        if show_credits:
            complete_html = html_template + sidebar + "<div class=\"main\">\n\n" + title + a + b + c + d + e + chat_string + credits + end_html
        else:
            complete_html = html_template + sidebar + "<div class=\"main\">\n\n" + title + a + b + c + d + e + chat_string + end_html

        with open("instaview_report.html", "w", encoding="utf-8") as f:
            f.write(complete_html)
            f.close()

    return result

if __name__ == '__main__':
    # functions are run with default args when script is executed
    # this should terminate succesfully if script is in the right directory 
    instaview()
