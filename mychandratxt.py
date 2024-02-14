import base64
import json
import requests
from jinja2 import Template

template  = Template(open("template.html").read())
login_url = "http://api.chandrainstitute.com/api/v2/api.php/user/login"

user = input("Enter user_id/mobile: ")
password = input("Enter password: ")

info = {
 "mobile": user,
 "password": password,
 "android_id": "asdasdasda"
}

auth = "7b81679d-a829-4476-8dcf-9c3bb4e0c80a"
res = requests.post(login_url, data=json.dumps(info), headers={"Auth":auth})
login_res = res.json()
login_dict = login_res["response"]
u_id, token = login_dict["u_id"], login_dict["auth_token"]
all_course_link = "http://api.chandrainstitute.com/api/v2/api.php/get/all/course"
new_info = {
 "user_id": u_id,
 "course_type": "videos",
 "payment_type": "paid"
}
courses_res = requests.post(all_course_link, data=json.dumps(new_info), headers={"Auth":auth, "token": token})

courses_dict = courses_res.json()["response"]
for course_dict in  courses_dict:
    course_id, course_title = course_dict["cp_id"], course_dict["title"]
    course_title = f"{course_id}. {course_title}"
    course_link = f"http://api.chandrainstitute.com/pdo/api/api.php/get/list/subjects/videos/all/{course_id}"
    course_res = requests.get(course_link, headers={"Auth":auth, "token": token})
    try:
        subjects = course_res.json()["response"]
    except:
        continue 
    output_dict = {}
    for subject in subjects:
        subject_id, subject_name = subject["subject_id"], subject["subject_name"]
        subject_title = f"{subject_id}. {subject_name}"
        subject_link = "http://api.chandrainstitute.com/api/v2/api.php/get/class/all/chapters/list"
        subject_info = {
         "course_id": course_id,
         "subject_id": subject_id,
         "u_id": u_id
        }
        subject_res = requests.post(subject_link, data=json.dumps(subject_info), headers={"Auth":auth, "token": token})
        try:
            chapters = subject_res.json()["response"]
        except:
            continue
        videos_dict = {}
        for chapter in chapters:
            chapter_id = chapter["chapter_id"]
            chapter_name = chapter["chapter_name"]
            youtube_id = chapter["youtubeId"]
            video_id = base64.b64decode(youtube_id).decode("UTF-8")
            video_link = f"https://youtu.be/{video_id}"
            video_title = f"{chapter_name}"
            videos_dict[video_title] = video_link
            mtext = f"{chapter_name}:{video_link}\n"
#            open(f"{subject_title}.txt", "a").write(mtext)
            open(f"{course_id}.txt", "a").write(mtext)
        
        output_dict[subject_title] = videos_dict
#        open(f"{course_title}/{subject_title}.txt", "w").write(mtext)

    open(f"{course_id}.json", "w").write(json.dumps(output_dict, indent=4))
#    open(f"{course_title}.txt", "a").write(mtext)
    print(f"Done:- {course_title}")

print("\n", "Finished".center(60, "-"))
#open(f"{course_title}.txt", "a").write(json.dumps(output_dict,"utf-8"))
#print(f"Done:- {subject_title}")
print("\n", "Finished".center(60, "-"))
open(f"{course_title}.html", "w").write(template.render(title=course_title, batch=course_title, topics=output_dict, type="videos"))
open(f"{course_title}.html", "w").write(template.render(title=course_title, batch=course_title, topics=output_dict, type="notes"))


