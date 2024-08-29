import streamlit as st
import requests

# Define the API token and URL
API_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/google-bert/bert-large-uncased-whole-word-masking-finetuned-squad"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

# Function to query the Hugging Face API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError as e:
            st.error(f"Error decoding JSON: {e}")
            st.error(f"Raw response: {response.text}")
    else:
        st.error(f"Request failed with status code {response.status_code}")
        st.error(f"Raw response: {response.text}")
    return None

# Streamlit app
def main():
    st.title("SMVDU Information Chatbot")
    # Display the university icon
    st.image("university_icon.png", width=100)  # Adjust width as needed
    
    # Define the context
    context = """
    You are an AI trained to provide information **only** from the following context. Do not use any other information, knowledge, or data that is not explicitly mentioned here. If the answer to a question is not in the provided context, respond with "I can only provide information based on the context given. Please refer to the official sources for more details."
    
        - About University
        Shri Mata Vaishno Devi University (SMVDU) was established under an Act of J&K State Legislature in 1999 as a fully residential and technical university, the first of its kind in J&K. Recognized by UGC under Section 2(f) & 12(B) of the UGC Act of 1956, the university receives funding from UGC. The university ranked 26th among Architecture Institutions, 101-150 among Engineering Institutions and 151-200 among the top Universities in the National Institutional Ranking Framework (NIRF 2023) declared by the MHRD, Govt. of India.
    
        - Core Values
        Academic Integrity and Accountability. Respect and Tolerance for the views of every Individual. Attention to issues of National relevance as well as of global concern. Appreciation of intellectual excellence and creativity. Ceaseless aptitude of scientific exploration.
    
        - Vision of the University
        Establishment of a Scientific & Technical University of Excellence to nurture young talented human resources for the service of Indian Society & the World at large, preserving the integrity and sanctity of human values.
    
        - Mission of the University
        The Mission of the University is the pursuit of Education, Scholarship, and Research and its application to the Society at the highest International levels of excellence.
    
        - How to reach?
        The university campus is located 14 km short of the holy town of Katra, and 40 km from Jammu, India. The campus is well-connected by Road, Rail & Air. Maps: https://goo.gl/maps/Z4tU8J7k9gU8n4b19.
    
        - Office & Administration
        His Excellency the Lieutenant Governor of J&K, Sh. Manoj Sinha is the Chancellor of the university, and Prof. (Dr.) Pragati Kumar is the Vice-Chancellor of the university. Sh. Ajay Kumar Sharma (JKAS) is the Registrar of the university.
    
        Establishment
        Shri Mata Vaishno Devi University was established under an Act of J&K State Legislature in 1999 as a fully residential and technical university, the first of its kind in J&K. Recognized by UGC under Section 2(f) & 12(B) of the UGC Act of 1956.
    
        - The Campus
        The University is located on 470 acres of land in the lap of Trikuta Hills, the abode of Shri Mata Vaishno Devi at about 2700 feet above sea level. The pyramidal type architecture merges beautifully with the valley-like ambiance of the surrounding serene hills. The surrounding green hills and the perennial stream of Jhajjar in the east minimize the effects of hot and cold winds and produce a pollution-free atmosphere on the campus. The average day temperature in summer is around 35 degrees Celsius, 4 degrees Celsius lesser than the surrounding areas of the Jammu region, and the maximum and minimum temperatures in winter are about 14 and 5 degrees Celsius respectively. Moderately high hills full of trees and plants on the western side of the campus shield the campus, particularly the residential zone, from the long summer afternoons. The slight incline of the campus provides an ideal place for endurance exercises and the spiritual influence of the Divine Mother and Holy Shrine is palpable on the campus, which helps add a spiritual dimension to the quality of scientific, technical, and management education and life on the campus. An early morning and late evening walk, along the Shrine Axis and other loop roads, surrounded by evenly placed lovely trees and a clear sky with sparkling stars, is very refreshing for the body, mind, and soul.
    
        - Establishment of SMVDU
        Shri Mata Vaishno Devi University (SMVDU) has been established under THE JAMMU AND KASHMIR SHRI MATA VAISHNO DEVI UNIVERSITY ACT, 1999, an Act of the J&K State Legislature (ACT No. XII of 1999 dated 12th May 1999) as an autonomous, highly technical, and fully residential university. The University started functioning as an academic unit in August 2004 when it was inaugurated on 19th August 2004 at the hands of the then Hon’ble President of India Dr. A.P.J Abdul Kalam. Dr. Kalam also delivered the first lecture to the students of the University.
    
        - Recognition
        The University is approved by UGC under Section 2(F) & Section 12(B) of the UGC Act of 1956. The technical programs of the University are recognized by AICTE (All India Council of Technical Education) while the Architecture program is recognized by the Council of Architecture.
    
        - Funding
        The University receives funding from Shri Mata Vaishno Devi Shrine Board, an autonomous Board set up in August 1986 under the provisions of The Jammu and Kashmir Shri Mata Vaishno Devi Shrine Act, 1986 of J&K State Legislature. The University also gets funds from the J&K Government. The University is also a participating institution under the World Bank-assisted TEQIP-III Project of MHRD, Government of India, and has been getting funds under this scheme.
    
        - Logo
        The Design of the logo looks like a Lotus, a symbol of regeneration or a flame. If we see it from a particular angle, it also looks like ‘OM’, the Supreme Word. The three green bars are symbolic representations of three holy peaks of Trikuta Hills and/or the three ‘pindies’ in Shri Mata Vaishno Devi Shrine. The Sun, the giver of Light, Warmth, Time, Direction, Life Force, Energy, Power, Radiance, and Enlightenment, has been shown surrounded by radiating rays going out to nine planets of the Solar System. All this is, however, left to the imagination of the viewer. The English version of the motto is “GOD (BRAHMA) IS SCIENCE”. ‘Brahma’ has been defined as something or someone who nourishes the universe and makes it grow. Science matches the definition wonderfully because science over the years has also done the same. If the world population is any indication, science has done very well indeed. We have not only become the dominant species, but we also have grown to unprecedented numbers. Moreover, the reach of modern scientists has spread much beyond the sun and the moon, and they are now eyeing the far reaches of the universe from where even the light takes years and centuries to reach the earth. Science has given man god-like powers to create and destroy and so far he has used these powers more or less responsibly. Let us hope the good sense continues to prevail and mankind continues to expand the boundaries of Human Knowledge, so that science and spirituality ultimately meet in a confluence of superhuman achievements. Link - https://smvdu.ac.in/wp-content/uploads/2022/03/logo-600-300x223.png
    
        - Academics at SMVDU
        At Shri Mata Vaishno Devi University (SMVDU), students experience a distinct teaching-learning process. Inspired by the Indian Institutes of Technology (IIT) system, known for its global recognition and time-tested success, SMVDU has consciously integrated this model. This adoption has resulted in a remarkable transformation in pedagogy, far from the mundane. By promoting knowledge acquisition, fostering critical thinking, and enhancing problem-solving skills, this IIT-inspired teaching and evaluation approach provides a transformative and beneficial educational experience at SMVDU.
    
        - Overview of Academics
        The students at SMVDU experience a remarkable & refreshingly different teaching-learning process which goes beyond the mundane and has been pioneered at the IITs for many decades. Realizing that the IIT system of teaching & evaluation has stood the test of time and is universally acknowledged as a very successful model, SMVDU has very consciously adopted the IIT system of Teaching & Evaluation. Academic Flexibility, Focus on Hands-on Learning, Varied Pedagogy, Mandatory Industrial Interface & Transparent Continuous Evaluation System are the hallmarks of the Academic Process at SMVDU. Extensive usage of varied contemporary pedagogy like Multi-media teaching aids, including Digital Light Projectors, Overhead Projectors, Net Enabled Labs, Video Conferencing, Cut Section Models, Simulation & Analysis Software, Colloquiums, Seminar, Field Trips, Mini & Major Projects enrich the teaching-learning process. SMVDU students are encouraged to break the mould and go beyond their disciplines; inter-disciplinary courses are highly encouraged. Students are provided the flexibility to go beyond the traditional course requirements and choose courses based on their interest and career choice. At SMVDU, you will see a B.Tech student choosing courses on Philosophy & Morals or Languages even in the final year. At SMVDU, we believe that every student needs to garner knowledge in multiple spheres which will give him an edge in the tough and competitive arena of Life. Open & Core Electives are offered to students to make choices based on their interest. There is a strong focus on Laboratory & Project-based learning. Industrial / corporate Training is a mandatory requirement in the curriculum besides the field trips. **Rules & Regulations are subject to change from Time-to-time and will be notified accordingly.
    
        - Faculty of Engineering
        The Faculty of Engineering at SMVDU provides a comprehensive range of educational opportunities. It currently offers Bachelor of Technology (B.Tech) programs in multiple engineering disciplines, equipping students with the skills required in the modern engineering landscape. Furthermore, the faculty is also planning to launch Master of Technology (M.Tech) programs in the near future, aimed at deepening the knowledge and expertise of graduate students. Beyond undergraduate and prospective postgraduate degrees, the Faculty of Engineering provides an enriching environment that fosters innovation, research, and practical application of engineering principles. Students benefit from hands-on learning, industry interactions, and a robust curriculum that prepares them to excel in their chosen fields. Whether aiming for advanced studies or a professional career, students at SMVDU's Faculty of Engineering receive a holistic and cutting-edge education designed to meet the demands of the ever-evolving engineering sector.
    
            - School of Electronics & Communication Engineering
    
                - Programmes
                    - B.Tech. in Electronics & Communication Engineering
                    - M.Tech. in Electronics & Communication Engineering
    
                - Curriculum & Syllabus
                    Details about the curriculum and syllabus can be found on the official university website or by contacting the department directly.
    
                - Training Methodology
                    The school emphasizes hands-on training through labs, projects, and industry interactions.
    
                - Infrastructure
                    The school boasts state-of-the-art laboratories and research facilities. For detailed information, please visit the university's infrastructure page.
    
                - Additional Information
                    Achievements and activities are regularly updated on the university's official website.
    
                - Achievements & Activities
                    - SMVDU Alumnus Bibhor Kumar Singh honored with Shaurya Chakra for Exemplary Bravery.
                    - Ms. Kajal Declared Qualified for the Award of Ph.D. Degree.
                    - Ms. Himani Sharma declared Qualified for the Award of Ph.D.
    
                - Laboratory Infrastructure
                    For details, visit the laboratory infrastructure page on the university's website.
    
                - Faculty List
                    1. **Dr. Anil Kumar Bhardwaj** - Assistant Professor & I/C Head of School. Email: anil.bhardwaj@smvdu.ac.in, Phone: 01991-285524 Extn.: 2333
                    2. **Dr. Manish Sabraj** - Associate Professor. Email: manish.sabraj@smvdu.ac.in, Phone: 01991-285524 Extn.: 2326
                    3. **Dr. Vipan Kakkar** - Associate Professor. Email: vipan.kakar@smvdu.ac.in, Phone: 01991-285524 Extn.: 2339
                    4. **Dr. Amit Kant Pandit** - Professor. Email: amit.pandit@smvdu.ac.in, amitkantpandit@ieee.org, Phone: 01991-285524 Extn.: 2332
                    5. **Dr. Sumeet Gupta** - Associate Professor, Faculty I/C Examination. Email: sumeet.gupta@smvdu.ac.in, sumeet1_gupta@rediffmail.com, Phone: 01991-285524 Extn.: 2327, Phone: 9419201936
                    6. **Dr. Kumud Ranjan Jha** - Professor, I/c. Dean Faculty of Engineering. Email: kumud.ranjan@smvdu.ac.in, jhakr@rediffmail.com, Phone: 01991-285524 Extn.: 2329
                    7. **Dr. Rakesh Kumar Jha** - Associate Professor (on Extra Ordinary Leave). Email: rakesh.jha@smvdu.ac.in, jharakesh.45@gmail.com, Phone: 01991-285524 Extn.: 2245
                    8. **Mr. Shashi Bhushan Kotwal** - Assistant Professor. Email: kotwal.sb@smvdu.ac.in, sbkotwal@gmail.com, Phone: 01991-285524 Extn.: 2331
                    9. **Mr. Ashish Suri** - Assistant Professor. Email: ashish.suri@smvdu.ac.in, Phone: 01991-285524 Extn.: 2337
                    10. **Dr. Neeraj Tripathi** - Assistant Professor. Email: neeraj.tripathi@smvdu.ac.in, ntripathi@lycos.com, Phone: 01991-285524 Extn.: 2328
                    11. **Mr. Swastik Gupta** - Assistant Professor (On-Leave). Email: swastik.gupta@smvdu.ac.in, Phone: 01991-285524 Extn.: 2340
                    12. **Dr. Purnima Hazra** - Assistant Professor. Email: purnima.hazra@smvdu.ac.in, purnimahazra26@gmail.com, Phone: 01991-285524, 9622273338 Extn.: 2344(O), 6344(R)
                    13. **Dr. Vikram Singh** - Assistant Professor. Email: vikram.singh@smvdu.ac.in, vikram.jangra@gmail.com, Phone: 01991-285524, 9466754797 Extn.: 2244
                    14. **Dr. Sachin Kumar Gupta** - Assistant Professor (On Extra Ordinary Leave). Email: sachin.gupta@smvdu.ac.in, sachin.rs.eee@iitbhu.ac.in, sachin.stm02@nctu.edu.tw, Phone: 01991-285524, 9086752707
                    15. **Dr. Vijay Kumar Sharma** - Assistant Professor. Email: vijay.sharma@smvdu.ac.in, Phone: 01991-285524 Extn.: 2241
    
            - School of Computer Science & Engineering
    
                - Description
                The School of Computer Science & Engineering at Shri Mata Vaishno Devi University is dedicated to providing a superior standard of education in the field of computer science. Recognizing the need for experts in the highly competitive global industrial market, the school offers comprehensive B.Tech, M.Tech, and Ph.D. programs. These programs are meticulously designed to cover the breadth and depth of Computer Science & Engineering, cultivating robust theoretical knowledge and practical skills among students. With a strong commitment to research and innovation, the school prepares its students to become future leaders and trailblazers in the evolving landscape of computer science and engineering. This blend of rigorous academics and an emphasis on cutting-edge research makes it an outstanding institution for computer science education.
    
                - Programmes Offered
                    - B.Tech in Computer Science & Engineering
                    - M.Tech in Computer Science & Engineering
                    - Ph.D. in Computer Science & Engineering
    
                - Curriculum & Syllabus
                Details about the curriculum and syllabus can be found on the official university website or by contacting the department directly.
    
                - BoS (Board of Studies) Minutes of Meeting
                For information on the Board of Studies meetings, please refer to the official university website or contact the department.
    
                - Infrastructure
                The school is equipped with state-of-the-art laboratories and research facilities. For detailed information, please visit the university's infrastructure page.
    
                - Achievements & Activities
                    - Ms. Insha Majeed Declared Qualified for the Award of Ph.D. Degree.
                    - SMVDU Researcher declared Qualified for the Award of Ph.D. Degree.
                    - SMVDU Student shines with Prestigious Pre-Placement Offer at MoFi Network Inc.
                    - View All Achievements on the official university website.
    
                - Laboratory Infrastructure
                For details about laboratory infrastructure, visit the laboratory infrastructure page on the university's website.
    
                - Faculty List
                    1. **Dr. Baij Nath Kaushik** - Associate Professor & Head of School. Email: baijnath.kaushik@smvdu.ac.in, Phone: 01991-285524 Extn.: 2323
                    2. **Dr. Manoj Kumar Gupta** - Associate Professor. Email: manoj.gupta@smvdu.ac.in, Phone: 9458393844
                    3. **Dr. Ajay Kaul** - Associate Professor. Email: ajay.kaul@smvdu.ac.in, Phone: 01991-285524 Extn.: 2306
                    4. **Mr. Manoj Kumar Verma** - Assistant Professor. Email: manoj.kumar@smvdu.ac.in ; vermamk@gmail.com, Phone: 01991-285524 Extn.: 2314(O), 6314(R)
                    5. **Dr. Naveen Kumar Gondhi** - Assistant Professor. Email: naveen.gondhi@smvdu.ac.in; naveenkumargondhi@gmail.com, Phone: 01991-285524 Extn.: 2311
                    6. **Sonika Gupta** - Assistant Professor. Email: sonika.gupta@smvdu.ac.in, Phone: 01991-285524 Extn.: 2308
                    7. **Dr. Sunanda** - Assistant Professor. Email: sunanda.gupta@smvdu.ac.in ; leo_sunanda@yahoo.com, Phone: 01991-285524 Extn.: 2309
                    8. **Dr. Sakshi Arora** - Assistant Professor. Email: sakshi@smvdu.ac.in ; net_sakshi@yahoo.com, Phone: 01991-285524 Extn.: 2310
                    9. **Dr. Pooja Sharma** - Assistant Professor. Email: pooja.sharma@smvdu.ac.in ; pooja2_2000@yahoo.com, Phone: 01991-285524 Extn.: 2312
                    10. **Mr. Sanjay Kumar Sharma** - Assistant Professor. Email: sanjay.sharma@smvdu.ac.in; sharma1314@gmail.com, Phone: 01991-285524 Extn.: 2313
                    11. **Mr. Deo Prakash** - Assistant Professor. Email: deoprakash@smvdu.ac.in, dp.smvdu@gmail.com, Phone: 01991-285524 Extn.: 2321
                    12. **Mr. Anuj Mahajan** - Assistant Professor. Email: anuj.mahajan@smvdu.ac.in, Phone: 01991-285524 Extn.: 2322
                    13. **Mr. Sudesh Kumar** - Assistant Professor. Email: sudesh.bhadu@smvdu.ac.in, Phone: 01991-285524 Extn.: 2307
    
    
        - Faculty of Sciences
        The Faculty of Sciences at SMVDU offers a dynamic and rigorous academic environment, fostering a deep understanding of scientific principles and promoting research and innovation. It provides a range of undergraduate, postgraduate, and doctoral programs designed to equip students with both theoretical knowledge and practical skills. The faculty emphasizes hands-on laboratory experience, critical thinking, and interdisciplinary learning, preparing students for diverse careers in science, technology, and related fields. Students at the Faculty of Sciences benefit from a curriculum that integrates foundational science with advanced research opportunities, supported by experienced faculty members and state-of-the-art facilities. This comprehensive approach ensures that graduates are well-prepared to contribute to scientific advancements and address complex challenges in their professional pursuits.
    
        - Faculty of Management
        The Faculty of Management at SMVDU is dedicated to cultivating future business leaders and managers through its robust academic programs. It offers undergraduate, postgraduate, and doctoral degrees that blend theoretical knowledge with practical experience in business and management. The curriculum is designed to provide students with a strong foundation in business principles, critical thinking, and strategic decision-making. Students engage in case studies, internships, and industry projects, gaining real-world insights and developing leadership skills. The faculty emphasizes ethical business practices, innovation, and entrepreneurship, preparing graduates to excel in various sectors and adapt to the evolving business landscape. With a focus on holistic development, the Faculty of Management equips students with the skills, knowledge, and mindset required to succeed in competitive and dynamic business environments.
    
        - Faculty of Humanities & Social Sciences
        The Faculty of Humanities and Social Sciences at SMVDU offers a broad spectrum of programs that delve into the complexities of human culture, society, and behavior. It provides undergraduate, postgraduate, and doctoral degrees that encourage critical thinking, creativity, and a deep understanding of human experiences. The faculty's interdisciplinary approach integrates perspectives from history, literature, philosophy, sociology, and other disciplines, fostering a comprehensive understanding of the human condition. Students engage in research, fieldwork, and experiential learning, gaining insights into social dynamics and cultural diversity. The curriculum emphasizes analytical skills, effective communication, and ethical considerations, preparing graduates to address societal challenges and contribute to the humanities and social sciences fields. Through its diverse academic offerings, the Faculty of Humanities and Social Sciences at SMVDU nurtures intellectual curiosity and a lifelong passion for learning.
    
        - Faculty of Architecture & Design
        The Faculty of Architecture and Design at SMVDU offers innovative programs aimed at shaping the future of the built environment. It provides undergraduate and postgraduate degrees that combine creative design thinking with technical proficiency. The curriculum emphasizes sustainable architecture, urban planning, and interior design, preparing students to address contemporary challenges in these fields. Students engage in studio projects, workshops, and industry collaborations, gaining practical experience and honing their design skills. The faculty's interdisciplinary approach integrates architecture with elements of engineering, art, and environmental science, fostering a holistic perspective on design. Graduates are equipped with the knowledge and expertise to create functional, aesthetic, and sustainable spaces, contributing to the advancement of architecture and design. The Faculty of Architecture and Design at SMVDU is dedicated to nurturing innovative thinkers and skilled professionals who will lead the way in creating a better-built environment.
    
        - Research at SMVDU
        Shri Mata Vaishno Devi University (SMVDU) is dedicated to fostering a robust research environment that encourages innovation, discovery, and the pursuit of knowledge. The university's research ethos is grounded in its commitment to addressing complex real-world problems and contributing to the advancement of science, technology, humanities, and social sciences. SMVDU offers extensive research opportunities across various disciplines, supported by state-of-the-art facilities and a collaborative academic atmosphere. Faculty members and students engage in cutting-edge research projects, often in partnership with industry, government agencies, and international institutions. The university's interdisciplinary approach to research ensures that diverse perspectives are considered, leading to comprehensive and impactful solutions. Through its research initiatives, SMVDU aims to enhance academic excellence, drive socio-economic development, and promote sustainable practices. The university is also committed to nurturing the next generation of researchers by providing mentorship, funding, and resources to support their academic and professional growth.
    
        - Admissions
        Shri Mata Vaishno Devi University (SMVDU) offers a range of undergraduate, postgraduate, and doctoral programs across various disciplines. Admissions to these programs are based on merit and eligibility criteria set by the university. The admission process typically involves entrance examinations, personal interviews, and academic record evaluations. Prospective students are encouraged to visit the university's official website for detailed information on admission requirements, application procedures, and important dates. SMVDU also provides scholarships and financial aid to deserving students, ensuring that talented individuals from diverse backgrounds have the opportunity to pursue higher education. The university's admissions office is available to assist applicants with any queries and guide them through the application process.
    
        - Student Life
        Shri Mata Vaishno Devi University (SMVDU) offers a vibrant and enriching student life, with a range of activities and facilities designed to enhance the overall university experience. Students at SMVDU have access to modern amenities, including well-equipped hostels, dining facilities, sports complexes, and recreational areas. The university encourages participation in extracurricular activities, such as clubs, societies, and cultural events, fostering a sense of community and personal development. SMVDU also organizes various workshops, seminars, and conferences, providing students with opportunities to learn and network beyond the classroom. The campus environment is safe, inclusive, and supportive, promoting holistic growth and well-being. With a strong focus on academics, research, and co-curricular engagement, student life at SMVDU is dynamic and fulfilling, preparing individuals for both professional success and personal fulfillment.
    
        - Placements
        Shri Mata Vaishno Devi University (SMVDU) has a dedicated Placement Cell that works tirelessly to provide students with excellent career opportunities. The Placement Cell maintains strong relationships with a wide range of industries and organizations, facilitating campus recruitment drives and internships. Students at SMVDU benefit from comprehensive training programs that include resume building, interview preparation, and soft skills development. The university's emphasis on practical learning and industry interaction ensures that graduates are well-prepared to meet the demands of the job market. SMVDU's Placement Cell also organizes career fairs, industry visits, and guest lectures, providing students with insights into various career paths and industry trends. With a high placement rate and strong alumni network, SMVDU is committed to helping students achieve their career aspirations and secure rewarding positions in their chosen fields.
    
        - Collaborations
        Shri Mata Vaishno Devi University (SMVDU) actively collaborates with leading academic institutions, industries, and research organizations both nationally and internationally. These collaborations aim to enhance the university's academic and research capabilities, provide students and faculty with global exposure, and promote knowledge exchange. SMVDU has established partnerships for joint research projects, faculty and student exchange programs, and collaborative academic initiatives. These partnerships foster innovation, interdisciplinary learning, and the development of cutting-edge technologies. By leveraging these collaborations, SMVDU aims to contribute to the global academic community and address complex challenges through joint efforts.
    
        - Alumni
        Shri Mata Vaishno Devi University (SMVDU) takes pride in its growing network of alumni who have made significant contributions to various fields. The university maintains strong connections with its alumni, encouraging their involvement in mentoring current students, participating in university events, and contributing to academic and professional development initiatives. SMVDU's alumni network provides valuable support to students through internships, job placements, and industry insights. The university regularly organizes alumni meetups, networking events, and webinars to foster a sense of community and facilitate knowledge sharing. By staying engaged with its alumni, SMVDU ensures that its graduates remain connected to their alma mater and continue to contribute to its legacy of excellence.
    
        - Campus Facilities
        Shri Mata Vaishno Devi University (SMVDU) offers a wide range of campus facilities designed to support the academic, social, and personal needs of students. The university campus is equipped with state-of-the-art infrastructure, including modern classrooms, well-equipped laboratories, a central library, and advanced research facilities. Students have access to comfortable and safe residential accommodations, dining services, and healthcare facilities. The campus also features sports complexes, fitness centers, and recreational areas to promote physical well-being and extracurricular engagement. SMVDU provides a conducive environment for learning and personal growth, with a focus on creating a holistic and enriching university experience for all students.
    
        - Support Services
        Shri Mata Vaishno Devi University (SMVDU) is committed to providing comprehensive support services to ensure the well-being and success of its students. The university offers academic advising, career counseling, and mental health support to help students navigate their academic journey and personal challenges. SMVDU also provides financial aid and scholarships to assist students with their educational expenses. The university's support services are designed to create a nurturing and inclusive environment, enabling students to achieve their full potential. With a focus on holistic development, SMVDU ensures that students have access to the resources and guidance they need to succeed both academically and personally.
    
        - Contact Information
        For any inquiries or additional information, please visit the official website of Shri Mata Vaishno Devi University (SMVDU) at https://smvdu.ac.in/. You can also contact the university's administration and support services through the contact details provided on the website. The university is dedicated to assisting prospective students, current students, alumni, and other stakeholders with their questions and needs.
    
        - Contact Information:
        Phone: +91-1991-285524
        Email: info@smvdu.ac.in
        Address: Shri Mata Vaishno Devi University, Kakryal, Katra, Jammu And Kashmir - 182320
    
    The information provided should be strictly related to Shri Mata Vaishno Devi University (also known as SMVDU). Any mention of other universities should be avoided.
    """

    # Initialize session state to store questions and answers
    if "history" not in st.session_state:
        st.session_state.history = []

    # Text input for the user's question
    user_question = st.text_input("Ask a question about SMVDU:")

    if user_question and st.button("Submit"):
        # Query the API
        payload = {"inputs": {"question": user_question, "context": context}}
        result = query(payload)
        
        # Store the question and answer in session state
        if result:
            answer = result.get("answer", "No answer found")
            st.session_state.history.append({"question": user_question, "answer": answer})
            user_question = ""  # Clear input after submission
        
    # Display the history of questions and answers
    if st.session_state.history:
        st.write("### Previous Questions and Answers")
        for entry in st.session_state.history:
            st.write(f"**Question:** {entry['question']}")
            st.write(f"**Answer:** {entry['answer']}")
            st.write("---")

if __name__ == "__main__":
    main()
