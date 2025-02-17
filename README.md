Hacker News CLI Reader

Overview
This script fetches and displays the top 10 articles from [Hacker News](https://news.ycombinator.com/) using its public API. Users can view article titles in the terminal and open selected articles in their web browser.

Features
- Fetches the latest top 10 stories from Hacker News.
- Displays article titles in a formatted list.
- Allows users to open selected articles in their default web browser.
- Automatically installs missing dependencies.

Prerequisites
- Python 3.x
- Internet connection

Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/HackerNews-CLI.git
   cd HackerNews-CLI
   ```
2. Ensure dependencies are installed:
   ```bash
   pip install requests
   ```

Usage
Run the script using:
```bash
python hackernews.py
```

How It Works
- The script fetches top articles from Hacker News.
- It prints a numbered list of article titles.
- Users can enter an article number to open it in their browser.
- Pressing Enter quits the program.

Future Improvements
- Support for fetching more than 10 articles.
- Additional filtering options (e.g., by score, author, time).
- Caching for offline access.

License
This project is open-source and available for modification and distribution.
