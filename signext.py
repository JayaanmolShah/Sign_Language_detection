import streamlit as st
import requests
import streamlit_lottie as stt
import cv2
import mediapipe as mp
from streamlit_option_menu import option_menu

hide_menu="""
<style>
#MainMenu{
    visibility:hidden;
}
</style>
"""

st.set_page_config(
    page_icon="images\signext_logo1.png",
    page_title="Signext"
)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

my_list = []

def main():
    st.markdown(hide_menu,unsafe_allow_html=True)
    st.session_state['page'] = 'welcome_page'
    st.sidebar.image('images\signext_logo.png')
    selected = option_menu(None, ["Home", 'Start Expressing','About Us',"How to Use"], icons=['house','balloon-heart','file-earmark-person','patch-question'], menu_icon="cast", default_index=1,orientation="horizontal")
    if selected=="Home":
        st.session_state['page'] = 'welcome_page'
    if selected=="Start Expressing":
        st.session_state['page'] = 'translate_page'
    if selected=="About Us":
        st.session_state['page'] = 'about_us_page'
    if selected=="How to Use":
        st.session_state['page'] = 'how_to_use_page'


    if 'page' not in st.session_state:
        st.session_state['page'] = 'welcome_page'
    if st.session_state['page'] == 'welcome_page':
        welcome_page()
    elif st.session_state['page'] == 'about_us_page':
        about_us_page()
    elif st.session_state['page'] == 'how_to_use_page':
        how_to_use_page()
    elif st.session_state['page'] == 'translate_page':
        translate_page()
    

def load_lottieurl(url:str):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def welcome_page():
    st.markdown("<h1 style='text-align: center;color:#c45c4c'>Welcome to Signext</h1>", unsafe_allow_html=True)
    st.subheader('where every gesture matters, and every voice is heard.')
    st.write('At Signext, we believe that communication is a fundamental human right. Our mission is to bridge the gap between sign language users and the wider community by providing a platform that seamlessly translates sign language gestures into written text. By harnessing the power of technology, we aim to make communication more inclusive and accessible for everyone, regardless of their hearing ability.')
    lottie_url="https://lottie.host/51647fe1-3703-4c2e-b1f6-8e0d920bdd53/RzIVXCCDBF.json"
    lottie_json=load_lottieurl(lottie_url)
    stt.st_lottie(lottie_json,height=300)
    st.markdown("<h6 style='text-align: center;'>Even without words, you have the power to inspire and uplift others.</h6>", unsafe_allow_html=True)
    

