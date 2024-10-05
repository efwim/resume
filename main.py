import streamlit as st
from datetime import datetime
from PIL import Image
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd

def company_plot():
    companies = ["Cotton Goods", "TVS Digital"]
    months = [3,6]
    intervals = ["May-Aug 2022", "Jan-Jun 2023"]
    fig = go.Figure()
    for i in range(len(companies)):
        fig.add_trace(go.Bar(
            y=[companies[i]],
            x=[months[i]],
            orientation='h',
            text=intervals[i], 
            textposition='inside', 
            hoverinfo='none',
            showlegend=False
        ))

    fig.update_layout(
        title="Internship Experience",
        xaxis_title="Number of Months",
        modebar_remove=['lasso', 'select','toimage', 'pan'],
        height=500,
        font=dict(size=20), 
        yaxis=dict(tickfont=dict(size=20)),
        title_font=dict(size=20)
    )
    return fig

def tools_plot():
    tools = ["Python", "C/C++", "Java", "R", "SQL", "Dart"]
    projects = [10, 2, 1, 3, 1, 2]

    fig = go.Figure(go.Pie(
        labels=tools,
        values=projects,
        textinfo='label+percent', 
    ))
    fig.update_traces(
        textfont=dict(size=20), 
        hoverinfo='none'  
    )
    fig.update_layout(
        height=500,
        title='Project-Based Tool Experience Distribution',
        title_font=dict(size=20),
        showlegend=False
    )
    return fig

def cgpa_plot():
    years = ['Y1-S1', 'Y1-S2', 'Y2-S1', 'Y2-S2', 'Y3-S1', 'Y4-S1', 'Y4-S2']
    courses_taken = [4, 9, 7, 7, 8, 6, 4] 
    cgpa = [3.67, 4.12, 3.97, 4.06, 4.08, 4.14, 4.23]    

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=years,
        y=courses_taken,
        name='Courses Taken',
    ))

    fig.add_trace(go.Scatter(
        x=years,
        y=cgpa,
        mode='lines+markers',
        name='CGPA',
        yaxis='y2', 
        line=dict(color='#EF553B', width=2)
    ))

    fig.update_layout(
        height=500,
        title='CGPA Through The Semesters',
        modebar_remove=['lasso', 'select','toimage', 'pan'],
        xaxis=dict(title='Year-Semester',tickfont=dict(size=20)),
        yaxis=dict(title='Number of Courses Taken'),
        yaxis2=dict(title='Cumulative GPA', overlaying='y', side='right'),
        legend=dict(x=0, y=1.1),
        title_font=dict(size=20)
    )
    return fig

def language_plot():
    languages = ["English", "Bahasa Indonesia", "Chinese", "Korean", "Japanese"]
    levels = [5, 5, 3, 3, 1]

    fig = go.Figure(go.Bar(
        x=levels,
        y=languages,
        orientation='h'
    ))

    fig.update_layout(
        title='Language Proficiency',
        modebar_remove=['lasso', 'select','toimage', 'pan'],
        height=500,
        xaxis=dict(tickvals=[0, 1, 2, 3, 4, 5], ticktext=["None", "Elementary", "Limited", "Professional", "Full Professional", "Native"]),
        yaxis=dict(tickfont=dict(size=20)),
        title_font=dict(size=20)
    )
    return fig

def mbti_plot():
    data = {
        'Category': ['Energy', 'Energy', 'Mind', 'Mind', 'Nature', 'Nature', 'Tactics', 'Tactics', 'Identity', 'Identity'],
        'Subcategory': ['Extraverted', 'Introverted', 'Intuitive', 'Observant', 'Feeling', 'Thinking', 'Prospecting', 'Judging', 'Assertive', 'Turbulent'],
        'Values': ['28%', '72%', '17%', '83%', '35%', '65%', '1%', '99%', '42%', '58%']
    }

    df = pd.DataFrame(data)
    df['Text'] = df['Subcategory'] + '  ' + df['Values']
    category_order = ['Energy', 'Mind', 'Nature', 'Tactics', 'Identity']

    fig = px.bar(df, x="Values", y="Category", color="Subcategory", orientation='h', text='Text', category_orders={"Category": category_order})
    fig.update_traces(textfont=dict(size=15))
    fig.update_layout(
        title='',
        modebar_remove=['lasso', 'select','toimage', 'pan'],
        title_font=dict(size=20),
        hovermode=False, 
        xaxis_visible=False, 
        yaxis_visible=False, 
        showlegend=False,)
    return fig


