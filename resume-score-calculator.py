def resume_score_Calculator()
    score =0
    python = input(" Do you know Python? (yes/no): ")
    ml= input("Do you know Machine Learning? (yes/no): ")
    tensorflow = input("Do you know TensorFlow or PyTorch? (yes/no): ")

    if python == "yes":
        score = score + 10

    if ml == "yes":
        score = score + 10 

    if tensorflow == "yes":
        score=score + 10
    print ("AI Resume Score: ", score)
    if __name__ = "main":
    main()
