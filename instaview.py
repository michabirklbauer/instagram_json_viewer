#!/usr/bin/env python3

# INSTAGRAM JSON VIEWER
# 2020 (c) Micha Johannes Birklbauer
# https://github.com/t0xic-m/
# micha.birklbauer@gmail.com

import urllib.request as ur
import traceback as tb
import datetime
import time
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
    <meta charset="utf-8">
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
    <a href="#devices">Devices</a>

"""

# patting myself on the shoulder for this one uwu
credits = \
"""
<h2 id="credits">Credits</h2>

    <p>
        Report created with Micha Birklbauer's <a href="https://github.com/t0xic-m/instagram_json_viewer">Instagram JSON Viewer</a>.
    </p>
"""

# reading profile information and converting it to html string
# default filenames and arguments should be fine for all functions if script is in the right directory
def read_profile(filename = "profile.json"):

    # error controls and logging
    status = 0
    errors = []

    # html template
    html_string = "<h2 id=\"profile\">Profile Information</h2>\n\t<ul>\n"

    # json to html conversion
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            f.close()

        for item in data:
            html_string = html_string + "\t\t<li><b>" + str(item) + ":</b> " + str(data[item]) + "</li>\n"
    except Exception as e:
        print("ERROR reading profile!")
        tb.print_exc()
        errors.append(str(repr(e)))
        errors.append("Detailed Traceback:")
        errors.append(tb.format_exc())
        status = status + 1

    html_string = html_string + "\t</ul>\n<hr>\n"

    # creating an error log for file output
    error_log = "Encountered errors reading profile: " + str(status) + "\nError messages:\n" + str("\n".join(errors)) + "\n\n"

    return [html_string, status, error_log]

# reading search information and converting it to html string
def read_searches(filename = "searches.json"):

    # error controls and logging
    status = 0
    errors = []

    # html template
    html_string = "<h2 id=\"searches\">Searches</h2>\n"

    # json to html conversion
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            f.close()

        main_search = data["main_search_history"]
        shopping_search = data["shopping_search_history"]

        html_string = html_string + "\t<h3>Profile Searches</h3>\n\t\t<ul>\n"

        counter = 1
        for item in main_search:
            if item == "You have no data in this section":
                html_string = html_string + "\t\t\t<li>You have no data in this section.</li>\n"
                break
            html_string = html_string + "\t\t\t<li><b>Search " + str(counter) + ":</b>\n\t\t\t\t<ul>\n"
            for subitem in item:
                html_string = html_string + "\t\t\t\t\t<li><b>" + str(subitem) + ":</b> " + str(item[subitem]) + "</li>\n"
            html_string = html_string + "\t\t\t\t</ul>\n\t\t\t</li>\n"
            counter = counter + 1

        html_string = html_string + "\t\t</ul>\n\t<h3>Shopping Searches</h3>\n\t\t<ul>\n"

        counter = 1
        for item in shopping_search:
            if item == "You have no data in this section":
                html_string = html_string + "\t\t\t<li>You have no data in this section.</li>\n"
                break
            html_string = html_string + "\t\t\t<li><b>Search " + str(counter) + ":</b>\n\t\t\t\t<ul>\n"
            for subitem in item:
                html_string = html_string + "\t\t\t\t\t<li><b>" + str(subitem) + ":</b> " + str(item[subitem]) + "</li>\n"
            html_string = html_string + "\t\t\t\t</ul>\n\t\t\t</li>\n"
            counter = counter + 1
    except Exception as e:
        print("ERROR reading searches!")
        tb.print_exc()
        errors.append(str(repr(e)))
        errors.append("Detailed Traceback:")
        errors.append(tb.format_exc())
        status = status + 1

    html_string = html_string + "\t\t</ul>\n<hr>\n"

    # creating an error log for file output
    error_log = "Encountered errors reading searches: " + str(status) + "\nError messages:\n" + str("\n".join(errors)) + "\n\n"

    return [html_string, status, error_log]

# reading connection information and converting it to html string
def read_connections(filename = "connections.json"):

    # error controls and logging
    status = 0
    errors = []

    # html template
    html_string = "<h2 id=\"connections\">Profile Connections</h2>\n\t<ul>\n"

    # json to html conversion
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            f.close()

        # blocked users
        try:
            blocked_users = data["blocked_users"]

            html_string = html_string + "<h3>Blocked Users</h3>\n\t<ul>\n"

            if len(blocked_users) == 0:
                html_string = html_string + "\t\t<li>None</li>\n"
            else:
                for item in blocked_users:
                    html_string = html_string + "\t\t<li>" + str(item) + " <b>blocked since</b> " + str(blocked_users[item]) + "</li>\n"
        except Exception as e:
            print("ERROR reading blocked_users!")
            tb.print_exc()
            errors.append(str(repr(e)))
            errors.append("Detailed Traceback:")
            errors.append(tb.format_exc())
            status = status + 1

        # restriced users
        try:
            restricted_users = data["restricted_users"]

            html_string = html_string + "\t</ul>\n\n<h3>Restricted Users</h3>\n\t<ul>\n"

            if len(restricted_users) == 0:
                html_string = html_string + "\t\t<li>None</li>\n"
            else:
                for item in restricted_users:
                    html_string = html_string + "\t\t<li>" + str(item) + " <b>restricted since</b> " + str(restricted_users[item]) + "</li>\n"
        except Exception as e:
            print("ERROR reading restricted_users!")
            tb.print_exc()
            errors.append(str(repr(e)))
            errors.append("Detailed Traceback:")
            errors.append(tb.format_exc())
            status = status + 1

        # follow requests sent
        try:
            follow_requests_sent = data["follow_requests_sent"]

            html_string = html_string + "\t</ul>\n\n<h3>Requested Following</h3>\n\t<ul>\n"

            if len(follow_requests_sent) == 0:
                html_string = html_string + "\t\t<li>None</li>\n"
            else:
                for item in follow_requests_sent:
                    html_string = html_string + "\t\t<li>" + str(item) + " <b>request sent</b> " + str(follow_requests_sent[item]) + "</li>\n"
        except Exception as e:
            print("ERROR reading follow_requests_sent!")
            tb.print_exc()
            errors.append(str(repr(e)))
            errors.append("Detailed Traceback:")
            errors.append(tb.format_exc())
            status = status + 1

        # following
        try:
            following = data["following"]

            html_string = html_string + "\t</ul>\n\n<h3>Following Users</h3>\n\t<ul>\n"

            if len(following) == 0:
                html_string = html_string + "\t\t<li>None</li>\n"
            else:
                for item in following:
                    html_string = html_string + "\t\t<li>" + str(item) + " <b>followed since</b> " + str(following[item]) + "</li>\n"
        except Exception as e:
            print("ERROR reading following!")
            tb.print_exc()
            errors.append(str(repr(e)))
            errors.append("Detailed Traceback:")
            errors.append(tb.format_exc())
            status = status + 1

        # followers
        try:
            followers = data["followers"]

            html_string = html_string + "\t</ul>\n\n<h3>Followers</h3>\n\t<ul>\n"

            if len(followers) == 0:
                html_string = html_string + "\t\t<li>None</li>\n"
            else:
                for item in followers:
                    html_string = html_string + "\t\t<li>" + str(item) + " <b>has followed since</b> " + str(followers[item]) + "</li>\n"
        except Exception as e:
            print("ERROR reading followers!")
            tb.print_exc()
            errors.append(str(repr(e)))
            errors.append("Detailed Traceback:")
            errors.append(tb.format_exc())
            status = status + 1

        # following hashtags
        try:
            following_hashtags = data["following_hashtags"]

            html_string = html_string + "\t</ul>\n\n<h3>Following Hashtags</h3>\n\t<ul>\n"

            if len(following_hashtags) == 0:
                html_string = html_string + "\t\t<li>None</li>\n"
            else:
                for item in following_hashtags:
                    html_string = html_string + "\t\t<li>" + str(item) + " <b>followed since</b> " + str(following_hashtags[item]) + "</li>\n"
        except Exception as e:
            print("ERROR reading following_hashtags!")
            tb.print_exc()
            errors.append(str(repr(e)))
            errors.append("Detailed Traceback:")
            errors.append(tb.format_exc())
            status = status + 1

        # dismissed suggested users
        try:
            dismissed_suggested_users = data["dismissed_suggested_users"]

            html_string = html_string + "\t</ul>\n\n<h3>Dismissed Suggested Users</h3>\n\t<ul>\n"

            if len(dismissed_suggested_users) == 0:
                html_string = html_string + "\t\t<li>None</li>\n"
            else:
                for item in dismissed_suggested_users:
                    html_string = html_string + "\t\t<li>" + str(item) + " <b>dismissed on</b> " + str(dismissed_suggested_users[item]) + "</li>\n"
        except Exception as e:
            print("ERROR reading dismissed_suggested_users!")
            tb.print_exc()
            errors.append(str(repr(e)))
            errors.append("Detailed Traceback:")
            errors.append(tb.format_exc())
            status = status + 1
    except Exception as e:
        print("ERROR reading connections!")
        tb.print_exc()
        errors.append(str(repr(e)))
        errors.append("Detailed Traceback:")
        errors.append(tb.format_exc())
        status = status + 1000

    html_string = html_string + "\t</ul>\n<hr>\n"

    # creating an error log for file output
    error_log = "Encountered errors reading connections: " + str(status) + "\nError messages:\n" + str("\n".join(errors)) + "\n\n"

    return [html_string, status, error_log]

# reading media information and converting it to html string
def read_media(filename = "media.json"):

    # error controls and logging
    status = 0
    errors = []

    # html template
    html_string = "<h2 id=\"media\">Media</h2>\n\t<ul>\n"

    # json to html conversion
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            f.close()

        # stories
        try:
            stories = data["stories"]

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
        except Exception as e:
            print("ERROR reading stories media!")
            tb.print_exc()
            errors.append(str(repr(e)))
            errors.append("Detailed Traceback:")
            errors.append(tb.format_exc())
            status = status + 1

        # photos
        try:
            photos = data["photos"]

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
        except Exception as e:
            print("ERROR reading photos media!")
            tb.print_exc()
            errors.append(str(repr(e)))
            errors.append("Detailed Traceback:")
            errors.append(tb.format_exc())
            status = status + 1

        # profile
        try:
            profile = data["profile"]

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
        except Exception as e:
            print("ERROR reading profile media!")
            tb.print_exc()
            errors.append(str(repr(e)))
            errors.append("Detailed Traceback:")
            errors.append(tb.format_exc())
            status = status + 1

        # videos
        try:
            videos = data["videos"]

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
        except Exception as e:
            print("ERROR reading video media!")
            tb.print_exc()
            errors.append(str(repr(e)))
            errors.append("Detailed Traceback:")
            errors.append(tb.format_exc())
            status = status + 1

        # direct
        try:
            direct = data["direct"]

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
        except Exception as e:
            print("ERROR reading direct media!")
            tb.print_exc()
            errors.append(str(repr(e)))
            errors.append("Detailed Traceback:")
            errors.append(tb.format_exc())
            status = status + 1
    except Exception as e:
        print("ERROR reading media!")
        tb.print_exc()
        errors.append(str(repr(e)))
        errors.append("Detailed Traceback:")
        errors.append(tb.format_exc())
        status = status + 1000

    html_string = html_string + "\t</ul>\n<hr>\n"

    # creating an error log for file output
    error_log = "Encountered errors reading media: " + str(status) + "\nError messages:\n" + str("\n".join(errors)) + "\n\n"

    return [html_string, status, error_log]

# reading comment information and converting it to html string
def read_comments(filename = "comments.json"):

    # error controls and logging
    status = 0
    errors = []

    # html template
    html_string = "<h2 id=\"comments\">Comments</h2>\n\t<ul>\n"

    # json to html conversion
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            f.close()

        # media comments
        try:
            media_comments = data["media_comments"]

            html_string = html_string + "<h3 id=\"mediacomments\">Media Comments</h3>\n\t<ul>\n"

            if len(media_comments) == 0:
                html_string = html_string + "\t\t<li>None</li>\n"
            else:
                for item in media_comments:
                    html_string = html_string + "\t\t<li>\n"
                    html_string = html_string + "\t\t\t<b>Post Owner:</b> " + str(item[2]) + "<br>\n\t\t\t<b>Commented on:</b> " + str(item[0]) + "<br>\n\t\t\t<b>Comment:</b> " + str(item[1]) + "\n"
                    html_string = html_string + "\t\t</li>\n"
        except Exception as e:
            print("ERROR reading media comments!")
            tb.print_exc()
            errors.append(str(repr(e)))
            errors.append("Detailed Traceback:")
            errors.append(tb.format_exc())
            status = status + 1

        # live comments
        try:
            live_comments = data["live_comments"]

            html_string = html_string + "\t</ul>\n\n<h3 id=\"livecomments\">Live Comments</h3>\n\t<ul>\n"

            # this is rather experimental because I had no live comments available
            try:
                if len(live_comments) == 0:
                    html_string = html_string + "\t\t<li>None</li>\n"
                else:
                    for item in live_comments:
                        html_string = html_string + "\t\t<li>\n"
                        html_string = html_string + "\t\t\t<b>Live Owner:</b> " + str(item[2]) + "<br>\n\t\t\t<b>Commented on:</b> " + str(item[0]) + "<br>\n\t\t\t<b>Comment:</b> " + str(item[1]) + "\n"
                        html_string = html_string + "\t\t</li>\n"
            except Exception as e:
                print(e)
                pass
        except Exception as e:
            print("ERROR reading live comments!")
            tb.print_exc()
            errors.append(str(repr(e)))
            errors.append("Detailed Traceback:")
            errors.append(tb.format_exc())
            status = status + 1

        # story comments
        try:
            story_comments = data["story_comments"]

            html_string = html_string + "\t</ul>\n\n<h3 id=\"storycomments\">Story Comments</h3>\n\t<ul>\n"

            # this is rather experimental because I had no story comments available
            try:
                if len(story_comments) == 0:
                    html_string = html_string + "\t\t<li>None</li>\n"
                else:
                    for item in story_comments:
                        html_string = html_string + "\t\t<li>\n"
                        html_string = html_string + "\t\t\t<b>Story Owner:</b> " + str(item[2]) + "<br>\n\t\t\t<b>Commented on:</b> " + str(item[0]) + "<br>\n\t\t\t<b>Comment:</b> " + str(item[1]) + "\n"
                        html_string = html_string + "\t\t</li>\n"
            except Exception as e:
                print(repr(e))
                pass
        except Exception as e:
            print("ERROR reading story comments!")
            tb.print_exc()
            errors.append(str(repr(e)))
            errors.append("Detailed Traceback:")
            errors.append(tb.format_exc())
            status = status + 1
    except Exception as e:
        print("ERROR reading comments!")
        tb.print_exc()
        errors.append(str(repr(e)))
        errors.append("Detailed Traceback:")
        errors.append(tb.format_exc())
        status = status + 1000

    html_string = html_string + "\t</ul>\n<hr>\n"

    # creating an error log for file output
    error_log = "Encountered errors reading comments: " + str(status) + "\nError messages:\n" + str("\n".join(errors)) + "\n\n"

    return [html_string, status, error_log]

# helper function to generate a messages json file from a directory
# dirname is the directory that stores the split message_*.json files
def generate_messages_json(dirname = "messages"):

    if not os.path.isdir(dirname):
        print("ERROR - Specified directory does not exist", dirname)
        return 1

    try:
        messages_json = []

        for dirpath, dirnames, filenames in os.walk(dirname):
            for fname in filenames:
                if fname.endswith(".json"):
                    with open(os.path.join(dirpath, fname), "r", encoding="utf-8") as f:
                        data = json.load(f)
                        f.close()
                    messages_json.append(data)

        filename = dirname + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(messages_json, f)
            f.close()

        return 0
    except Exception as e:
        print("ERROR creating specified messages JSON file!")
        print(repr(e))
        print("Detailed Traceback:")
        tb.print_exc()
        return 1

# this is a debug function to reversely generate a messages-folder-like structure
# for testing purposes
def reverse_generate_messages_json(filename = "messages.json"):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        f.close()

    for item in data:
        dirname = "messages/inbox/"+", ".join(item["participants"])
        print(dirname)
        try:
            os.mkdir(dirname)
        except Exception:
            tb.print_exc()
        with open(dirname+"/message_1.json", "w", encoding="utf-8") as f:
            json.dump(item, f)

# reading message information and converting it to html string (only links)
# also creates "chat" subdirectory in current directory
# creates chat html pages in "chat" subdirectory
# for args refer to README.md
# there are no input checks, incorrect inputs will lead to crashes!
# so be careful if you don't want things to go sideways
def read_messages(filename = "messages.json", profile = "profile.json", reverse_conversations = False, profile_pic = None, default_avatar = None, download_all = False, hd = False, avatars_dict = {}, http_traceback = False):

    # generate messages.json (or specified messages json file) if not present on
    # the current file tree
    if not os.path.isfile(filename):
        mjson_status = generate_messages_json(filename.split(".")[0])
        if mjson_status != 0:
            print("WARNING - Generating", filename, "was unsuccessful! Trying to continue...")

    # error controls and logging
    status = 0
    errors = []
    # logging errors in conversations
    conv_errors = []

    # creating chat directory
    try:
        os.mkdir("chat")
    except Exception as e:
        print("ERROR creating directory 'chat'!")
        print(repr(e))
        print("Detailed Traceback:")
        tb.print_exc()

    # creating icons directory
    try:
        os.mkdir("chat/icons")
    except Exception as e:
        print("ERROR creating directory 'chat/icons'!")
        print(repr(e))
        print("Detailed Traceback:")
        tb.print_exc()

    # creating media directory if media is downloaded
    if download_all:
        try:
            os.mkdir("chat/media")
        except Exception as e:
            print("ERROR creating directory 'chat/icons'!")
            print(repr(e))
            print("Detailed Traceback:")
            tb.print_exc()

    chat_list = []

    # html template
    html_string = "<h2 id=\"messages\">Messages</h2>\n\n<ul>\n"

    # reading self username from profile.json
    with open(profile, "r", encoding="utf-8") as f:
        data = json.load(f)
        f.close()

    user_username = str(data["username"])

    # setting a default avatar if None is provided
    if default_avatar is not None:
        default_avatar = str(default_avatar)
    else:
        if hd:
            default_avatar = "https://raw.githubusercontent.com/t0xic-m/instagram_json_viewer/master/icons/icon_hd.jpg"
        else:
            default_avatar = "https://raw.githubusercontent.com/t0xic-m/instagram_json_viewer/master/icons/icon.jpg"

    # setting self profile picture if None is provided
    if profile_pic is None:
        try:
            pp_list = os.listdir("profile")
            pp_last = pp_list[-1]
            pp_pics = os.listdir(("profile/" + str(pp_last)))
            pp_pic = pp_pics[-1]
            profile_pic = "../profile/" + str(pp_last) + "/" + str(pp_pic)
        except Exception as e:
            print(repr(e))
            print("ERROR fetching profile picture locally!")
            print("Trying to fetch online...")
            errors.append(str(repr(e)))
            errors.append("Detailed Traceback:")
            errors.append(tb.format_exc())
            status = status + 1
            try:
                ig_url = "https://instagram.com/" + user_username + "/?__a=1"
                request_header = { "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64)" }
                request = ur.Request(ig_url, headers=request_header)
                data = ur.urlopen(request).read()
                json_data = json.loads(data)
                if hd:
                    profile_pic_url = str(json_data["graphql"]["user"]["profile_pic_url_hd"])
                    file_name = "chat/icons/" + str(profile_pic_url).split("/")[-1].split("?")[0]
                    ur.urlretrieve(str(profile_pic_url), file_name)
                    profile_pic = "icons/" + str(profile_pic_url).split("/")[-1].split("?")[0]
                else:
                    profile_pic_url = str(json_data["graphql"]["user"]["profile_pic_url"])
                    file_name = "chat/icons/" + str(profile_pic_url).split("/")[-1].split("?")[0]
                    ur.urlretrieve(str(profile_pic_url), file_name)
                    profile_pic = "icons/" + str(profile_pic_url).split("/")[-1].split("?")[0]
            except Exception as e:
                print(repr(e))
                print("ERROR fetching profile picture online!")
                print("Profile picture set to default avatar!")
                errors.append(str(repr(e)))
                errors.append("Detailed Traceback:")
                errors.append(tb.format_exc())
                status = status + 1
                profile_pic = default_avatar

    # function to fetch avatar for given username
    def get_avatar(username, profile_pic = profile_pic, default = default_avatar, hd = hd, http_traceback = http_traceback):

        if str(username) == user_username:
            return profile_pic
        else:
            ig_url = "https://instagram.com/" + username + "/?__a=1"
            try:
                request_header = { "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64)" }
                request = ur.Request(ig_url, headers=request_header)
                data = ur.urlopen(request).read()
                json_data = json.loads(data)
                if hd:
                    avatar_url = str(json_data["graphql"]["user"]["profile_pic_url_hd"])
                    file_name = "chat/icons/" + str(username) + ".jpg"
                    ur.urlretrieve(str(avatar_url), file_name)
                    avatar = "icons/" + str(username) + ".jpg"
                else:
                    avatar_url = str(json_data["graphql"]["user"]["profile_pic_url"])
                    file_name = "chat/icons/" + str(username) + ".jpg"
                    ur.urlretrieve(str(avatar_url), file_name)
                    avatar = "icons/" + str(username) + ".jpg"
            except Exception as e:
                try:
                    avatar_url = default
                    file_name = "chat/icons/" + str(username) + ".jpg"
                    ur.urlretrieve(str(avatar_url), file_name)
                    avatar = "icons/" + str(username) + ".jpg"
                except:
                    print("INFO: Downloading of default avatar was unsuccessful! Avatar is still set!")
                    avatar = default
                print(("WARNING - error getting avatar for user " + str(username) + "!\n Set to default!"))
                print(repr(e))
                if http_traceback:
                    print("Detailed Traceback:")
                    tb.print_exc()
            return avatar

    # save media locally if possible
    def get_media(media_share_url, download_all = download_all):

        if download_all:
            try:
                file_name = "chat/media/" + str(media_share_url).split("/")[-1].split("?")[0]
                ur.urlretrieve(str(media_share_url), file_name)
                media = "media/" + str(media_share_url).split("/")[-1].split("?")[0]
                return str(media)
            except:
                return str(media_share_url)
        else:
            return str(media_share_url)

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        f.close()

    avatars = avatars_dict
    avatars[user_username] = profile_pic

    for item in data:
        participants = item["participants"]

        try:
            # getting avatars might not work if u send to many requests to instagram
            # if avatars are not shown correctly in chat, run script again at a different time
            # or change IP address if u can
            for participant in participants:
                if participant not in avatars:
                    avatars[participant] = str(get_avatar(participant))

            chat_list.append(participants)

            if reverse_conversations:
                conversation = reversed(item["conversation"])
            else:
                conversation = item["conversation"]

            html_chat_string = "<h3 id=\"" + str("".join(participants)) + "\">" + str(", ".join(participants)) + "</h3>\n\n"

            for message in conversation:
                if message["sender"] == user_username:
                    html_chat_string = html_chat_string + "<div class=\"container darker\">\n"
                    html_chat_string = html_chat_string + "\t<img src=\"" + str(avatars[message["sender"]]) + "\" alt=\"" + str(message["sender"]).upper() + "\" class=\"right\" style=\"width:100%;\">\n"
                else:
                    html_chat_string = html_chat_string + "<div class=\"container\">\n"
                    html_chat_string = html_chat_string + "\t<img src=\"" + str(avatars[message["sender"]]) + "\" alt=\"" + str(message["sender"]).upper() + "\" class=\"left\" style=\"width:100%;\">\n"

                if "media_share_url" in message:
                    content = "\t<p>\n\t\t<img src=\"" + get_media(message["media_share_url"]) + "\"IMAGE\">\n\t\t<br>\n\t\t<b>Media Owner:</b> " + str(message["media_owner"]) + "<br>\n"
                    content = content + "\t\t<b>Media Caption:</b> " + str(message["media_share_caption"]) + "<br>\n"
                    if "text" in message:
                        content = content + "\t\t<br><b>Text:</b> " + str(message["text"]) + "\n"
                    html_chat_string = html_chat_string + content + "\t</p>\n"
                elif "voice_media" in message:
                    if message["voice_media"] == "Media unavailable.":
                        content = "\t<p>\n\t\t<b>Voice Message:</b> Media unavailable.<br>\n"
                    else:
                        content = "\t<p>\n\t\t<b>Voice Message:</b>\n\t\t<br>\n\t\t\t<audio controls>\n\t\t\t\t<source src=\""
                        content = content + get_media(message["voice_media"]) + "\" type=\"audio/mpeg\">\n\t\t\t</audio>\n\t\t<br>\n"
                    if "text" in message:
                        content = content + "\t\t<br><b>Text:</b> " + str(message["text"]) + "\n"
                    html_chat_string = html_chat_string + content + "\t</p>\n"
                elif "media" in message:
                    if message["media"].split("?")[0].split(".")[-1] == "mp4":
                        content = "\t<p>\n\t\t<b>Video:</b>\n\t\t<br>\n\t\t\t<video controls>\n\t\t\t\t<source src=\""
                        content = content + get_media(message["media"]) + "\" type=\"video/mp4\">\n\t\t\t</video>\n\t\t<br>\n"
                    elif message["media"].split("?")[0].split(".")[-1] == "m4a":
                        content = "\t<p>\n\t\t<b>Voice Message:</b>\n\t\t<br>\n\t\t\t<audio controls>\n\t\t\t\t<source src=\""
                        content = content + get_media(message["media"]) + "\" type=\"audio/mpeg\">\n\t\t\t</audio>\n\t\t<br>\n"
                    else:
                        content = "\t<p>\n\t\t<b>Image:</b>\n\t\t<br>\n\t\t\t<img src=\"" + get_media(message["media"]) + "\" alt=\""
                        content = content + get_media(message["media"]) + "\">\n\t\t<br>\n"
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

                if message["sender"] == user_username:
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
        except Exception as e:
            print("ERROR reading messages!")
            # this prevents the script from crashing when participants is not an appropriate list
            try:
                print("Affected conversion: ", str(", ".join(participants)))
                conv_errors.append(str(", ".join(participants)))
            except Exception as e:
                print("WARNING - Error for participants cannot be displayed, participants not in right format!")
                print("Participants:")
                print(participants)
                tb.print_exc()
            tb.print_exc()
            errors.append(str(repr(e)))
            errors.append("Detailed Traceback:")
            errors.append(tb.format_exc())
            status = status + 1

    html_string = html_string + "</ul>\n"

    # creating an error log for file output
    error_log = "Encountered errors reading media: " + str(status) + "\n\nAffected conversations:\n" + str("\n".join(conv_errors)) + "\n\nError messages:\n" + str("\n".join(errors)) + "\n\n"

    return [html_string, chat_list, status, error_log]

# reading device information and converting it to html string
def read_devices(filename = "devices.json"):

    # error controls and logging
    status = 0
    errors = []

    # html template
    html_string = "<h2 id=\"devices\">Devices</h2>\n\t<ul>\n"

    # json to html conversion
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            f.close()

        for device in data:
            item_counter = 1
            html_string = html_string + "\t\t<li><b>" + str(device) + "</b></li>\n\t\t\t<ul>\n"
            for item in data[device]:
                html_string = html_string + "\t\t\t\t<li><b>Item " + str(item_counter) + "</b></li>\n\t\t\t\t\t<ul>\n"
                for key in item:
                    html_string = html_string + "\t\t\t\t\t\t<li><b>" + str(key) + ":</b> " + str(item[key]) + "</li>\n"
                html_string = html_string + "\t\t\t</ul>\n"
                item_counter = item_counter + 1
            html_string = html_string + "\t\t\t</ul>\n"
    except Exception as e:
        print("ERROR reading devices!")
        tb.print_exc()
        errors.append(str(repr(e)))
        errors.append("Detailed Traceback:")
        errors.append(tb.format_exc())
        status = status + 1

    html_string = html_string + "\t</ul>\n<hr>\n"

    # creating an error log for file output
    error_log = "Encountered errors reading devices: " + str(status) + "\nError messages:\n" + str("\n".join(errors)) + "\n\n"

    return [html_string, status, error_log]

# main function = executes all previous functions and concatenates html string to html file
# title can be changed as title = "<h1>YOUR TITLE HERE</h1>\n" (should be html)
# for args refer to README.md again
# needless to say that there are no input checks here either, incorrect inputs will lead to crashes!
# so be careful if you don't want things to go sideways
def instaview(filenames = ["profile.json", "searches.json", "connections.json", "media.json", "comments.json", "messages.json", "devices.json"], parse = [True, True, True, True, True, True, True], title = None, show_credits = True, verbose = True, logging = True, **kwargs):

    result = 0
    complete_log = ""

    if title is None:
        title = "<h1>INSTAGRAM DATA [" + str(datetime.datetime.today().strftime('%Y-%m-%d'))+ "]</h1>\n"

    if parse[5]:
        if verbose:
            print("Reading messages...")
        try:
            chat_string, chat_list, status_code, error_log = read_messages(filenames[5], **kwargs)
            complete_log = complete_log + error_log
            if status_code != 0:
                print("ERRORs encountered while reading chats: ", str(status_code))
        except Exception as e:
            chat_string, chat_list = ["", []]
            result = result + 32
            print("FATAL ERROR reading messages!")
            tb.print_exc()
            complete_log = complete_log + "\n\nFATAL ERROR reading messages!\n" + tb.format_exc() + "\n\n"

    if show_credits:
        sidebar = sidebar_template + "\t<a href=\"#credits\">Credits</a>\n</div>\n"
    else:
        sidebar = sidebar_template + "</div>\n"

    end_html = "\n</div>\n</body>\n</html>"

    if parse[0]:
        if verbose:
            print("Reading profile...")
        try:
            a, status_code, error_log = read_profile(filenames[0])
            complete_log = complete_log + error_log
            if status_code != 0:
                print("ERRORs encountered while reading profile: ", str(status_code))
        except Exception as e:
            a = ""
            result = result + 1
            print("FATAL ERROR reading profile!")
            tb.print_exc()
            complete_log = complete_log + "\n\nFATAL ERROR reading profile!\n" + tb.format_exc() + "\n\n"
    if parse[1]:
        if verbose:
            print("Reading searches...")
        try:
            b, status_code, error_log = read_searches(filenames[1])
            complete_log = complete_log + error_log
            if status_code != 0:
                print("ERRORs encountered while reading searches: ", str(status_code))
        except Exception as e:
            b = ""
            result = result + 2
            print("FATAL ERROR reading searches!")
            tb.print_exc()
            complete_log = complete_log + "\n\nFATAL ERROR reading searches!\n" + tb.format_exc() + "\n\n"
    if parse[2]:
        if verbose:
            print("Reading connections...")
        try:
            c, status_code, error_log = read_connections(filenames[2])
            complete_log = complete_log + error_log
            if status_code != 0:
                print("ERRORs encountered while reading connections: ", str(status_code))
        except Exception as e:
            c = ""
            result = result + 4
            print("FATAL ERROR reading connections!")
            tb.print_exc()
            complete_log = complete_log + "\n\nFATAL ERROR reading connections!\n" + tb.format_exc() + "\n\n"
    if parse[3]:
        if verbose:
            print("Reading media...")
        try:
            d, status_code, error_log = read_media(filenames[3])
            complete_log = complete_log + error_log
            if status_code != 0:
                print("ERRORs encountered while reading media: ", str(status_code))
        except Exception as e:
            d = ""
            result = result + 8
            print("FATAL ERROR reading media!")
            tb.print_exc()
            complete_log = complete_log + "\n\nFATAL ERROR reading media!\n" + tb.format_exc() + "\n\n"
    if parse[4]:
        if verbose:
            print("Reading comments...")
        try:
            g, status_code, error_log = read_comments(filenames[4])
            complete_log = complete_log + error_log
            if status_code != 0:
                print("ERRORs encountered while reading comments: ", str(status_code))
        except Exception as e:
            g = ""
            result = result + 16
            print("FATAL ERROR reading comments!")
            tb.print_exc()
            complete_log = complete_log + "\n\nFATAL ERROR reading comments!\n" + tb.format_exc() + "\n\n"
    if parse[6]:
        if verbose:
            print("Reading devices...")
        try:
            h, status_code, error_log = read_devices(filenames[6])
            complete_log = complete_log + error_log
            if status_code != 0:
                print("ERRORs encountered while reading devices: ", str(status_code))
        except Exception as e:
            h = ""
            result = result + 16
            print("FATAL ERROR reading devices!")
            tb.print_exc()
            complete_log = complete_log + "\n\nFATAL ERROR reading devices!\n" + tb.format_exc() + "\n\n"

    if show_credits:
        complete_html = html_template + sidebar + "<div class=\"main\">\n\n" + title + a + b + c + d + g + chat_string + h + credits + end_html
    else:
        complete_html = html_template + sidebar + "<div class=\"main\">\n\n" + title + a + b + c + d + g + chat_string + h + end_html

    with open("instaview_report.html", "w", encoding="utf-8") as f:
        f.write(complete_html)
        f.close()

    if logging:
        with open("instaview_report.log", "w", encoding="utf-8") as f:
            f.write(complete_log)
            f.close()

    return result

if __name__ == '__main__':
    # functions are run with default args when script is executed
    # this should terminate succesfully if script is in the right directory
    try:
        res = instaview()
        print(res)
    except Exception as e:
        print("ERROR! Is script in right directory?")
        tb.print_exc()