def home():
    st.title("Greetings! I am Angel")
    st.header("Explore my dashboard to get to know me")
    st.markdown("<h5 style='text-align: left'>🧭 Navigate through the pages using the sidebar.</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: left'>🎓 Graduated in June 2024 with a Bachelor of Science (Hons).</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: left'>🪪 As an international candidate, I will require an Employment Pass to join the team.</h5>", unsafe_allow_html=True)
    st.divider()
    st.header("Here's a quick summary of me using data visualization plots")
    st.plotly_chart(company_plot())
    st.divider()
    st.plotly_chart(tools_plot(), use_container_width=True)
    st.write("This pie chart visualizes my experience with various tools based on the projects I completed during my university studies. Each segment represents the proportion of projects utilizing a specific tool, calculated by dividing the number of projects using that tool by the total number of projects completed.")
    st.divider()
    st.plotly_chart(cgpa_plot())
    st.divider()
    st.plotly_chart(language_plot())
    st.divider()
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("#### Myers–Briggs Type Indicator (MBTI)")
        st.write("My personality type, ISTJ-T, is known for being:")
        istj_list = [
            "Honest and Direct",
            "Disciplined",
            "Very Responsible",
            "Calm and Practical",
            "Organized and Effective",
            "Research-Oriented"
        ]
        istj_markdown = "\n".join([f"- {istj}" for istj in istj_list])
        st.markdown(istj_markdown)
        st.markdown("[Click here](https://www.16personalities.com/istj-personality) to read more about ISTJs")
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.image('image/istj.png', use_column_width=True)

    st.markdown("##### Test results and interpretation")
    col1, col2 = st.columns([1, 1])
    with col1:
        istj2_list = [
            "**Introverted**: prefer fewer, yet deep and meaningful, social interactions and calmer environments.",
            "**Observant**: pragmatic, down-to-earth, and have a strong focus on current and likely events.",
            "**Thinking**: focus on objectivity and rationality, and may prioritize effectiveness over social harmony.",
            "**Judging**: decisive, thorough, and highly organized. They value clarity, predictability, and closure, preferring structure and planning to spontaneity.",
            "**Turbulent**: tend to be success-driven, perfectionistic, and eager to improve.",
        ]
        istj2_markdown = "\n".join([f"- {istj}" for istj in istj2_list])
        st.markdown(istj2_markdown)
    with col2:
        st.plotly_chart(mbti_plot(), use_container_width=True)

