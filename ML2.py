import streamlit as st
import time as t
import requests
from streamlit_lottie import st_lottie
import json
import pickle
import numpy as np
import time
import random




def main():
    def load_lottie(filepath):
        with open(filepath, "r") as f:
            return json.load(f)

    #page title and icon with message
    st.set_page_config(page_title="MACHINE LEARNING MODEL",page_icon=":stethoscope:",layout="wide")
    
    st.title(":green[WELCOME TO SELF PREDICTORY ANALYSIS]")
    #st.markdown(" ##### :orange[(*click ' > ' for options*)] ")
    lottie_hello = load_lottie("hello_boy.json")
    st_lottie(lottie_hello,height=300,width=300,speed=1,reverse=True)
    #st.header(" :blue[MEASURE YOUR HEART STATISTICS AS WELL AS DIABETES STATISTICS USING THIS MACHINE LEARNING MODEL] ")
    
    #st.image("ML_PIC - Copy.png",width = 350)
    #st.write(":orange[]")
    #to give user info
    st.caption(" :black[_THIS WEBSITE HAS BEEN DEVELOPED AND MANAGED BY SOURABH DEY_] ")
    def load_lottie(filepath):
        with open(filepath, "r") as f:
            return json.load(f)

    t1, t2 = st.tabs([":red[ ❤️ Heart Disease Predction]",":blue[ 💉 DIABETES PREDICTION]"])

    with t1:
        main_heart()
    with t2:
        main_diabetes()
        
    
    #st.sidebar.title(""" :violet[CHOOSE YOUR PREDICTORY MODEL]  """)
    #st.sidebar.image("hello_robotic.jpg",width = 180)
    #st.sidebar.markdown("### :orange[(* ***type anything in anyone of the blank boxes below to proceed with your desired predictive model*** *)]\n")
    #if st.sidebar.button(":red[HEART DISEASE PREDICTION]"):
        #st.sidebar.markdown(" ##### :orange[(*click on 'X', then scroll down*)] ")
        #st.sidebar.markdown(" ##### :orange[(*after getting your data,press backspace and then enter to go back*)] ")
        #main_heart()
    #elif st.sidebar.button(":blue[DIABETES PREDICTION]"): 
        #st.sidebar.markdown(" ##### :orange[(*click on 'X', then scroll down*)] ")
        #st.sidebar.markdown(" ##### :orange[(*after getting your data,press backspace and then enter to go back*)] ")
        #main_diabetes()
    

    #if st.button(" ##### :orange[(*click here for going back*)] "):
        #with st.expander(" ##### :orange[(*click me*)]"):
            #st.markdown("##### :orange[(*click ' > ' for options*)]")
            #st.sidebar.header(" :red[(*press backspace and then enter to go back*)] ")
    #else:
        #pass


    if t1 or t2:
        st.file_uploader("UPLOAD SUPPORTING MEDICAL DATA FOR YOUR ABOVE GIVEN DETAILS")
    else:
        pass
    
    #about the developer
    with st.expander("CONTACT THE DEVELOPER"):
        st.write(" [LEARN MORE ABOUT THE DEVELOPER >](https://sourabh-dey-resume.streamlit.app/)")
        st.image("profile-pic (6).png",width = 250)
        contact = """ <form action="https://formsubmit.co/uhddey@gmail.com" method="POST">
                 <input type="text" name="name" placeholder = "YOUR NAME" required>
                 <input type="email" name="email" placeholder = "YOUR EMAIL" required>
                 <textarea name="message" placeholder="Tell us your problem" required></textarea>
                 <button type="submit">Send</button>
            </form>  """

        
        st.markdown(contact, unsafe_allow_html=True)
    



#funtion where the machine learning predction happens for diabetes
def predict_diabetes(input_data_D):
    #loading the diabetes data saved model
    loaded_model_2 = pickle.load(open("D_trained_model.sav","rb"))

    # Making user-based predictions
    #input_data = (1,113,98,32,87,34.4,0.617,63)
    # For ease, we will convert this data to a numpy array
    input_data_array = np.asarray(input_data_D)
    # Reshaping the array to give only one data instance
    reshaped_input = input_data_array.reshape(1, -1)

    #standardizing the input data
    #std_data = scaler.transform(reshaped_input)
    #print(std_data)

    prediction = loaded_model_2.predict(reshaped_input)


    if prediction[0] == 0:
        st.success('DOES NOT HAVE DIABETES')
        st.balloons()
    elif prediction[0] == 1:
        st.warning('MAY HAVE DIABETES')






