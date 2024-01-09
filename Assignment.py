# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Welcome to Ghea's Page",
        page_icon="👋",
    )

    st.write("# Welcome to My Page! 👋")

    st.sidebar.success("Cool projects")

    st.markdown(
        """
        This website is part of the TECHIN510 Lab Assignment. If you want to know more about me
        **👈 Select a cool project from the sidebar** 
        ### About
        - Ghea Chrestella Suyono 
        - Linkedin [Linkedin Profile](https://www.linkedin.com/in/suyonoghea/)

        ### Education
        - Grad (on going) in Ms Technology Innovation - University of Washington
        - Undergrad in Banking and Finance - University of London

        ### Work Experience
        - Payment Experience Lead in Gojek Tokopedia
        - Loan PM - SeaGroup, SeaBank
        - PMO, COO Office - SeaGroup
        - Corporate Relationship Manager - OCBC Bank
        - Management Associate - OCBC Bank

        ### Hobbies and Interests
        
        ### Interesting Project
    """
    )


if __name__ == "__main__":
    run()