def work():
    st.title("Work Experience")
    st.header("TVS Digital, Singapore")
    col1, col2 = st.columns([1, 1]) 

    with col1:
        st.subheader("Product Management Intern")
        st.markdown("#### Accomplishment")
        tasks_list = [
            "Managed more than 500 backlogs, driving the successful completion of 3 Functional Acceptance Tests (FAT) and 2 User Acceptance Tests (UAT).",
            "Performed meticulous manual testing, documenting, and resolving over 200 bugs or issues, while maintaining a well-organized database of over 300 test cases.",
            "Developed user manuals for clients and comprehensive product configuration documents for the team, improving efficiency of customizing clients’ applications by 85%."
        ]
        tasks_markdown = "\n".join([f"- {task}" for task in tasks_list])
        st.markdown(tasks_markdown)

        st.markdown("#### Tools")
        tools_list = [
            "JIRA",
            "Confluence",
            "Microsoft Excel",
            "Microsoft Powerpoint"
        ]
        tools_markdown = "\n".join([f"- {tool}" for tool in tools_list])
        st.markdown(tools_markdown)
    with col2:
        st.markdown("<h3 style='text-align: right'>Jan-Jun 2023</h3>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.image('image/tvs.jpg', use_column_width=True)

    st.divider()
    
    st.header("Cotton Goods, Bandung, Indonesia")
    col1, col2 = st.columns([1, 1]) 

    with col1:
        st.subheader("Project Management Intern")
        st.markdown("#### Accomplishment")
        tasks_list = [
            "Enhanced Shopee and Tokopedia shop chat performance from 70% to 91% by addressing customer concerns effectively.",
            "Optimized inventory management and sales performance by 30% through strategic construction of production backlog for restocks and slow-moving products.",
            "Improved product quality and customer satisfaction from an average rating of 3.5 to 4.8 stars by analyzing customer ratings and comments and implementing improvement plans."
        ]
        tasks_markdown = "\n".join([f"- {task}" for task in tasks_list])
        st.markdown(tasks_markdown)

        st.markdown("#### Tools")
        tools_list = [
            "Microsoft Excel"
        ]
        tools_markdown = "\n".join([f"- {tool}" for tool in tools_list])
        st.markdown(tools_markdown)
    with col2:
        st.markdown("<h3 style='text-align: right'>May-Aug 2022</h3>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.image('image/cottongood.jpg', use_column_width=True)

def education():
    st.title("Education")
    st.header("Nanyang Technological University, Singapore")
    st.subheader("Bachelor of Science (Hons) in Data Science and Artificial Intelligence")
    st.write("- Graduated in June 2024")
    st.write("- Minor in Modern Languages (Korean)")
    st.write("- **Skills:**   Machine Learning,  Deep Learning,  Data Visualization,  Data Wrangling,  Statistical Analysis,  Data Scraping,  Data Querying,  Software Development,  and more")
    st.divider()
    st.header("Projects")
    selected_tool = st.selectbox('Filter projects by tool used', ['Python', 'R', 'Dart', 'Others'], index=2)
    
    if selected_tool == 'Python':
        st.subheader("Data Visualization")
        col1, col2 = st.columns([1, 1]) 
        with col1:
            st.markdown("#### 'Depression Around The World'")
            st.write("- Used Plotly to make interactive visualization through widgets and animations")
            st.write("- Applied data visualization principles to make effective visualizations")
            st.markdown("- Watch Video: [Click here](https://youtu.be/0Mc-5_6lgLQ)")
        with col2:
            st.image('image/cz4124.png', use_column_width=True) 

        st.divider()

        st.subheader("Machine Learning")
        col1, col2 = st.columns([1, 1]) 
        with col1:
            st.markdown("#### 'Store Item Demand Forecasting Challenge'")
            st.write("- Developed a time-series model to forecast 3 months of sales data for each item across 10 stores")
            st.write("- Achieved a score within the Top 5% by identifying seasonality and trend components and passing them as features to XGBRegressor")
        with col2:
            st.image('image/cz4041.png', use_column_width=True) 
        
        st.divider()

        st.subheader("Data Products")
        col1, col2 = st.columns([1, 1]) 
        with col1:
            st.markdown("#### 'Innovative Stock Analysis Tool: Fusing News Sentiment and Technical Indicators'")
            st.write("- Incorporated API to retrieve stock-related news articles")
            st.write("- Created a stock movement prediction model by using sentiment polarity scores from news articles as features")
        with col2:
            st.image('image/cz4125.jpg', use_column_width=True) 

        st.divider()

        st.subheader("Neural Networks and Deep Learning")
        col1, col2 = st.columns([1, 1]) 
        with col1:
            st.markdown("#### 'State-of-the-Art Model for Material Recognition'")
            st.write("- Utilized InceptionV3 and Xception models from Keras deep learning library to build a material recongition model")
            st.write("- Implemented transfer learning, data augmentation, and fine-tuning techniques")
        with col2:
            st.image('image/cz4042.png', use_column_width=True) 

        st.divider()

        st.subheader("Simulation Techniques in Finance")
        col1, col2 = st.columns([1, 1]) 
        with col1:
            st.markdown("#### 'Product Analysis on Swiss Market Index'")
            st.write("- Identified potential risks and opportunities in the Swiss Market Index, assisting in portfolio management decisions")
            st.write("- Performed analysis using 'Black Scholes' and 'Heston' models, while applying variance reduction techniques and parameter calibration to enhance accuracy")
        with col2:
            st.image('image/mh4518.png', use_column_width=True) 
        
        st.divider()

        st.subheader("Introduction to Data Science")
        col1, col2 = st.columns([1, 1]) 
        with col1:
            st.markdown("#### 'IBM HR Analytics Employee Attrition & Performance'")
            st.write("- Performed data cleaning and exploratory data analysis to predict possible reasons for employee attrition")
            st.write("- Developed and fine-tuned a random forest model with GridSearchCV, achieving a high accuracy of 95% and 90% on train and test datasets, respectively")
        with col2:
            st.image('image/cz1016.png', use_column_width=True)

    elif selected_tool == 'R':
        st.subheader("Regression Analysis")
        st.markdown("#### 'Traffic Monitoring - Multiple Linear Regression Problem'")
        st.write("Given a multiple linear regression problem, employed techniques to check adequecy of full model and come up with a reduced model:")
        st.write("- Conducted t tests, F tests, R-Squared statistic, ANOVA tests")
        st.write("- Performed normality checks, check for time effects, check for sequential dependence and non-constant variance of residuals")
        st.divider()
        st.subheader("Data Analysis with Computer")
        st.markdown("#### 'Business Analysis and Proposal for Superstore'")
        st.write("The objective of the problem is to identify posible solutions for improving the financial performance of a Superstore (from a Kaggle dataset)")
        st.write("- Conducted data cleaning, variable transformation, t-tests and ANOVA tests")

    elif selected_tool == 'Dart':
        st.subheader("Final Year Project")
        col1, col2 = st.columns([1, 1]) 
        with col1:
            st.markdown("#### 'Smartphone-based memory game using physical gestures'")
            st.write("- Featured on NTU College of Computing and Data Science [Technovation 2024](https://www.ntu.edu.sg/computing/news-events/news/technovation-2024) page")
            st.write("- Developed a memory game application centered around gesturing, with a focus on gamifying memory training and enhancing user engagement.")
            st.write("- Incorporated visual, auditory cues and hand gestures to reinforce memory recall through multiple senses, thereby providing a more comprehensive and effective cognitive exercise.")
            st.write("- Integrated MediaPipe library for real-time hand recognition within a Flutter-based application.")
            st.write("- Optimized algorithms to interpret gestures accurately during gameplay, enhancing user interaction and experience")
            st.markdown("- Read Paper: [Click here](https://dr.ntu.edu.sg/handle/10356/174871)")
            st.markdown("- Watch Video: [Click here](https://youtu.be/8VpbTkrRP94?si=vxpbMtep4KZfAB_q)")
        with col2:
            st.image('image/fyp_rhythm.png', use_column_width=True) 

        st.divider()

        st.subheader("Software Engineering")
        col1, col2 = st.columns([1, 1]) 
        with col1:
            st.markdown("#### 'Software Application for Building the Smart Nation'")
            st.write("- **SmartRide** enables customers to efficiently compare prices and durations across various travel methods in Singapore.")
            st.write("- Developed an Android application using Flutter Dart, taking charge of both frontend and backend development.") 
            st.write("- For **TAXI**, I obtained the driving distance through Google Maps API and multiplied it by the distance and time-based unit fare obtained from LTA, added by the flag-down fare")
            st.write("- For **PUBLIC TRANSPORT**, I obtained the direction through Google Maps API. Direction could be segregated into categories: only bus, only MRT, both bus and MRT. For each category, I created different functions and calculated based on the unit fare provided by LTA")
            st.markdown("- Watch Video: [Click here](https://youtu.be/2eASCKv2QmM)")
        with col2:
            st.image("image/cz2006.png", use_column_width=True)
    else:
        st.markdown("### SQL")
        st.subheader("Introduction to Databases")
        st.write("- Creating an ER diagram ensuring correct identification of entity sets, relationships, weak entities, subclasses, etc.")
        st.write("- Converting ER diagram into relational schema while specifying the keys, primary key and functional dependencies of each relation")
        st.write("- Implementing database schema using SQL DDL commands")

        st.divider()

        st.markdown("### C/C++")
        st.subheader("Algorithm Design and Analysis")
        st.write("- Integrated InsertionSort and MergeSort algorithms and compared its performance with original MergeSort")
        st.write("- Compared efficiency of Dijkstra's algorithm when the input graph is stored in an adjacency matrix and when it is stored in an array of adjacency list")
        st.write("- Developed a dynamic programming algorithm to compute maximum profit of a knapsack problem")
        
        st.divider()

        st.markdown("### HTML/CSS/JavaScript/Java")
        st.subheader("Coursera Specialization by Duke University")
        st.write("- Built a green screen and different colored filters")
        st.write("- Implemented Caesar and Vigenere Ciphers")
        st.write("- Created a WordGram and Word N-Grams using Markov Model concept")
        st.write("- Developed a Movie Recommendation System")
        st.markdown("- Verify Certificate: [Click here](coursera.org/verify/specialization/63V8YM3AZAFF)")

def get_streak():
    start_date = datetime(2023, 12, 3)
    today = datetime.now()
    days_passed = (today - start_date).days
    streak = 171
    streak_today = 171+days_passed
    return streak_today

def hobby():
    st.title("Hobbies")
    st.subheader("Learning New Languages")
    col1, col2 = st.columns([1, 1]) 
    with col1:
            st.write("- Fluent in English and Bahasa Indonesia")
            st.write("- Studied Chinese from Primary to Junior College where I achieved an \"A\" in Cambridge AS Level Chinese")
            st.write("- Graduated with a Minor in Modern Languages, specifically for Korean")
            st.write("- Obtained an \"A\" grade for Thai Level 1 in university")
            st.write(f"- Studying Japanese with Duolingo with current streak at 🔥{get_streak()}")
            st.write("- Life-long dream to achieve fluency in sign language and braille")
    with col2:
            st.image('image/language.jpg', use_column_width=True, caption='Me and my boyfriend with our Korean teacher') 

    st.divider()

    st.subheader("Food Blogging")
    col1, col2 = st.columns([1, 1]) 
    with col1:
            st.write("- To lose the sense of taste, in my opinion, is among life's greatest losses")
            st.markdown("- Started an Instagram food blog ([@heaven_a_foodcoma](https://instagram.com/heaven_a_foodcoma?igshid=NGVhN2U2NjQ0Yg==)) in 2023")
            st.markdown("- Achieved [Google Local Guide](https://goo.gl/maps/jBfGCdSTLu67BiwQ6) Level 6 with contributions totaling over 700,000 views")
    with col2:
            st.image('image/waffle.jpg', use_column_width=True, caption="Ree and Mummy at Katong V") 
    
    st.divider()

    st.subheader("Crocheting and Puzzles")
    col1, col2 = st.columns([1, 1]) 
    with col1:
            st.write("- Began crocheting in April 2023 and have since crafted a variety of items, including a turtle coaster, clam plushie, and flower bouquet")
            st.write("- Skilled in assembling nano-block figures and puzzles, with achievements including completing a 2000 piece puzzle")
    with col2:
            st.image('image/crochet.jpg', use_column_width=True, caption="Turtle coaster") 

def main(): 
    st.sidebar.image('image/me.jpg', use_column_width=True)

    st.sidebar.markdown("<h1 style='text-align: center'>Angelin Grace Wijaya</h1>", unsafe_allow_html=True)
    st.sidebar.markdown("<p style='text-align: center'>A graduate from Nanyang Technological University with a Bachelor of Science (Hons) in Data Science & Artificial Intelligence</p>", unsafe_allow_html=True)

    st.sidebar.markdown("""
    <div style="display: flex; justify-content: center;">
        <a href='mailto:angelingracewijaya@gmail.com'><img src='https://img.icons8.com/color/48/000000/new-post.png' width='30' style='margin-right: 20px;'></a>
        <a href='http://www.linkedin.com/in/angelin-w-4870a2220'><img src='https://img.icons8.com/color/48/000000/linkedin.png' width='30'></a>
    </div>
    """, unsafe_allow_html=True)

    st.sidebar.divider()
    st.sidebar.title("Navigate")
    selected_section = st.sidebar.selectbox('Select Page', ['Home', 'Work Experience', 'Education', 'Hobbies'], index=0)

    if selected_section == 'Home':
        home()
    elif selected_section == 'Work Experience':
        work()
    elif selected_section == 'Education':
        education()
    elif selected_section == 'Hobbies':
        hobby()

if __name__ == '__main__':
    main()
