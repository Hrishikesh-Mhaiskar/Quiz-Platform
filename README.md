# Quizit

#### Video Demo: [Link to Video Demo](https://youtu.be/yhcOtwTsDfA)

#### Description:

Welcome to Quiz Platform, a place where you can make and enjoy personalized quizzes. Whether you're looking to test your knowledge or spark some friendly competition, this platform has you covered. With an easy registration process and robust security measures, you can dive into the world of quizzes worry-free! Additionally, there random quizzes to explore that ensure there's always something new to discover!

## Features

### 1. Custom Quizzes

Users have the freedom to create their own custom quizzes, adding questions tailored to their preferences. Whether it's for educational purposes, testing knowledge on a specific subject, or simply for fun, the custom quiz feature allows users to curate content that suits their interests and learning objectives. With the ability to customize the questions, and multiple-choice options, users can create quizzes that cater to various topics and difficulty levels.

### 2. System-Generated Quizzes

For users seeking variety and spontaneity, the platform offers system-generated quizzes sourced from the Open Trivia DB API. These quizzes cover a wide range of topics and are dynamically generated. Whether users are looking to challenge themselves with random trivia or explore new topics, the system-generated quizzes provide a convenient way to engage with fresh content and expand their knowledge base.

### 3. Secure Authentication

The platform prioritizes the security of user accounts by implementing robust authentication mechanisms. User passwords are securely encrypted using the SHA256 hashing algorithm and salts, ensuring that sensitive information remains protected against unauthorized access. Additionally, the login and registration processes are designed to prevent common security vulnerabilities such as SQL injection and cross-site scripting, providing users with peace of mind while accessing the platform's features.

### 4. Dynamic Question Rendering

Questions provided by users are stored in a database and dynamically rendered into HTML templates for quiz-taking. This dynamic rendering process ensures that quizzes are displayed consistently across different devices providing users with a seamless experience. Additionally, the use of dynamic rendering allows for efficient management of quiz content without disrupting the overall quiz-taking experience.

### 5. Time-Limited Quizzes

Each quiz is equipped with a time limit of 5 minutes, ensuring timely completion and submission. This time limit adds an element of challenge and urgency to the quiz-taking experience, encouraging users to prioritize their responses and make quick decisions. By setting a time limit, users are prompted to focus their attention and demonstrate their knowledge within a defined timeframe, enhancing the overall engagement and excitement of quiz participation.

### 6. Score Display

Upon quiz submission, users are redirected to a score page displaying their performance metrics, including the number of correct, incorrect, and unattempted questions, as well as the time taken to complete the quiz. This score display provides users with valuable feedback on their quiz performance, allowing them to assess their strengths and areas for improvement. This helps to foster a sense of competition and motivation for continuous learning and improvement.

## Technologies Used

- Flask
- HTML
- CSS
- SQLite
- JavaScript
- Bootstrap
- Open Trivia DB API
- Jinja Templating Language
- Python (backend logic)
- Werkzeug Security (for password encryption)
- CS50 Module

## Usage

The Quiz Platform is designed to be intuitive and user-friendly. Here's a step-by-step guide on how to use it:

1. Registration and Login: To access the full features of the platform, users need to register an account. Click on the "Register" button and fill in the required information, including a username and a secure password. Once registered, users can log in using their credentials.

2. Creating Custom Quizzes: After logging in, users can select the "Make Quiz" section. Here, they can add questions by clicking on the "Add Question" button. Each question requires a prompt and multiple-choice options. Users can add as many questions as they like and save the quiz.

3. Taking Quizzes: To take a quiz, users can either select the "Take quiz" option available to access their own created quizzes or select "Attempt a random quiz" to take the system-generated quizzes. Upon selecting a quiz, users are directed to the quiz-taking interface where they can read each question, select their answer, and proceed to the next question. The platform automatically tracks the time remaining for each quiz, which is displayed at top right corner.

4. Viewing Scores: Once a quiz is completed, users are redirected to a score page where they can view their performance metrics that shows the number of correct, incorrect, and unattempted questions, as well as the time taken to complete the quiz.

## Conclusion

In conclusion, Quizit is your ultimate quiz companion, designed to make learning fun and engaging. By offering a blend of user-created and system-generated quizzes, it caters to every learning style and interest. With a focus on security and a user-friendly interface, it aims to provide a seamless experience for quiz enthusiasts of all levels. So why wait? Register at Quizit Quiz today and embark on your quiz-taking adventure!

Thank you for exploring Quiz Platform! I welcome you to dive in and start creating and taking quizzes. Happy quizzing!