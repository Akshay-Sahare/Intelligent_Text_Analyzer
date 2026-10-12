def text_analyzer(user_text):
    print("-----------Text analytic process start------------\n")

    if not user_text.strip():
        print("Error:-Empty File ,Text is not available")
        return
    
    char_count=len(user_text)

    word_list=user_text.split()
    word_count=len(word_list)

    positive_word=["good", "great", "excellent", "pass", "correct"]
    negative_word=["bad", "wrong", "fail", "error", "incorrect"]

    pos_score=0
    neg_score=0

    for word in word_list:
        clean_word=word.lower().strip(",.?")
        if clean_word in  positive_word:
            pos_score +=1
        elif clean_word in negative_word:
            neg_score +=1


    if pos_score>neg_score:
       sentiment= "Text is positive"
    elif neg_score>pos_score:
        sentiment="Text is negative"
    else:
        sentiment="neutral, Text does not contain any positive or negative words"


    #printing final report
    print(f"User text is :-{user_text}")
    print(f"Length of user text is :-{char_count}")
    print(f"Words in text is :-{word_count}")
    print(f"Final sentiment of text is :-{sentiment}")

if __name__=="__main__":
    sample_text="Akshay is a good boy"
    text_analyzer(sample_text)
   
    