# Baby Names A to Z!

Discover every possible baby name in the English language.

## What is this?
This is a simple Python script that takes the number of letters as input and generates all possible combinations of letters from A to Z, saving them in a SQL database file. The first letter of each name is capitalized.

## Who is this for?
This script is designed for anyone looking to brainstorm and find their next baby name.

## How to run?
Running the script is straightforward:
1. Download the Python script `babynames-a-to-z.py`. You can find the latest version in the releases section.
2. Execute the script. It will prompt you to enter the number of letters. Type in your desired number to generate a `.db` file containing the combinations.

## How to use?
You will need a database viewer, such as DB Browser for SQLite, to view the generated database file. This tool is available for free. Familiarity with SQL will help you make the most of this project.

### Example 1
To find 4-letter names starting with 'M' and ending with 'A', run the following query in DB Browser:
```sql
SELECT combination 
FROM combinations 
WHERE 
    combination LIKE 'm%' 
    AND 
    combination LIKE '%a';
```
Output:
![image](https://github.com/user-attachments/assets/a9c512ef-b9a1-4657-b05b-7f4345f42fcc)

### Example 2
To find 4-letter names starting with 'A', ending with 'A', but not ending with 'la', use this query:
```sql
SELECT combination 
FROM combinations 
WHERE 
	combination LIKE 'a%' 
	AND 
	combination LIKE 
	'%a' 
	AND 
	combination NOT LIKE '%la';
```
Output:
![image](https://github.com/user-attachments/assets/6f5e2042-c09c-4a7c-a2ca-689a18c30ce9)

Feel free to adjust any part of this further if you have specific preferences!

## Caution
Generating a database of 5-letter combinations can create a file size of nearly 180MB. Please consider your disk space before running the script with higher letter counts.

## Collaboration
I am open to collaboration on this project. If you have ideas for improvements or would like to build on this work, feel free to reach out.
