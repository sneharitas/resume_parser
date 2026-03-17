#step 1 : store resumes as list of strings

resumes = [ 
    "Sneha Shrestha snehashrestha138@gmail.com python sql 3 years experience",
    "Ashim Joshi ashim34@gmail.com java python 2 years experinece",
    "Sangita Shrestha sangitastha23@gmail.com python sql ml 6 years experience",
    "Suraj Shrestha surajkoseli33@gmail.com python sql 3 years experience",
    "Prazwal Wagle prazu79@gmail.com python ml java 6 years experience",
]

#step 2: required skills (tuple)

required_skills = ("python","sql","ml")

# STEP 3: Parse resume
def parse_resume(text):
    words = text.split()

    # Name (first two words)
    name = words[0] + " " + words[1]

    # Email
    email = ""
    for word in words:
        if "@" in word:
            email = word

    # Skills (check using "in")
    skills = []
    if "python" in text:
        skills.append("python")
    if "java" in text:
        skills.append("java")
    if "sql" in text:
        skills.append("sql")
    if "ml" in text:
        skills.append("ml")

    # Experience
    experience = 0
    for i in range(len(words)):
        if words[i] == "years":
            experience = int(words[i-1])

    # Store in dictionary
    resume_data = {
        "name": name,
        "email": email,
        "skills": skills,
        "experience": experience
    }

    return resume_data


# STEP 4: Parse all resumes
parsed_resumes = []

for r in resumes:
    parsed_resumes.append(parse_resume(r))


# STEP 5: Unique skills using set
all_skills = set()

for r in parsed_resumes:
    for skill in r["skills"]:
        all_skills.add(skill)


# STEP 6: Match skills and give score
for r in parsed_resumes:
    score = 0
    for skill in r["skills"]:
        if skill in required_skills:
            score = score + 1
    r["score"] = score


# STEP 7: Rank candidates (simple sorting logic)
for i in range(len(parsed_resumes)):
    for j in range(i+1, len(parsed_resumes)):
        if parsed_resumes[j]["score"] > parsed_resumes[i]["score"]:
            temp = parsed_resumes[i]
            parsed_resumes[i] = parsed_resumes[j]
            parsed_resumes[j] = temp


# STEP 8: Detect duplicates
seen = set()
duplicates = []

for r in parsed_resumes:
    identifier = r["name"] + r["email"]
    if identifier in seen:
        duplicates.append(r)
    else:
        seen.add(identifier)


# STEP 9: Filter by experience
filtered = []

for r in parsed_resumes:
    if r["experience"] >= 3:
        filtered.append(r)


# STEP 10: Report
print("\n=== SHORTLISTED CANDIDATES ===")

for r in filtered:
    print("Name:", r["name"])
    print("Email:", r["email"])
    print("Skills:", r["skills"])
    print("Experience:", r["experience"])
    print("Score:", r["score"])
    print("-------------------")


print("\nUnique Skills:", all_skills)
print("Duplicate Resumes:", len(duplicates))