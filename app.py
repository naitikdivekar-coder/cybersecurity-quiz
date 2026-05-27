import streamlit as st

# Setup browser tab title and layout
st.set_page_config(page_title="Cybersecurity Quest", page_icon="🔒", layout="centered")

# 1. SETUP: Your original questions and data structure
questions = [
    {
        "question": "If someone tries to blackmail you online, what should you do?",
        "options": ["1. Tell a parent or teacher", "2. Lock yourself in a room", "3. Do what they ask"],
        "answer": "1. Tell a parent or teacher"  # Updated to match the string selection
    },
    {
        "question": "A gaming app asks for your birthdate and address. What should you do?",
        "options": ["1. Give all details to play", "2. Skip the step or uninstall the app"],
        "answer": "2. Skip the step or uninstall the app"
    },
    {
        "question": "You receive an email with a link from a 'friend' but it looks strange. What's the best move?",
        "options": ["1. Click it immediately", "2. Delete it or ask your friend in person first"],
        "answer": "2. Delete it or ask your friend in person first"
    },
    {
        "question": "Is it safe to use the same password for your email, games, and social media?",
        "options": ["1. Yes, it's easier to remember", "2. No, if one is hacked, they all are"],
        "answer": "2. No, if one is hacked, they all are"
    },
    {
        "question": "What is 'phishing' in the digital world?",
        "options": ["1. Catching digital fish", "2. Fake messages trying to steal your info"],
        "answer": "2. Fake messages trying to steal your info"
    }
]

# 2. SESSION STATE: This remembers the variables when the page reloads
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "quiz_complete" not in st.session_state:
    st.session_state.quiz_complete = False

# Web Page Header
st.title("🛡️ Cybersecurity Quest")
st.write("Answer the following 5 puzzles to test your safety skills!")
st.write("---")

# 3. QUIZ DISPLAY LOGIC
if st.session_state.quiz_complete:
    # --- RESULT PAGE ---
    st.balloons()  # Visual celebration effect
    st.subheader("🏁 Quiz Complete!")
    
    # Large score metric box
    st.metric(label="Your Final Score", value=f"{st.session_state.score} / {len(questions)}")
    
    # Conditional feedback from your original script
    if st.session_state.score >= 4:
        st.success("🎉 GOOD JOB! You are well aware of security measures.")
    else:
        st.warning("⚠️ BETTER BE AWARE! Check security measures and try again.")
        
    # Reset button to start over
        # Reset button to start over
    if st.button("Try Again"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.quiz_complete = False
        st.rerun()


else:
    # --- ONE-BY-ONE QUESTION PAGE ---
    current_idx = st.session_state.current_question
    q = questions[current_idx]
    
    # Progress indicator bar
    st.write(f"**Question {current_idx + 1} of {len(questions)}**")
    st.progress((current_idx) / len(questions))
    
    # Visual question and clickable radio choices
    st.subheader(q["question"])
    user_choice = st.radio("Choose the correct number:", q["options"], index=None)

    
    st.write("---")
    
    # Button text matches context (Submit at the final question)
    is_last_question = (current_idx == len(questions) - 1)
    button_text = "Submit Quiz" if is_last_question else "Next Question →"
    
    if st.button(button_text):
        if user_choice is None:
            st.error("Please pick an answer before clicking next!")
        else:
            # Check accuracy and track points
            if user_choice == q["answer"]:
                st.session_state.score += 1
                
            # Change state to move forward
            if is_last_question:
                st.session_state.quiz_complete = True
            else:
                st.session_state.current_question += 1
                
            st.rerun()
