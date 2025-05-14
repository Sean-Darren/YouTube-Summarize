# YouTube Video Summarizer

Easily generate concise summaries and key points for any YouTube video!  
This tool extracts video metadata, fetches English transcripts, and uses OpenAI to summarize the content—making it perfect for quick reviews or note-taking.

---

## ✨ Features

- **Extracts Video Title & Channel**  
  Automatically fetches the video's title and the publishing channel.

- **Fetches English Transcripts**  
  Retrieves and compiles English subtitles (if available) for accurate summarization.

- **Generates Summaries with Key Points**  
  Uses OpenAI to produce a brief summary, bullet-pointed key points, and a conclusion—all in your chosen language.

---

## 🚀 Usage

1. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```
2.**Set Up OpenAI API Key**

  ```bash
  export OPENAI_API_KEY="your-api-key"
  ```
3. **Run the Summarizer**

   ```bash
   python main.py
   ```

You will be prompted to enter:
- The YouTube video URL
- The language code for your summary (default: en for English)

## 🛠️ How It Works
- Extracts Video ID from your YouTube URL
- Fetches Title & Channel using BeautifulSoup
- Downloads English Transcripts with youtube-transcript-api
- Generates Summaries using OpenAI’s GPT models
  
## ⚠️ Requirements
- Python 3.7+
- OpenAI API Key
- All Python dependencies from requirements.txt

## 🤝 Contributions
Pull requests and issues are welcome!


