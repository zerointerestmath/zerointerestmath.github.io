#!/usr/bin/env python3
import os

page_title = "0% Interest Math"
main_title = "Zero Interest Math"
content_dir = "content"
template_file = "template/default.html"
author = "<a href='https://twitter.com/0InterestMath/'>@0InterestMath</a>"


def readfile(path):
    f = open(path, encoding="utf-8")
    if not f:
        return ""
    s = f.read()
    f.close()
    return s



def link_template(postname, post):
    lines = post.split("\n")
    title = lines[0]
    # print(postname)
    return f"<li><a href='#{postname}'>{title}</a></li>"

def post_template(postname, post):
    lines = post.split("\n")
    title = lines[0]
    subtitle = lines[1]
    body = "\n".join(lines[2:])
    body = body.replace("\n\n", "</p><p>")
    return (f"<h2 id='{postname}'>{title}</h2>\n" +
        f"<h3>{subtitle}</h3>\n" +
        f"<p>{body}</p>")

main_content = ""
links = ""
posts = os.listdir(content_dir)
posts.sort(reverse=True)
for postname in posts:
    file = os.path.join(content_dir, postname)
    try:
        post = readfile(file)
        link = link_template(postname, post)
        text = post_template(postname, post)
        links = links + "\n" + link
        main_content = main_content + "\n<hr>\n\n" + text
        #print(link)
    except:
        pass

html = readfile(template_file)
html = html.replace("{{page_title}}", page_title)
html = html.replace("{{main_title}}", main_title)
html = html.replace("{{links}}", links)
html = html.replace("{{main}}", main_content)
html = html.replace("{{author}}", author)


with open("index.html", "w") as file:
    file.write(html)
