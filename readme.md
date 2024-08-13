# Lead Generation Script

This script helps find potential customers automatically. You can run it on your computer or use Docker (a tool that packages your application).

## How to Run the Script

### Option 1: Run Without Docker

1. **Install Python Packages:**  
   First, make sure you have Python installed. Then, you need to install some extra tools to help the script work. To do that, type this command:
   ```bash
   pip3 install -r requirements.txt
   ```
2. **Create the .env File:**
   This file will store your API key securely. Create a new file called .env in the same folder as the script, and add this line to it:
   ```
   SERPAPI_KEY=78152e9897d998cc2b18bc9e2ab2203d490e47126b93f32d8b728983a7b3f422
   ```
3. **Run the Script:**
   After installing the tools, you can run the script with this command:
   ```bash
   python3 leadgen_script.py
   ```



### Option 2: Run with Docker

1. **Create the `.env` File:**  
   Before you build and run the Docker image, create a `.env` file in the same folder as the script. Inside this file, add your API key:
   ```
   SERPAPI_KEY=78152e9897d998cc2b18bc9e2ab2203d490e47126b93f32d8b728983a7b3f422
   ```

2. **Build the Docker Image:**  
   To use Docker, you first need to build the Docker image. Run this command in your terminal:
   ```bash
   docker build -t leadgen .
   ```

3. **Run the Script in Docker:**  
   After building the image, you can run the script inside a Docker container with this command:
   ```bash
   docker run --rm --env-file .env leadgen
   ```