def about_us_page():
    st.markdown("<h1 style='text-align: center;color:#c45c4c'>Welcome to Signext</h1>", unsafe_allow_html=True)
    st.subheader('where every gesture matters, and every voice is heard.')
    st.write('We are a team of passionate developers currently pursuing our Bachelor of Technology (B.Tech) degrees in our second year. Our shared vision is to make a positive impact by leveraging technology to enhance communication and accessibility for individuals who use sign language.')
    st.markdown("<h3 style='text-align: center;color:#b41c0c'>MEET THE TEAM</h3>", unsafe_allow_html=True)
    st.header('')
    t1,t2=st.columns(2)
    t1.image('images\coat jaya.jpeg')
    t2.markdown("<h4 style='color:#4cd4bc'>Jayaanmol Shah</h4>", unsafe_allow_html=True)
    t2.header("")
    t2.write("I'm currently pursuing my B.Tech in Computer Science at AISSMS College, Pune, following diploma in CS from Wadia College. As a passionate full-stack web developer, I enjoy bringing digital ideas to life. Outside of coding, you'll often find me immersed in the world of painting. Let's connect and explore the realms of technology and art together!")
    i1,i2,i3=t2.columns(3)
    i1.markdown('<a href="https://www.instagram.com/jazz__arts/" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/1384/1384031.png" alt="Instagram" width="30" height="30"></a>', unsafe_allow_html=True)
    i2.markdown('<a href="https://github.com/JayaanmolShah" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="Instagram" width="30" height="30"></a>', unsafe_allow_html=True)
    i3.markdown('<a href="https://www.linkedin.com/in/jayaanmol-shah-b36092230/" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/61/61109.png" alt="Instagram" width="30" height="30"></a>', unsafe_allow_html=True)

    st.header('')

    u1,u2=st.columns(2)
    u2.image('images/upeksha.jpeg')
    u1.markdown("<h4 style='color:#4cd4bc'>Upeksha Kohak</h4>", unsafe_allow_html=True)
    u1.header("")
    u1.write("I am a dedicated Computer Science student at AISSMS College of Engineering Pune, pursuing my BTech degree with a solid foundation in web development skills acquired through diploma  in Government Polytechnic pune. With hands-on experience in web development technologies, including HTML, CSS, JavaScript, and more.")
    o1,o2,o3=u1.columns(3)
    o1.markdown('<a href="https://www.instagram.com/jazz__arts/" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/1384/1384031.png" alt="Instagram" width="30" height="30"></a>', unsafe_allow_html=True)
    o2.markdown('<a href="https://github.com/JayaanmolShah" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="Instagram" width="30" height="30"></a>', unsafe_allow_html=True)
    o3.markdown('<a href="https://www.linkedin.com/in/jayaanmol-shah-b36092230/" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/61/61109.png" alt="Instagram" width="30" height="30"></a>', unsafe_allow_html=True)
    st.header('')

    r1,r2=st.columns(2)
    r1.image('images/raj.jpeg')
    r2.header("")
    r2.markdown("<h4 style='color:#4cd4bc'>Rajnandini Patil</h4>", unsafe_allow_html=True)
    r2.header("")
    r2.write("I am currently pursuing a Bachelor of Engineering degree at AISSMSCOE in Pune. Prior to this, I completed a diploma in Computer Engineering at ICRE Polytechnic. I am actively engaged in Android app development and concurrently studying web development.")
    p1,p2,p3=r2.columns(3)
    p1.markdown('<a href="https://www.instagram.com/jazz__arts/" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/1384/1384031.png" alt="Instagram" width="30" height="30"></a>', unsafe_allow_html=True)
    p2.markdown('<a href="https://github.com/JayaanmolShah" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="Instagram" width="30" height="30"></a>', unsafe_allow_html=True)
    p3.markdown('<a href="https://www.linkedin.com/in/jayaanmol-shah-b36092230/" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/61/61109.png" alt="Instagram" width="30" height="30"></a>', unsafe_allow_html=True)
    st.header('')

    m1,m2=st.columns(2)
    m2.image('images/iffa.jpeg')
    m1.header("")
    m1.markdown("<h4 style='color:#4cd4bc'>Shaikh Iffa</h4>", unsafe_allow_html=True)
    m1.header("")
    m1.write("I am Shaikh Iffa. Completed my diploma in Computer Engineering form JSPM'S polytechnic. Now studying B.E in Computer Engineering from AISSMS COE .Passionate about learning new technologies in technical field (Coding). Besides engineer I am a graphic designer (Digital Artist). Exploring about merging tech & creativity.")
    b1,b2,b3=m1.columns(3)
    b1.markdown('<a href="https://www.instagram.com/jazz__arts/" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/1384/1384031.png" alt="Instagram" width="30" height="30"></a>', unsafe_allow_html=True)
    b2.markdown('<a href="https://github.com/JayaanmolShah" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="Instagram" width="30" height="30"></a>', unsafe_allow_html=True)
    b3.markdown('<a href="https://www.linkedin.com/in/jayaanmol-shah-b36092230/" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/61/61109.png" alt="Instagram" width="30" height="30"></a>', unsafe_allow_html=True)
    st.header('')

def how_to_use_page():
    st.markdown("<h1 style='text-align: center;color:#c45c4c'>Welcome to Signext</h1>", unsafe_allow_html=True)
    st.subheader('where every gesture matters, and every voice is heard.')
    st.markdown("<h3 style='text-align: center;color:#c45c4c'>How to Use Signext</h3>", unsafe_allow_html=True)
    st.subheader('Learn how to interact with Signext to translate sign language to text.')

    st.write("1. **Enable Webcam:** Click on the 'Use Webcam' button to start using the webcam for gesture recognition.")
    st.write("2. **Gesture Recognition:** Once the webcam is enabled, make hand gestures in front of the camera. Signext will recognize your gestures and translate them into text.")
    st.image('images/alphabet.png')
    st.image('images/number.jpg')
    st.write("3. **Interpret Gestures:** Signext can recognize various gestures, such as numbers and letters in sign language. Perform these gestures clearly in front of the camera.")
    st.write("4. **View Translated Text:** As you perform gestures, Signext will display the corresponding text translation on the screen.")
    st.write("5. **Stop Gesture Recognition:** To stop gesture recognition, click the 'Stop Expressing' button.")

    st.header("Get Started")
    st.write("Ready to start expressing yourself? Head over to the 'Start Expressing' section to begin translating your sign language gestures into text.")

    st.header("Troubleshooting")
    st.write("Encountering issues or have questions about using Signext? Visit the 'About Us' section to learn more about our team and how to get in touch.")


