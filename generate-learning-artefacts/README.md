# Introduction

A fundamental problem of traditional lecture-based education is that the learning process is exaggerated from its natural “life” context, and is artificially implanted into classroom/lecture hall settings. Often there is a serious mismatch between the skills needed in real-life and the theoretical knowledge acquired. This is especially important for the area of ICT where the speed of technology changes constantly increases. Therefore, the education should be teaching students how to learn, think and collaborate effectively, instead of just transferring knowledge.

By designing learning process as role-playing game (RPG), in ChallengeUnicorder™ method and platform developed by IPT - Intellectual Products & Technologies Ltd we try to bring back fun as main intrinsic motivation for learning. The paper investigates how to cultivate these “natural”, “integral” and fun qualities of the learning process, lost in traditional “lecture-style” education. In order to do so we employ Problem Based Learning (PBL) – authentic learning challenges, missions, and activities are proposed, solving real-world problems, but in limited context and complexity.

The game design follows the MDA (Mechanics, Dynamics, Aesthetics) framework, proposed by Hunicke et al. The main gamification elements are mapped to learning domain concepts – challenges are mapped to learning goals, levels to learning path, points and feedback to positive reinforcement, leaderboards to learning analytics, badges and tokens are used to improve motivation. Both forces of competition (allowing to compare team achievements with other learners/teams), and collaboration (between the players in a team) are employed to design engaging and productive learning experience.

## Using LLMs for learning gamification artifacts generation
The main purpose of current sub-project was to employ existing Large Language Models (LLMs) for gamification challenges and content (learning objects - LOs) generation in the context of ChallengeUnicorder™ platform. Several LLMs were investigated - llama3-8B, llama3.1-8B, gemma2-9B/70B, and mistral-7B. Larger LLMs were also tried, but due to my lack of previous experience with AMD cloud, I was not able to run them successfully. I preferred using Ollama and ollama-python libraries for running LLMs.

