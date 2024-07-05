# QGen Atlas - Multilingual Query Generation and Response Validation
## Authors

- Sai Pranav Kothapalli (saipranavkothapalli@gmail.com)
- Panchumarthi Sri Hari Priya (sriharipriya2529@gmail.com)
- Deepthi Godavarthi (saideepthi531@gmail.com)

## Institution

School of Computer Science and Engineering, VIT-AP University, Inavolu Beside AP Secretariat, Amaravati, Andhra Pradesh, India

<img width="822" alt="Screenshot 2024-07-05 at 6 24 42 PM" src="https://github.com/saipranavkothapalli/QGen-Atlas/assets/144220767/8c61b40e-e785-4c1e-bd7d-6fda775ad872">

## Abstract

QGen Atlas is a comprehensive framework designed for facilitating multilingual query generation and response validation within the realm of natural language processing (NLP) projects. This versatile system enables users to input text, effortlessly generate a specified number of queries and corresponding responses, and seamlessly choose between objective and subjective question types. Leveraging advanced techniques such as chunking for syntactic analysis and the Levenshtein distance algorithm for computing similarity percentages between user responses and expected answers, the framework accurately parses input text, extracts relevant information, and generates meaningful questions and responses. The system also integrates translation capabilities into multiple languages via an API, enhancing accessibility and accommodating diverse linguistic preferences. QGen Atlas demonstrates its efficacy across educational, research, and practical applications, addressing the need for a versatile framework in NLP and contributing to advancements in language processing technologies.

## Keywords

Response validation, multilingual, objective questions, subjective questions, chunking, cosine similarity scoring

## Introduction

Natural Language Processing (NLP) systems play a vital role in various domains, including education, research, and information retrieval. One fundamental aspect of NLP is query generation, which involves creating questions based on input text for comprehension testing or study purposes. However, existing systems often lack support for multilingualism and comprehensive response validation. QGen Atlas addresses these limitations by providing a robust framework for generating questions and validating responses in multiple languages.

## Problem Statement

Existing NLP frameworks often lack comprehensive support for multilingual query generation and response validation, limiting their effectiveness and usability in diverse linguistic contexts. Additionally, the absence of robust techniques for generating varied and contextually relevant questions hampers the utility of NLP systems in educational, research, and practical applications. Therefore, the need for a comprehensive framework that enables multilingual query generation and response validation in NLP projects is crucial.

## Description of User-Provided Input

QGen Atlas operates on user-provided text data, which can vary in length, language, and complexity. The system is flexible and adaptable to different types of text, including articles, essays, and research papers. Users can input text in any supported language, and the framework handles translation and processing seamlessly.

## Methodology

### Preprocessing

Tokenization is a fundamental preprocessing step in natural language processing (NLP) where text is broken down into smaller units known as tokens. Sentence segmentation, also known as sentence boundary detection, involves identifying and separating individual sentences within a given text.

### Building Architecture

#### Chunking for Sentence Processing

Chunking aids in the extraction of relevant linguistic information from sentences, facilitating the generation of both objective and subjective questions. By defining specific rules and patterns for chunking, we can isolate and capture key noun phrases, which are crucial for formulating coherent questions.

<img width="820" alt="Screenshot 2024-07-05 at 6 26 42 PM" src="https://github.com/saipranavkothapalli/QGen-Atlas/assets/144220767/acf5690f-03ea-4a41-af73-5eb02cbb77c9">

#### ObjectiveTest Class

- **Initialization**: Initialized with input text data and the desired number of questions.
- **Trivial Sentence Identification**: Tokenizes the input text into sentences and identifies trivial sentences based on certain criteria.
- **Trivial Sentence Processing**: Processes trivial sentences to extract key information.
- **Question Generation**: Generates objective-type questions by replacing certain words or phrases with blanks.
- **Answer Generation**: Derives answers from the identified key information.

#### SubjectiveTest Class

- **Initialization**: Initialized with input text data and the desired number of questions.
- **Question Pattern Definition**: Defines a set of question patterns for subjective-type questions.
- **Sentence Processing**: Tokenizes input text into sentences and identifies noun phrases.
- **Question Generation**: Generates subjective-type questions using the defined patterns and noun phrases.
- **Answer Generation**: Derives answers from the input text.

#### Language Translation Module

The language translation module leverages an API for handling translation requests within the Flask application. It utilizes pre-trained machine translation models to perform text translation.

#### Response Validation

In the context of response validation, the Levenshtein distance algorithm is utilized to measure the similarity between the user's response and the expected or original answer.

**Functions Used to Find the Match Percentage**:

- **similarityPercentage() Method**: Calculates the similarity percentage between two strings using the Levenshtein distance algorithm.
- **levenshteinDistance() Method**: Computes the Levenshtein distance between two strings.

<img width="619" alt="Screenshot 2024-07-05 at 6 28 31 PM" src="https://github.com/saipranavkothapalli/QGen-Atlas/assets/144220767/94d0efc8-b8f6-412c-a965-6f95a44c8841">

## Usage

To use QGen Atlas, follow these steps:

1. Input the text data into the system.
2. Specify the number of queries and the type of questions (objective or subjective).
3. The system will generate the queries and corresponding responses.
4. Validate user responses using the Levenshtein distance algorithm.
5. Utilize the translation API for multilingual support.
