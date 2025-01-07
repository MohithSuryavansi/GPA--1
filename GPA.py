import streamlit as st
import re

def main():
    st.title("PESU GPA Calculator")
    
    # User SRN Input
    username = st.text_input("Enter your SRN:")
    if username:
        # Updated regex to be more inclusive
        if re.search(r"^PES(1|2|3)UG\d{2}(CS|AM|EC|ME|EE|CE)\d{3}$", username):
            st.success("Username is valid. You can proceed.")
            
            # Semester/Cycle Selection with placeholder
            selected_option = st.selectbox("Select your semester/cycle", ['', 'Physics Cycle', 'Chemistry Cycle'], index=0)
            if selected_option:
                show_entries(selected_option)
        else:
            st.error("Invalid SRN. Access denied.")

def show_entries(selected_option):
    if selected_option == 'Chemistry Cycle':
        gpa_chem()
    elif selected_option == 'Physics Cycle':
        gpa_phy()

def button_submit(to):
    if st.button("Submit"):
        st.info(f"Your GPA is {round(to, 2)}")  # GPA rounded to two decimal places for better precision

def gpa_chem():
    # Input for Chemistry cycle courses and GPA calculation
    col1, col2 = st.columns(2)
    with col1: 
        chem = get_chem()
    with col2:
        python = get_python()
    
    st.divider()
    
    col3, col4 = st.columns(2)
    with col3:
        maths = get_maths()
    with col4:
        epd = get_epd()
    
    st.divider()
    
    col5, col6 = st.columns(2)
    with col5:
        mechanics = get_mechanics()
    with col6:
        constitution = get_constitution()

    total_credits = chem[1] + python[1] + maths[1] + epd[1] + mechanics[1] + constitution[1]
    weighted_sum = chem[0] + python[0] + maths[0] + epd[0] + mechanics[0] + constitution[0]
    
    sgpa = weighted_sum / total_credits
    button_submit(sgpa)

def gpa_phy():
    # Input for Physics cycle courses and GPA calculation
    col1, col2 = st.columns(2)
    with col1:
        phy = get_phy()
    with col2:
        python = get_python()
    
    st.divider()
    
    col3, col4 = st.columns(2)
    with col3:
        maths = get_maths()
    with col4:
        elec = get_elec()
    
    st.divider()
    
    col5, col6 = st.columns(2)
    with col5:
        mechanic = get_mechanical()
    with col6:
        evs = get_evs()

    total_credits = phy[1] + python[1] + maths[1] + elec[1] + mechanic[1] + evs[1]
    weighted_sum = phy[0] + python[0] + maths[0] + elec[0] + mechanic[0] + evs[0]
    
    sgpa = weighted_sum / total_credits
    button_submit(sgpa)

# Input for each course, similar to the original code with GPA calculation logic

def get_chem():
    st.markdown("### Engineering Chemistry")
    st.divider()
    credits = st.number_input("Enter the credits in Chemistry course:", min_value=1, max_value=5)
    marksi1 = st.number_input("Marks obtained in Chemistry ISA1:", value=0, step=1)
    marksi2 = st.number_input("Marks obtained in Chemistry ISA2:", value=0, step=1)
    markse = st.number_input("Marks obtained in Chemistry ESA:", value=0, step=1)
    misc = st.number_input("Marks obtained in Chemistry lab/assignment:", value=0, step=1)
    total = (markse / 2) + (marksi1 / 2) + (marksi2 / 2) + misc
    gp = grade_point(total)
    return gp * credits, credits

def get_python():
    st.markdown("### Python for Computational Problem Solving")
    st.divider()
    credits = st.number_input("Enter the credits in Python course:", min_value=1, max_value=5)
    marksi1 = st.number_input("Marks obtained in Python ISA1:", value=0, step=1)
    marksi2 = st.number_input("Marks obtained in Python ISA2:", value=0, step=1)
    markse = st.number_input("Marks obtained in Python ESA:", value=0, step=1)
    misc = st.number_input("Marks obtained in Python project/assignment:", value=0, step=1)
    total = (markse / 2) + (marksi1 / 2) + (marksi2 / 2) + misc
    gp = grade_point(total)
    return gp * credits, credits

# Similar course input methods for each other course (get_maths, get_epd, etc.) 
# following the same structure as the above get_chem and get_python functions.

def grade_point(marks):
    if 90 <= marks <= 100:
        return 10
    elif 80 <= marks < 90:
        return 9
    elif 70 <= marks < 80:
        return 8
    elif 60 <= marks < 70:
        return 7
    elif 50 <= marks < 60:
        return 6
    elif 40 <= marks < 50:
        return 5
    else:
        return 0

if __name__ == "__main__":
    main()
