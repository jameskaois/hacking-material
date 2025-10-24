#!/usr/bin/env python3

import requests
import argparse

md_content = ""
# https://tryhackme.com/api/v2/rooms/details?roomCode
# https://tryhackme.com/api/v2/rooms/tasks?roomCode
def getRoomDetails(ROOM_SLUG):
    global md_content
    response = requests.get(f"https://tryhackme.com/api/v2/rooms/details?roomCode={ROOM_SLUG}")

    if response.status_code != 200:
        print("❌ Failed to fetch details. Status:", response.status_code)
        exit()
    
    data = response.json()['data']

    title = data['title']
    difficulty = data['difficulty']
    description = data['description']
    timeToComplete = data['timeToComplete']

    md_content += f"# {title} - TryHackMe \n\n{description}\n\n## Overview\n- **Room URL:** [https://tryhackme.com/room/{ROOM_SLUG}](https://tryhackme.com/room/{ROOM_SLUG})\n- **Difficulty:** {difficulty.capitalize()}\n- **Time to complete:** {timeToComplete}\n\n"

def getRoomTasks(ROOM_SLUG):
    global md_content
    response = requests.get(f"https://tryhackme.com/api/v2/rooms/tasks?roomCode={ROOM_SLUG}")

    if response.status_code != 200:
        print("❌ Failed to fetch tasks. Status:", response.status_code)
        exit()

    tasks = response.json()['data']
    md_content += "## Walkthrough\n"

    for i in range(0, len(tasks)):
        task_title = tasks[i]['title']
        questions = tasks[i]['questions']

        md_content += f"### {i+1}. {task_title}\n"

        for question in questions:
            title = question['question']
            md_content += f"- {title}\n\n"
            md_content += "**=> Answer: `something`**\n\n"

def main():
    parser = argparse.ArgumentParser(description="Scrape TryHackMe room tasks and export to markdown")
    parser.add_argument("--slug", required=True, help="Slug of the TryHackMe room (e.g. offensivesecurityintro)")
    args = parser.parse_args()

    slug = args.slug
    getRoomDetails(slug)
    getRoomTasks(slug)

    with open(f"./{slug}_writeup.md", "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"✅ Writeup saved as {slug}_writeup.md")

if __name__ == "__main__":
    main()