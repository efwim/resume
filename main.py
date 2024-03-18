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
        modebar_remove=['lasso', 'select','toimage', 'pan'],
        height=500,
        font=dict(size=20), 
        yaxis=dict(tickfont=dict(size=20)),
        title_font=dict(size=20)
    )
    return fig

def tools_plot():
    tools = ["Python", "C/C++", "HTML/CSS/JavaScript/Java", "R", "SQL", "Dart"]
    projects = [6, 1, 1, 2, 1, 2]

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
        title='Experience Based on Projects',
        title_font=dict(size=20),
        showlegend=False
    )
    return fig

def cgpa_plot():
    years = ['Y1-S1', 'Y1-S2', 'Y2-S1', 'Y2-S2', 'Y3-S1', 'Y4-S1'] #, 'Y4-S2']
    courses_taken = [4, 9, 7, 7, 8, 6] 
    cgpa = [3.67, 4.12, 3.97, 4.06, 4.08, 4.14]    

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
        'Subcategory': ['Extraverted', 'Introverted', 'Intuitive', 'Observant', 'Thinking', 'Feeling', 'Judging', 'Prospecting', 'Assertive', 'Turbulent'],
        'Values': ['28%', '72%', '17%', '83%', '65%', '35%', '99%', '1%', '42%', '58%']
    }

    df = pd.DataFrame(data)
    df['Text'] = df['Subcategory'] + '  ' + df['Values']
    category_order = ['Energy', 'Mind', 'Nature', 'Tactics', 'Identity']

    fig = px.bar(df, x="Values", y="Category", color="Subcategory", orientation='h', text='Text', category_orders={"Category": category_order})
    fig.update_traces(textfont=dict(size=15))
    fig.update_layout(
        title='My MBTI is Logistician ISTJ-T',
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
    st.markdown("<h5 style='text-align: left'>🎓 Expected to graduate in June 2024.</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: left'>💼 Seeking a full-time position in data science or as a data analyst, with a desired start date by July 2024.</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: left'>🪪 As an international candidate, I will require an Employment Pass to join the team.</h5>", unsafe_allow_html=True)
    st.divider()
    st.header("Here's a quick summary of me using data visualization plots")
    st.plotly_chart(company_plot())
    st.divider()
    st.plotly_chart(tools_plot())
    st.divider()
    st.plotly_chart(cgpa_plot())
    st.divider()
    st.plotly_chart(language_plot())
    st.divider()
    col1, col2 = st.columns([1, 1])
    with col1:
        st.plotly_chart(mbti_plot(), use_container_width=True)
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.image('image/istj.png', use_column_width=True)

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
    st.subheader("Bachelor of Science in Data Science and Artificial Intelligence")
    st.write("- Direct honours programme with expected graduation in June 2024")
    st.write("- Pursuing a Minor in Modern Languages")
    st.write("- Skills:  Machine Learning,  Deep Learning,  Data Visualization,  Data Wrangling,  Statistical Analysis,  Data Scraping,  Data Querying,  Software Development,  Languages")
    st.divider()
    st.header("Projects")
    selected_tool = st.selectbox('Filter projects by tool used', ['Python', 'R', 'Dart', 'Others'], index=0)
    
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
            st.write("- **WORK IN PROGRESS**")
            st.write("- Developing an engaging memory game application that incorporates efficient hand gesture recognition technology using Flutter and Media Pipe libraries")
        with col2:
            st.image('image/fyp.jpg', use_column_width=True) 

        st.divider()

        st.subheader("Software Engineering")
        col1, col2 = st.columns([1, 1]) 
        with col1:
            st.markdown("#### 'Software Application for Building the Smart Nation'")
            st.write("- **SmartRide** enables customers to efficiently compare prices and durations across various travel methods in Singapore.")
            st.write("- Developed an Android application using Flutter Dart, taking charge of both frontend and backend development.") 
            st.write("- Implemented essential features such as integration with Firebase and Google Maps API")
            st.write("- For **TAXI**, I obtained the driving distance from Google Maps and multiplied it by the distance and time-based unit fare obtained from LTA, added by the flag-down fare")
            st.write("- For **PUBLIC TRANSPORT**, I obtained the direction from Google Maps. Direction could be segregated into categories: only bus, only MRT, both bus and MRT. For each category, I created different functions and calculated based on the unit fare provided by LTA")
            st.write(" - I used Firebase for sign up, login, reset password, forget password features")
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
            st.write("- Studied Chinese from Primary to Junior College where I achieved an A in Cambridge AS Level Chinese")
            st.write("- Studying Korean as an elective in NTU. Achieved an A+ from Level 1 to 3. This semester I am studying Level 4")
            st.write(f"- Studying Japanese with Duolingo, 🔥{get_streak()}")
            st.write("- Took Thai Level 1 in Year 2 Semester 1 and got an \"A\"")
            st.write("- Goal is to learn sign language and braille")
    with col2:
            st.image('image/language.jpg', use_column_width=True, caption='Me and my boyfriend with our Korean teacher') 

    st.divider()

    st.subheader("Crocheting and Puzzles")
    col1, col2 = st.columns([1, 1]) 
    with col1:
            st.write("- Started crocheting in April 2023. So far I made: a turtle coaster, a clam, and a pink cat that looks like a pig😭")
            st.write("- Frequently watch Kdramas, KVariety shows and anime")
            st.write("- Enjoy building nano-block figures and puzzles, especially completing a 2000-piece puzzle and destroying it to rebuild it again 😝")
    with col2:
            st.image('image/crochet.jpg', use_column_width=True, caption="My turtle coaster") 

    st.divider()

    st.subheader("Food Blogging")
    col1, col2 = st.columns([1, 1]) 
    with col1:
            st.write("- I love eating and I can eat a lot")
            st.write("- The worst thing to lose in life is to lose your ability to taste")
            st.markdown("- I started an Instagram food blog in April 2023: [Click here to visit my profile](https://instagram.com/heaven_a_foodcoma?igshid=NGVhN2U2NjQ0Yg==)")
            st.write("- My favorite place for mala xiang guo is at JEM's Kopitiam")
            st.write("- Best places for waffles is DOPA (soft waffle) or Ree and Mummy (crispy waffle)")
            st.write("- No, this is not sponsored 🤭")
    with col2:
            st.image('image/waffle.jpg', use_column_width=True, caption="Ree and Mummy at Katong V") 

def main(): 
    st.sidebar.image('image/me.jpg', use_column_width=True)

    st.sidebar.markdown("<h1 style='text-align: center'>Angelin Grace Wijaya</h1>", unsafe_allow_html=True)
    st.sidebar.markdown("<p style='text-align: center'>A senior in Nanyang Technological University, pursuing a Bachelor's Degree in Data Science & Artificial Intelligence with a Minor in Modern Languages.</p>", unsafe_allow_html=True)

    st.sidebar.markdown("""
    <div style="display: flex; justify-content: center;">
        <a href='mailto:angelingracewijaya@gmail.com'><img src='https://img.icons8.com/color/48/000000/new-post.png' width='30' style='margin-right: 20px;'></a>
        <a href='http://www.linkedin.com/in/angelin-wijaya-4870a2220'><img src='https://img.icons8.com/color/48/000000/linkedin.png' width='30'></a>
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