The [instructions for installing Ollama from their official web site / GitHub repository](https://github.com/ollama/ollama?tab=readme-ov-file) should be first followed. The examples from Ollama official github repository were used as base for interactive and non interactive learning gamification artifacts generation: [https://github.com/ollama/ollama/tree/main/examples](https://github.com/ollama/ollama/tree/main/examples)

Here are some examples for prompting Llama3.1 (with minor editing):

> generate short programming problems/challenges to determine proficiency for each topic in python programming (concepts, objects, methods, algorithms and data structures):
```
1. Basic Concepts (Python):
- Write a Python script that takes two command-line arguments and outputs their sum.
- Write a Python script that prints Fibonacci sequence up to a specified number.
- Write a Python script that defines a function to find the maximum of three numbers.
2. Basic Concepts (Web Programming):
- Create a simple Flask application that displays "Hello, World!" on the browser.
- Write a simple Django view that returns an HTTP 404 error with a custom message.
3. Data Structures:
- Implement a linked list using classes and methods in Python.
- Write a Python function to find the kth smallest element in a binary search tree.
- Create a dictionary where the keys are integers, and the values are lists of their factors.
4. Algorithms:
- Implement a quicksort algorithm for sorting a list of integers.
- Write a Python function that checks if two strings are anagrams of each other.
- Implement a binary search algorithm for finding a target value in a sorted list.
5. Libraries:
- Use NumPy to find the mean and standard deviation of a given 1D array.
- Import Pandas and use it to load a CSV file containing data about employees, then group employees by department.
6. File Operations:
- Write a Python script that reads lines from a text file and outputs their frequencies as a dictionary.
- Create a function that takes a filename as input and appends the contents of that file to another file.
7. Advanced Concepts:
- Implement a coroutine using Python's asyncio library.
- Write a decorator in Python that logs all functions called with it, including arguments and return values.
- Use context managers to ensure that a file is always closed after use.
8. Web Frameworks (Flask):
- Create a Flask application that displays a list of users and allows adding new ones using a form.
- Build a simple authentication system for a Flask application using username and password hashes stored in a database.
9. Databases and ORMs (SQLAlchemy):
- Write a Python script that connects to a SQLite3 database, creates a table named "users", and inserts some sample data into it.
- Define a User class using SQLAlchemy's declarative base, then create instances of the class and save them to the database.
10. APIs (Scrapy):
- Scrape data from an HTML page using Beautiful Soup and store it in a CSV file.
- Create a simple web scraper that logs into a website and retrieves a user's profile information.
11. Web Security:
- Implement input validation for an HTML form to prevent XSS attacks.
- Write a Flask middleware that checks incoming requests for CSRF tokens.
- Use HTTPS when making external requests with the Requests library.
```
The second, more specific task performed by LLMs was to:
> generate more basic programming problems/challenges together with unit tests for their solutions' verification

Here is a specific example for task 1.2 (Fibbonacci number generation):

- Problem: Write a function `fibonacci(n)` that takes an integer as input and returns the nth Fibonacci number.
- Test Case:
```python
def test_fibonacci(self):
    self.assertEqual(fibonacci(0), 0)
    self.assertEqual(fibonacci(1), 1)
    self.assertEqual(fibonacci(2), 1)
    self.assertEqual(fibonacci(3), 2)
    self.assertEqual(fibonacci(4), 3)
    self.assertEqual(fibonacci(5), 5)
    self.assertEqual(fibonacci(6), 8)
```
- Solution:
```python
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
             a, b = b, a + b
        return b
```

Because the corner test cases were missing I used further prompt elaboration (for another challenge/problem):

> for the problems above add test cases for border cases and errors/exceptions
Below are additional test cases added to the previous data structures problems, including edge cases, corner cases, and error handling:
```
1. Singly Linked List (Insert, Search, Delete) - Added tests for an empty list, duplicate elements, and out-of-range indices:
- Empty List:
```
```python
def test_insert_empty(self):
    sll = SinglyLinkedList()
    sll.insert(1)
    self.assertEqual(sll.head.data, 1)

- Duplicate Elements:
```python
def test_insert_duplicates(self):
    sll = SinglyLinkedList()
    sll.insert(1)
    sll.insert(1)
    self.assertEqual(sll.head.next.data, 1)
```
```
- Out-of-Range Indices:
```
```python
def test_search_out_of_range(self):
    sll = SinglyLinkedList()
    sll.insert(1)
    self.assertFalse(sll.search(-1))
def test_delete_out_of_range(self):
    sll = SinglyLinkedList()
    sll.insert(1)
    with self.assertRaises(IndexError):
    sll.delete(-1)
```
LLMs were used also for automatic generation of a questionnaires to determine the gaming and learning styles of individual learners/players (needed for dynamic adaptation of learning challenge/content). Here are the generated questions:
> provide testing questions allowing to determine affinity of a learner to each learner style
To assess a learner's affinity toward different learning styles, you can use the following questions as a starting point:
```
1. Visual learners:
- When studying for an exam, do you prefer using diagrams, charts, or other visual aids?
- Do you remember information better when it is presented visually, such as in pictures, maps, or infographics?
- Would you rather read textbooks with lots of illustrations or ones with minimal visual elements?
2. Auditory learners:
- Do you find that listening to lectures helps you understand and remember the material better?
- When studying, do you prefer to listen to recorded lessons, discussions, or podcasts?
- Are you more comfortable expressing your ideas through speaking rather than writing?
3. Kinesthetic learners:
- Do you prefer hands-on activities, such as experiments, demonstrations, or simulations, when learning new concepts?
- Would you describe yourself as someone who prefers to take notes by hand instead of typing them on a computer?
- Are you more engaged in learning situations that involve physical movement, such as group projects or role-playing exercises?
>>> and for the Diverger/Converger, Introvert/Extrovert, Active/Reflective, and Global/Analytical
For the alternative learner styles:
1. Diverger/Converger:
- Do you prefer brainstorming new ideas and exploring possibilities before analyzing them (Diverger)?
- Or do you like to focus on specific details and analyze information before considering the bigger picture (Converger)?
2. Introvert/Extrovert:
- Are you more comfortable working alone or in small groups, and prefer quiet environments for studying (Introvert)?
- Or do you thrive in social settings, prefer group discussions and projects, and gain energy from being around others (Extrovert)?
3. Active/Reflective:
- Are you more engaged when actively participating in learning activities such as hands-on projects or simulations (Active)?
- Or do you prefer to take a step back and think about concepts before diving into practical applications (Reflective)?
4. Global/Analytical:
- Do you have a tendency to focus on the overall picture and connections between ideas when learning (Global)?
- Or do you prefer to pay close attention to details and specifics in order to fully understand a concept (Analytical)?
```
Here are 10 more python programming challenges generated by Gemma2 model:
**Challenges:**
1. **Title: "Number Guessing Game"**
* **Learning Objective(s):**  Basic input/output, conditional statements (`if`, `else`), random number generation
* **Scenario:** You're a psychic trying to guess the secret number chosen by a mysterious entity.
* **Task:** Write a program that generates a random number between 1 and 100. The player has to guess the number within a limited number of attempts, receiving feedback (higher/lower) after each guess.
* **Reward:** 50 points + "Psychic Apprentice" badge
2. **Title:  "Grocery List Manager"**
* **Learning Objective(s):** Lists, list manipulation (`append`, `remove`, indexing), loops
* **Scenario:** You're organizing your grocery shopping for the week.
* **Task:** Create a program that allows users to add items to their grocery list, remove items, and view the complete list. Implement a loop to keep the program running until the user decides to quit.
* **Reward:** 75 points + "Organized Shopper" badge
3. **Title: "Text Analyzer"**
* **Learning Objective(s):** String manipulation (`len`, `.upper()`, `.lower()`, `.split()`), basic file I/O
* **Scenario:** You're a detective analyzing a cryptic message.
* **Task:** Write a program that reads text from a file, counts the number of words and characters, identifies the most frequent word, and converts the entire text to uppercase or lowercase based on user input.
* **Reward:** 100 points + "Detective Duo" badge
4. **Title: "Temperature Converter"**
* **Learning Objective(s):** Functions, arguments, return values, basic math operations
* **Scenario:** You're building a handy tool for travelers to convert temperatures between Celsius and Fahrenheit.
* **Task:** Create a program with a function that takes a temperature in one unit (Celsius or Fahrenheit) as input and returns the equivalent temperature in the other unit. Allow users to choose which conversion they
want.
* **Reward:** 60 points + "Climate Concierge" badge
5. **Title: "Simple Calculator"**
* **Learning Objective(s):** Conditional statements, user input, basic arithmetic operations
* **Scenario:** You're designing a user-friendly calculator app.
* **Task:** Write a program that takes two numbers as input from the user and performs basic mathematical operations (addition, subtraction, multiplication, division) based on the user's choice.
* **Reward:** 70 points + "Math Magician" badge
6.  **Title: "Password Generator"**
* **Learning Objective(s):** Modules (`random`), loops, string concatenation
* **Scenario:** You want to create strong and random passwords for your online accounts.
* **Task:** Write a program that generates a random password of a specified length (user input) using a combination of uppercase letters, lowercase letters, numbers, and special characters.
* **Reward:** 80 points + "Cybersecurity Guru" badge
7. **Title:  "Rock Paper Scissors"**
* **Learning Objective(s):** Conditional statements (`if`, `elif`, `else`), random number generation, loops
* **Scenario:** You're playing a classic game of Rock Paper Scissors against the computer.
* **Task:** Create a program that allows the player to choose between rock, paper, or scissors. The computer randomly selects its move. Implement logic to determine the winner based on the standard rules of the game.
* **Reward:** 90 points + "Game Master" badge
8. **Title: "Data Visualization with Matplotlib"**
* **Learning Objective(s):** Introducing external libraries (Matplotlib), data visualization, basic plotting techniques
* **Scenario:** You have collected some data on a topic that interests you (e.g., temperature changes over time, population growth).
* **Task:** Use the Matplotlib library to create a visual representation of your data. Experiment with different plot types (line graphs, bar charts, scatter plots) and customize the appearance of your visualizations.
* **Reward:** 120 points + "Data Artist" badge
9.  **Title:  "Text-Based Adventure Game"**
* **Learning Objective(s):** Combining multiple concepts learned previously (functions, loops, conditional statements, input/output), basic game design principles
* **Scenario:** You're creating a simple text adventure where the player navigates through different rooms or locations and makes choices that affect the outcome of the story.
* **Task:** Design a storyline with multiple paths. Use functions to represent different actions or events in the game. Implement input from the player to guide the progress of the story.
* **Reward:** 150 points + "Game Developer" badge
10. **Title:  "Simple Web Scraper"**
* **Learning Objective(s):** Introducing web scraping concepts (using libraries like `requests` and `BeautifulSoup`), handling HTML data
* **Scenario:** You want to collect information from a specific website (e.g., news headlines, product prices).
* **Task:** Write a program that retrieves the HTML content of a webpage and extracts relevant data using appropriate selectors. Display the extracted information in a user-friendly format.
* **Reward:** 200 points + "Web Wizard" badge

## Interactive Generation Example

The **chat** endpoint is one of two ways to generate text from an LLM with Ollama, and is introduced in version 0.1.14. At a high level, you provide the endpoint an array of objects with a role and content specified. Then with each output and prompt, you add more of those role/content objects, which builds up the history.

### Running the Example

1. Ensure you have the `llama3.1` model installed:

   ```bash
   ollama pull llama3.1
   ```

2. Install the Python Requirements.

   ```bash
   pip install -r requirements.txt
   ```

3. Run the example:

   ```bash
   python interactive.py
   ```

### Review the Code

You can see in the **chat** function that actually calling the endpoint is done simply with:

```python
r = requests.post(
  "http://0.0.0.0:11434/api/chat",
  json={"model": model, "messages": messages, "stream": True},
)
```

With the **generate** endpoint, you need to provide a `prompt`. But with **chat**, you provide `messages`. And the resulting stream of responses includes a `message` object with a `content` field.

The final JSON object doesn't provide the full content, so you will need to build the content yourself.

In the **main** function, we collect `user_input` and add it as a message to our messages and that is passed to the chat function. When the LLM is done responding the output is added as another message.

### Next Steps

In this example, all generations are kept. You might want to experiment with summarizing everything older than 10 conversations to enable longer history with less context being used.


## Learning Artifacts Generation Example

This is a simple example using the **Generate** endpoint.

### Running the Example

1. Ensure you have the `stablelm-zephyr` model installed:

   ```bash
   ollama pull mistral:7b-instruct-v0.2-q8_0
   ```

2. Install the Python Requirements.

   ```bash
   pip install -r requirements.txt
   ```

3. Run the example:

   ```bash
   python generation.py
   ```

### Review the Code

The **main** function simply asks for input, then passes that to the generate function. The output from generate is then passed back to generate on the next run.

The **generate** function uses `requests.post` to call `/api/generate`, passing the model, prompt, and context. The `generate` endpoint returns a stream of JSON blobs that are then iterated through, looking for the response values. That is then printed out. The final JSON object includes the full context of the conversation so far, and that is the return value from the function.

## Conclusions and future work
As a conclusion, by using further LLMs prompting, the challenges/problems/tests/questions can be further varied/extended which proves to be useful for dynamic artifacts generation in an e-learning gamification platform like ChallengeUnicorder™. The generated unit tests could be used for automatic solutions verification and scoring. Though for more complex problems the generated tests tend to be less detailed/robust, and more "sketchy", with some white spots to be filled manually, which defeats the purpose of fully automated solutions verification. So this problem should be further investigated and resolved.
