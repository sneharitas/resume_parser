def resume_project_counter()
    projects = int(input("How many AI projects are in your portfolio? "))

    Total = []

    for i in range(projects):
        project = input("Enter AI project name: ")
        Total.append(project)

    print("\nYour AI Projects:")

    for i in range(len(Total)):
        print(i+1, ".", Total[i])
    if __name__ = "main":
    main()
