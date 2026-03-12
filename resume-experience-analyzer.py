def resume_experience_analyzer()

    experience = int(input("Enter years of AI experience: "))
    if experience < 1:
        print("AI Beginner")
    elif experience <=3:
        print(" Junior AI Engineer")
    elif experience <=7:
        print("Mid Level AI Engineer")
    else:
        print("Senior AI Engineer")

if __name__ = "main":
main()
