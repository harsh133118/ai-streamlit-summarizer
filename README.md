# ai-streamlit-summarizer
AI text summarizer using Streamlit and Hugging Face's DistilBART model.
AI Text Summarizer Project 🧠
Project Goal and Deliverables
This project fulfills the requirement to build a simple AI-powered application, demonstrating effort, resourcefulness, and creativity. I chose to build a Text Summarizer using free, powerful tools to condense long articles into a customized, concise length.

Requirement	Status	Stretch Goals Achieved
AI Q&A Bot / Summarizer / Tracker	Completed (Summarizer)	1. Built a Streamlit UI. 2. Deployed for free via Google Colab/ngrok.
Install Python/Node.js	Completed (Used Python/Colab)	3. Implemented performance caching (@st.cache_resource).
Create GitHub Repo & README	Completed	4. Solved a critical deployment issue (ERR_NGROK_4018).

Export to Sheets
Technical Stack
Language: Python

AI Library: Hugging Face transformers (using the sshleifer/distilbart-cnn-12-6 model).

User Interface: Streamlit.

Deployment: Google Colab (for environment) and ngrok (for public tunnel access).

Documentation of Effort and Resourcefulness (My Journey)
This section details the critical challenges encountered and the solutions implemented, directly showcasing resourcefulness and problem-solving skills.

1. The ngrok Authentication Fix (ERR_NGROK_4018)
Challenge	Solution Implemented	Resourcefulness Shown
The application failed to expose the Streamlit UI, returning an ERR_NGROK_4018 due to ngrok's new requirement for token authentication on the free tier.	I immediately signed up for a free ngrok account, copied my unique authtoken from the dashboard, and used the ngrok.set_auth_token() command in the Colab notebook before connecting the tunnel.	Demonstrated adaptability and successful use of external documentation to fix a sudden dependency change.

Export to Sheets
2. Controlling Summary Length Accurately
Challenge	Solution Implemented	Resourcefulness Shown
Initial thought was to force a 3-sentence stop, but this is messy and breaks the AI model's natural flow.	I researched the Hugging Face pipeline documentation and pivoted the design to use the model's native max_length parameter. I connected this to a Streamlit slider so the user controls the summary length accurately by word count.	Demonstrated pragmatism and adapting the UI/design to leverage the most robust and intended features of the AI tool.

Export to Sheets
3. Preventing Slow Model Reloads
Challenge	Solution Implemented	Resourcefulness Shown
The AI model is large (~400MB) and reloading it every time a user generated a summary was too slow and wasteful.	I wrapped the model loading function in Streamlit's @st.cache_resource decorator, ensuring the model is only downloaded and loaded into memory once per session.	Demonstrated attention to performance optimization and efficient use of the specific platform (Streamlit).

Export to Sheets
How to Run the App (Live Demo)
The application is fully runnable via Google Colab.

Open the AI_Summarizer_Project.ipynb Colab notebook.

Run all code cells sequentially (after inserting your ngrok token).

Click the final ngrok URL provided in the output to access the live web application.

(Your live link, which was active when this was written): https://cammy-foreign-unstridently.ngrok-free.dev
