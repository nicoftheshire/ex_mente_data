---
title: "Ex Mente Python Assignment: Python Package Development, Git Repository, and Data Analysis"
author: "Stefan van der Merwe (stefan.vandermerwe@ex-mente.co.za)"
date: "2023-07-18"
geometry: "left=2cm,right=3cm,top=1.5cm,bottom=2cm"
output: pdf_document
---

## Objective:

The objective of this assignment is to assess the junior software developer's Python skills, including package development, Git repository management, file I/O, subprocess handling, and data analysis using Pandas and Matplotlib. The candidate will be required to create a Python package, implement specific functionalities involving file operations and subprocess handling, and perform data analysis using Pandas and data visualization using Matplotlib. Additionally, the candidate will need to write a short report explaining their development process, choices made, and the rationale behind those choices.

## Requirements:

1. Python Package Development:

   - Create a Python package named "DataAnalysis" with the following functionalities:

     - File Operations:

       - Implement a function that reads a CSV file and returns a Pandas DataFrame containing the data.
       - Implement a function that writes a given Pandas DataFrame to a CSV file.

     - Data Analysis:
       - Implement a function that takes a Pandas DataFrame as input and performs the following tasks:
         - Calculates summary statistics (e.g., mean, median, standard deviation) for numerical columns.
         - Generates descriptive statistics (e.g., count, unique values, frequency) for categorical columns.
         - Provides basic data visualization using Matplotlib, such as histograms or bar plots.

2. Git Repository Management:

   - Set up a Git repository to track the development of the "DataAnalysis" package.
   - Maintain version control using Git by committing and pushing changes at appropriate stages of development.
   - Create at least three branches:
     - "development": Used for implementing and testing new features.
     - "bug-fix": Used for fixing any reported bugs or issues.
     - "documentation": Used for updating the documentation and writing the report.
   - Demonstrate merging of branches and resolving any merge conflicts, if necessary.

3. Subprocess Handling and File I/O:

   - Implement a function within the "DataAnalysis" package that uses the `subprocess` module to execute the rsync command, copying a specified results file to a specified directory.
     - The function should take the source file path, destination directory path, and any necessary rsync options as input.
     - Handle any errors or exceptions that may occur during the subprocess execution.

4. Data Analysis and Visualization:

   - Demonstrate the functionality of the "DataAnalysis" package by performing data analysis and visualization on a given CSV file.
     - Read the CSV file using the implemented file reading function.
     - Perform data analysis using Pandas to generate summary statistics and descriptive statistics.
     - Use Matplotlib to visualize the data, creating at least two meaningful plots or charts.

5. Documentation and Report:
   - Write a README.md file for the "DataAnalysis" package, explaining how to install and use the package.
   - Include docstrings in the code for all functions and classes, providing necessary documentation.
   - Write a short report (500-1000 words) detailing the development process, including the following:
     - Introduction: Describe the purpose and scope of the project.
     - Implementation: Explain how the "DataAnalysis" package was designed and structured, including the subprocess handling and file I/O.
     - Challenges: Discuss any difficulties encountered during the development process and how they were resolved.
     - Version Control: Explain the branching strategy used and provide examples of merge operations and conflict resolution.
     - Data Analysis: Describe the dataset used, provide insights gained from the analysis, and showcase the visualizations created.
     - Conclusion: Summarize the overall experience and discuss any future improvements or enhancements.

## Submission Guidelines:

1. The candidate should create a public Git repository on a platform of their choice (e.g., GitHub, GitLab).
2. The Python package and associated code should be organized and committed within the repository.
3. The report should be written in a clear and concise manner, providing adequate explanations and justifications for design choices.
4. The candidate should provide the repository URL and the report document as a submission.

> _**Note:** This assignment aims to assess a broader set of Python skills, including package development, Git repository management, file I/O, subprocess handling, and data analysis using popular packages like Pandas and Matplotlib. It also evaluates the candidate's ability to document their work effectively._
