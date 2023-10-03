import streamlit as st


def check_guess(guess, answer):
    if guess and guess.lower() == answer.lower():
        return True, "Correct Answer!"
    elif guess:
        return False, "Sorry, Wrong Answer!"
    return None, ""


def main():
    st.title("Guess the Animal")

    score = 0

    st.write("Which bear lives at the North Pole?")
    guess1 = st.text_input("Your answer for bear:", key='input1')  # Unique key assigned
    is_correct1, response1 = check_guess(guess1, "polar bear")

    if is_correct1 == True:
        score += 1
        st.success(response1)
    elif is_correct1 == False:
        st.error(response1)

    st.write("Which is the fastest land animal?")
    guess2 = st.text_input("Your answer for land animal:", key='input2')  # Unique key assigned
    is_correct2, response2 = check_guess(guess2, "cheetah")

    if is_correct2 == True:
        score += 1
        st.success(response2)
    elif is_correct2 == False:
        st.error(response2)

    st.write("Which is the largest animal?")
    guess3 = st.text_input("Your answer for largest animal:", key='input3')  # Unique key assigned
    is_correct3, response3 = check_guess(guess3, "blue whale")

    if is_correct3 == True:
        score += 1
        st.success(response3)
    elif is_correct3 == False:
        st.error(response3)

    st.write("Your Score is:", score)


if __name__ == "__main__":
    main()