#function for taking input from the users in the web for diabetes prediction data
def main_diabetes():
    def load_lottie(filepath):
        with open(filepath, "r") as f:
            return json.load(f)

    lottie_diabetes_animate = load_lottie("animation_lkfl0fus.json")

    
    #title
    st.title(" :violet[ 💉 WELCOME TO DIABETES PREDICTION MODEL]  " )
    #image addtion
    #st.image("DiabetesPredictioninMachineLearningusingPython20220505114933 - Copy.jpg")

                #header file
    st.header(" :blue[Get your diabetes data monitored here ] ")
    st_lottie(lottie_diabetes_animate,height=300,width=300,speed=1,reverse=True)


    st.caption(" #### :violet[*WITHOUT SUGAR, YOU ARE STILL SWEET*] ")



            

                


    st.subheader(":green[ENTER YOUR HEALTH DETAILS HERE]")
            #WARNING MESSAGE
    st.warning("""  ----- NOTE  -----  \n ENTER DETAILS CORRECTLY FOR ACCURATE EVALUATION OF THE RESULTS, OTHERWISE THE MODEL WILL GENERATE FALSE RESULTS WHICH MAY NOT BE APPROPRIATE """)

            

    a = st.radio("GENDER",["MALE","FEMALE"])

                
                    

    #taking user input
    if a == "MALE":
        Pregnancies = 0
    elif a == "FEMALE":
        Pregnancies = st.slider("Number of pregnancies",0,10)

                    
                
    Glucose = st.number_input("Your Fasting Blood Sugar Level(mg/dl):  ")
    with st.expander("TAP TO KNOW MORE"):
        st.write(":green[_A normal fasting blood sugar level is usually considered to be between 70 and 99 milligrams per deciliter (mg/dL)_]")
                
    BloodPressure = st.number_input("Your Resting Blood Pressure(mm Hg): ")
    with st.expander("TAP TO LEARN MORE"):
        st.write("""The general range for resting blood pressure is typically measured in millimeters of mercury (mm Hg) and is categorized as follows:
                                                    \n
        - Normal : Systolic (top number) less than 120 mm Hg and diastolic (bottom number) less than 80 mm Hg.
        - Elevated : Systolic between 120-129 mm Hg and diastolic less than 80 mm Hg.
        - Hypertension Stage 1 : Systolic between 130-139 mm Hg or diastolic between 80-89 mm Hg.
        - Hypertension Stage 2 : Systolic 140 mm Hg or higher or diastolic 90 mm Hg or higher.
        - Hypertensive Crisis :  Systolic higher than 180 mm Hg and/or diastolic higher than 120 mm Hg.""")
                    
            #SkinThickness = st.number_input(" Your Skinfold Thickness (mm): ")
            #with st.expander(" WHAT IS SKIN FOLD THICKNESS? "):
                #st.write(""" :orange[Skinfold thickness refers to the amount of fat under the skin.
                            #It's often measured at specific body sites to estimate body fat.]\n
                            
                                                        #\t__NOTE__\t
                           # \n
        #:red[It is advisable to go to medical professional who will measure it using a skinfold caliper]
                #\n
                            
        # :blue[To measure at home, gently pinch skin between thumb and forefinger, then measure the pinched area's width with a ruler or caliper.
        # Keep in mind, professional assessments are more accurate]""")
                
    Insulin = st.number_input("Your Insulin Level after 2 Hours (mu U/ml): ")
    with st.expander("TAP TO KNOW MORE ABOUT INSULIN LEVEL AFTER 2 HOURS"):
        st.write(""" :green[_Insulin Level after 2 Hours" refers to the measurement of insulin concentration
                            in the blood two hours after a particular event,such as consuming a meal or undergoing a test.
                            This measurement helps assess the body's response to glucose metabolism over time and
                            can provide insights into insulin sensitivity and diabetes risk._]
                            """)

        st.write("""    *HOW IT IS DIFFERENT FROM POST MEAL BLOOD SUGAR LEVEL*? """)
        st.write("""  :blue[_Insulin Level after 2 Hours" checks how insulin reacts to sugar in the blood after 2 hours.
            "Post-Meal Blood Sugar Level" measures sugar concentration in the blood after eating.
            Both help evaluate glucose control and diabetes risk_]""")  
        st.write(":red[_for simplicity you can add your post meal blood sugar level_]")
                
    weight = st.number_input("Enter your weight in kgs: ",2,200)
                
    height = st.number_input("Enter your height in centimetres: ",20,300)
    Height = height/100
    BMI = (weight)/(Height*Height)
    with st.expander(" CHECK YOUR BMI "):
        st.write("YOUR BMI IS",BMI)

    diabetes_history = st.radio("DOES YOUR FAMILY HAVE A HISTORY OF DIABETES ?",["YES","NO"])
    if diabetes_history == "YES":
        DiabetesPedigreeFunction = random.uniform(0.5,0.9)
    elif diabetes_history == "NO":
        DiabetesPedigreeFunction = 0
                                                                                         
                
            #DiabetesPedigreeFunction = st.slider("Your Family Diabetes History Score:  ",0.0,1.0,0.001)
            #with st.expander(" KNOW MORE "):
           #     st.write(""":orange[_Think of the this as a score that shows how much your family's history of diabetes might affect your own risk.
        #If the score is higher, it means there's a stronger chance that diabetes runs in your family, which could increase your own risk.
        #It's a way to see how family history might play a role in your health_]""")
                
    Age = st.number_input("ENTER YOUR AGE: ",1,101)

    SkinThickness = 10
    if a == "MALE":  # Male
        if Age >= 1 and Age <= 9:
            SkinThickness = random.uniform(5.0,12.1)
        elif Age >= 10 and Age <= 13:
            SkinThickness = random.uniform(6.0,15.1)
        elif Age >= 14 and Age <= 17:
            SkinThickness = random.uniform(8.0,18.1)
        elif Age >= 18 and Age <= 29:
            SkinThickness = random.uniform(5.5, 10.6)
        elif Age >= 30 and Age <= 59:
            SkinThickness = random.uniform(7.0, 12.6)
        elif Age >= 60:
            SkinThickness = random.uniform(9.0, 14.2)


            
    elif a == "FEMALE":  # Female
        if Age >= 1 and Age <= 9:
            SkinThickness = random.uniform(5.0,13.1)
        elif Age >= 10 and Age <= 13:
            SkinThickness = random.uniform(7.0,16.1)
        elif Age >= 14 and Age <= 17:
            SkinThickness = random.uniform(9.0,20.1)
        elif Age >= 18 and Age <= 29:
            SkinThickness = random.uniform(11.0, 18.6)
        elif Age >= 30 and Age <= 59:
            SkinThickness = random.uniform(12.5, 21.2)
        elif Age >= 60:
            SkinThickness = random.uniform(14.5, 23.3)
                
    if Age == None:
        Age = 20
        
                

            #code for prediction
            #diagnosis = " "

            #prediction button
    if st.button('DIABETES DATA Test Result'):
        diagnosis = predict_diabetes([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
    with st.spinner(" WAIT FOR A WHILE "):
        t.sleep(3)

    #st.success(diagnosis)
    #pass
    #error message
    #st.error(" ONE SHOULD NOT PLAY WITH THIS WEBSITE ")

    #SUCCESS MESSAGE
    #st.file_uploader("UPLOAD SUPPORTING MEDICAL DATA FOR YOUR ABOVE GIVEN DETAILS")
    

#funtion where the machine learning predction happens for diabetes
def pred_heart_dis(input_data):
    #loading the saved model
    loaded_model = pickle.load(open("H_trained_model.sav","rb"))
    # Making user-based predictions
    #input_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    # For ease, we will convert this data to a numpy array
    input_data_array = np.asarray(input_data)
    # Reshaping the array to give only one data instance
    reshaped_input = input_data_array.reshape(1, -1)
    #standardizing the input data
    #std_data = scaler.transform(reshaped_input)
    prediction = loaded_model .predict(reshaped_input)
    

    if prediction[0] == 0:
        st.success('DOES NOT HAVE HEART DISEASE RISK')
        st.snow()
    elif prediction[0] == 1:
        st.warning('MAY HAVE A HEART DISEASE RISK')





    
#function for taking input from the users in the web for heart disease predciton data
def main_heart():
    def load_lottie(filepath):
        with open(filepath, "r") as f:
            return json.load(f)

    #function to store lottie varible

    lottie_heart_animate = load_lottie("HEART.json")

    #page title and icon with message
    #st.set_page_config(page_title="HEART DISEASE PREDICTION MODEL",page_icon=":mending_heart:",layout="wide")
    #title
    st.title(" :red[ ❤ WELCOME TO HEART DISEASE PREDICTION MODEL] " )
    #image addtion
    #st.image("Machine-Learning-Project-on-Heart-Disease-Prediction.webp")

    #header file
    st.header(" :violet[Get your heart data monitored here] ")
    st_lottie(lottie_heart_animate,height=300,width=300,speed=1,reverse=True)

    #to give user info
    #st.info(" THIS WEBSITE HAS BEEN DEVELOPED AND MANAGED BY SHRABONI DEY")
    #adding an mathematical expression
    st.caption(":orange[*exercise + balanced  diet = healthy  heart*]")





    st.subheader(":green[ENTER YOUR HEALTH DETAILS HERE]")

    #WARNING MESSAGE
    st.warning("""  :white[----- NOTE  -----  \n ENTER DETAILS CORRECTLY FOR ACCURATE EVALUATION OF THE RESULTS, OTHERWISE THE MODEL WILL GENERATE FALSE RESULTS WHICH MAY NOT BE APPROPRIATE] """)
    
    #age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal
    #taking user inputs
    age = st.number_input(" Enter your age ")#age
    
    sex = 0
    GENDER = st.radio("GENDER ",["MALE","FEMALE"])#sex
    if GENDER == "MALE":
        sex = 1
    elif GENDER== "FEMALE":
        sex = 0
    
    cp = st.radio("Chest pain experienced(Value 1: typical angina, Value 2: atypical angina, Value 3: non-anginal pain, Value 4: asymptomatic)",[1,2,3,4])#cp
    trestbps = st.number_input("Your resting blood pressure (mm Hg on admission to the hospital)")#trestbps
    chol = st.number_input("Your cholesterol measurement in mg/dl")#chol
    
    fbs = st.radio("Your fasting blood sugar, if it is > 120 mg/dl then type 1 or else type 0 if < 120 mg/dl",[1,0])#fbs
    restecg = st.radio("Your Resting electrocardiographic measurement (0 = normal, 1 = having ST-T wave abnormality, 2 = showing probable or definite left ventricular hypertrophy by Estes' criteria)",[0,1,2])#restecg
    thalach = st.slider("Your maximum heart rate achieved",60,180)#thalach
    
    exang = st.radio("Exercise induced angina (1 = yes; 0 = no)",[0,1])#exang
    oldpeak = st.number_input("ST depression induced by exercise relative to rest ('ST' relates to positions on the ECG plot)")#oldpeak
    slope = st.radio("The slope of the peak exercise ST segment (Value 1: upsloping, Value 2: flat, Value 3: downsloping)",[1,2,3])#slope
   
    ca = st.radio("The number of major vessels (0-4):",[0,1,2,3,4])#ca
    
    thal = st.radio("Thalassemia value (A blood disorder)(3 = normal; 6 = fixed defect; 7 = reversible defect)",[0,1,2,3,4,5,6,7])#thal
    

 

    #code for prediction
    #diagnosis = " "

    #prediction button
    if st.button('HEART DISEASE Test Result'):
        diagnosis = pred_heart_dis([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
    with st.spinner(" WAIT FOR A WHILE "):
        t.sleep(3)


    #st.success(diagnosis)

    


    #error message
    #st.error(" ONE SHOULD NOT PLAY WITH THIS WEBSITE ")

    #SUCCESS MESSAGE
    #st.file_uploader("UPLOAD SUPPORTING MEDICAL DATA FOR YOUR ABOVE GIVEN DETAILS")
    
    
    



if __name__ == "__main__":
    main()
