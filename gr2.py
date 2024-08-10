import streamlit as st
from textblob import TextBlob
import language_tool_python
from spellchecker import SpellChecker

# Function for spell checking using pyspellchecker
def check_spelling(text):
    spell = SpellChecker()
    words = text.split()
    corrected_words = [spell.correction(word) for word in words]
    corrected_text = ' '.join(corrected_words)
    return corrected_text

# Function for grammar checking
def check_grammar(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text, matches

# Function to further correct specific common issues
def additional_corrections(text):
    text = text.replace('Gets see', "Let's see")
    return text

# Streamlit Interface
st.title("Grammar and Spell Checker")

input_text = st.text_area("Enter Text:", height=200)

if st.button("Check Text"):
    if input_text:
        # Spell Checking
        corrected_spelling = check_spelling(input_text)
        st.subheader("After Spell Check")
        st.write(corrected_spelling)

        # Grammar Checking
        corrected_grammar, grammar_issues = check_grammar(corrected_spelling)
        st.subheader("After Grammar Check")
        st.write(corrected_grammar)

        # Additional Corrections
        final_corrected_text = additional_corrections(corrected_grammar)
        st.subheader("Final Corrected Text")
        st.write(final_corrected_text)

        if grammar_issues:
            st.subheader("Grammar Issues Found")
            for issue in grammar_issues:
                st.write(f"Issue: {issue.message}")
                st.write(f"Suggestion: {issue.replacements}")
                st.write(f"Context: {issue.context}")
                st.write("------")
    else:
        st.write("Please enter some text to check.")
