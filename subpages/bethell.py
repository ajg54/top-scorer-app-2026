import streamlit as st

st.title("Jacob BEThell")
st.header("Description")
st.write("During the 2025/2026 Ashes Tour, Jacob Bethell finally took Ollie Pope's spot at #3 in the batting order."
         " After that tour, Bethell's Test average stood at 43.27 based on 12 innings (including one not out)."
         " The goal of this sub BEThell is to predict his end of year test average."
         " The upcoming series each consist of three tests: New Zealand (home), Pakistan (home) and SA (away)."
         " The latter series is part of the 2026/2027 tour and it is currently unclear how many tests will be in 2026.")

st.header("Current Wagers")
st.write("So far only Matt has picked a number: 40.")

st.header("Scenario Calculator")
number_of_outs = st.slider("Number of Outs", min_value=0, max_value=18, value=18)
number_of_runs = st.number_input("Number of Runs", min_value=0, max_value=2000, value=684)
if number_of_outs == 0:
    period_average_value = None
else:
    period_average_value = number_of_runs/number_of_outs
period_average_display = st.number_input("Scenario Average (excluding previous performance)",
                                         disabled=True, value=period_average_value)
final_average = st.number_input("Final Average", disabled=True, value=(number_of_runs+476)/(number_of_outs+11))