def translate_page():
    st.title('Sign Language to Text')
    finger_tips = [8, 12, 16, 20]
    thumb_tip = 4
    use_webcam = st.sidebar.button('Use Webcam') 
    hell=st.sidebar.button("Stop Expressing")
    if use_webcam:
        vid = cv2.VideoCapture(0)
        stframe = st.empty()
        while hell:
            vid.release()
            cv2.destroyAllWindows()
        while not hell:
            ret, img = vid.read()
            img = cv2.flip(img, 1)
            h, w, c = img.shape
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hands.process(img)

            img.flags.writeable = True
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            if results.multi_hand_landmarks:
                for hand_landmark in results.multi_hand_landmarks:
                    lm_list = []
                    for id, lm in enumerate(hand_landmark.landmark):
                        lm_list.append(lm)
                    finger_fold_status = []
                    for tip in finger_tips:
                        x, y = int(lm_list[tip].x * w), int(lm_list[tip].y * h)
                        if lm_list[tip].x < lm_list[tip - 2].x:
                            finger_fold_status.append(True)
                        else:
                            finger_fold_status.append(False)

                    print(finger_fold_status)
                    x, y = int(lm_list[8].x * w), int(lm_list[8].y * h)
                    print(x, y)
                    # fuck off
                    if lm_list[3].x < lm_list[4].x and lm_list[8].y > lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                            lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                        cv2.putText(img, "fuck off !!!", (200, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        sameer="fuck off"

                    # one
                    if lm_list[3].x > lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y > lm_list[10].y and \
                            lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y and lm_list[4].y < lm_list[
                        12].y:
                        cv2.putText(img, "ONE", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        my_list.append("1")

                    # two
                    if lm_list[3].x > lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                            lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                        cv2.putText(img, "TWO", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        my_list.append("2")
                        sameer="two"
                    # three
                    if lm_list[2].x < lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                            lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                        cv2.putText(img, "THREE", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        my_list.append("3")
                        sameer="three"

                    # four
                    if lm_list[2].x > lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                            lm_list[16].y < lm_list[14].y and lm_list[20].y < lm_list[18].y and lm_list[2].x < lm_list[8].x:
                        cv2.putText(img, "FOUR", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        my_list.append("4")
                        sameer="Four"

                    # five
                    if lm_list[2].x < lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                            lm_list[16].y < lm_list[14].y and lm_list[20].y < lm_list[18].y and lm_list[17].x < lm_list[
                        0].x < \
                            lm_list[5].x:
                        cv2.putText(img, "FIVE", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        my_list.append("5")
                        sameer="Five"
                        # six
                    if lm_list[2].x > lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                            lm_list[16].y < lm_list[14].y and lm_list[20].y > lm_list[18].y and lm_list[17].x < lm_list[
                        0].x < \
                            lm_list[5].x:
                        cv2.putText(img, "SIX", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        my_list.append("6")
                        sameer="Six"
                    # SEVEN
                    if lm_list[2].x > lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                            lm_list[16].y > lm_list[14].y and lm_list[20].y < lm_list[18].y and lm_list[17].x < lm_list[
                        0].x < \
                            lm_list[5].x:
                        cv2.putText(img, "SEVEN", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        my_list.append("7")
                        sameer="Seven"
                    # EIGHT
                    if lm_list[2].x > lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y > lm_list[10].y and \
                            lm_list[16].y < lm_list[14].y and lm_list[20].y < lm_list[18].y and lm_list[17].x < lm_list[
                        0].x < \
                            lm_list[5].x:
                        cv2.putText(img, "EIGHT", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        my_list.append("8")
                        sameer="Eight"
                    # NINE
                    if lm_list[2].x > lm_list[4].x and lm_list[8].y > lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                            lm_list[16].y < lm_list[14].y and lm_list[20].y < lm_list[18].y and lm_list[17].x < lm_list[
                        0].x < \
                            lm_list[5].x:
                        cv2.putText(img, "NINE", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        my_list.append("9")
                        sameer="Nine"
                    # A
                    if lm_list[2].y > lm_list[4].y and lm_list[8].y > lm_list[6].y and lm_list[12].y > lm_list[10].y and \
                            lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y and lm_list[17].x < lm_list[
                        0].x < \
                            lm_list[5].x and lm_list[4].y < lm_list[6].y:
                        cv2.putText(img, "A", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        my_list.append("A")
                    # B
                    if lm_list[2].x > lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                            lm_list[16].y < lm_list[14].y and lm_list[20].y < lm_list[18].y and lm_list[2].x > lm_list[8].x:
                        cv2.putText(img, "B", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        my_list.append("B")
                        sameer="B"
                    # c
                    if lm_list[2].x < lm_list[4].x and lm_list[8].x > lm_list[6].x and lm_list[12].x > lm_list[10].x and \
                            lm_list[16].x > lm_list[14].x and lm_list[20].x > lm_list[18].x:
                        cv2.putText(img, "C", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        my_list.append("C")
                    # d
                    if lm_list[3].x > lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y > lm_list[10].y and \
                            lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y and lm_list[4].y > lm_list[8].y:
                        cv2.putText(img, "D", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        my_list.append("D")

                    # E
                    if lm_list[2].x > lm_list[4].x and lm_list[8].y > lm_list[6].y and lm_list[12].y > lm_list[10].y and \
                            lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y and lm_list[17].x < lm_list[
                        0].x < \
                            lm_list[5].x and lm_list[4].y > lm_list[6].y:
                        cv2.putText(img, "E", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        my_list.append("E")
                        
                    

                mp_draw.draw_landmarks(img, hand_landmark,mp_hands.HAND_CONNECTIONS,mp_draw.DrawingSpec((0, 0, 255), 6, 3),mp_draw.DrawingSpec((0, 255, 0), 4, 2))
                frame = cv2.resize(img, (0, 0), fx=0.8, fy=0.8)
                stframe.image(frame, channels='BGR', use_column_width=True)
                print(my_list)
        
    else:
        st.header("Waiting for you to enable Web-Cam")

if __name__ == '__main__':
    main()