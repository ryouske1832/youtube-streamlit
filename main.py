from datetime import time
from typing import Text
import streamlit as st
import numpy as np
import pandas as pd
import time as time 
from PIL import Image


st.title('Steamlit 超入門')
st.write("progress bar display")

"start!!!"

latest_iteration =st.empty()
bar= st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.01)



'Done!!!'


left_column, right_column = st.beta_columns(2)
button = left_column.button('right column display figure')

if button:
    right_column.write('here is right column')

expander1 = st.beta_expander('aquirement1')
expander1.write('matter1')

expander2 = st.beta_expander('aquirement2')
expander2.write('matter2')

expander3 = st.beta_expander('aquirement3')
expander3.write('matter3')

expander4 = st.beta_expander('aquirement4')
expander4.write('matter4')


