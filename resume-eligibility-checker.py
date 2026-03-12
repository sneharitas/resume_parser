
def resume_eligibility_checker()

    name = input("Enter your name:")
    experience = int(input("Enter years of AI/ML experience:"))
    if experience>=3:
        print(name, "is eligible for AI Software Engineer role")
    else:
        print(name, "is eligible for AI intern or Junior ML Engineer role")


if __name__ = "main":
main()
