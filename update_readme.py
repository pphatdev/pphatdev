import json

with open('wakatime-stats.json') as f:
    data = json.load(f)

languages = data['data']['languages']
most_used_language = languages[0]['name']
total_seconds = languages[0]['total_seconds']

readme_content = f"""
# Hi there, I'm pphatdev! 👋

## About Me
I'm a passionate software developer who enjoys working on innovative and challenging projects. I love contributing to the developer community and learning new technologies. 

## Skills and Technologies
Here are some of the technologies I frequently work with:

- **Languages:** 
  - Python 🐍
  - JavaScript (Node.js, React) 🌐
  - Java ☕
  - C++ 💻

- **Frameworks and Libraries:**
  - Django 🚀
  - React ⚛️
  - Spring Boot 🌱

- **Tools:**
  - Git & GitHub 🐙
  - Docker 🐳
  - Kubernetes ☸️
  - Jenkins 🛠️

- **Databases:**
  - MySQL 🗄️
  - PostgreSQL 🐘
  - MongoDB 🍃

## Projects
Here are some of my favorite projects that I've worked on:

- [**Project 1**](https://github.com/pphatdev/project1): A brief description of what this project does.
- [**Project 2**](https://github.com/pphatdev/project2): A brief description of what this project does.
- [**Project 3**](https://github.com/pphatdev/project3): A brief description of what this project does.

## WakaTime Stats
Most used language this week: **{most_used_language}**
Total coding time: **{total_seconds // 3600} hours {total_seconds % 3600 // 60} minutes**

## Get in Touch
- **Email:** pphatdev@example.com
- **LinkedIn:** [linkedin.com/in/pphatdev](https://www.linkedin.com/in/pphatdev)
- **Twitter:** [twitter.com/pphatdev](https://twitter.com/pphatdev)

Feel free to reach out to me if you have any questions, suggestions, or just want to connect!

## GitHub Stats
![pphatdev's GitHub stats](https://github-readme-stats.vercel.app/api?username=pphatdev&show_icons=true&theme=radical)

Thanks for visiting my profile!
"""

with open('README.md', 'w') as f:
    f.write(readme_content)
