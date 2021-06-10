def register_user(df_):
    name = widgets.Text(
    value='',
    placeholder='Type something',
    description='Name:',
    disabled=False
    )
    gender = widgets.RadioButtons(
    options=['Male', 'Female'],
    description='Gender',
    disabled=False
    )
    date = widgets.DatePicker(
    description='date of birth',
    disabled=False
    )
    name_of_area = widgets.Text(
    value='',
    placeholder='Type something',
    description='Locality:',
    disabled=False
    )
    URL = "https://geocode.search.hereapi.com/v1/geocode"
    api_key = 'sO0hb7sykYZPwb-O8Y2PBv3w7bpy69IKrPmbPBxIRcU' # Acquire from developer.here.com
    PARAMS = {'apikey':api_key,'q':location} 

    # sending get request and saving the response as response object 
    r = requests.get(url = URL, params = PARAMS) 
    data = r.json()
    latitude = data['items'][0]['position']['lat']
    longitude = data['items'][0]['position']['lng']
    postal_code = data['items']
    
    
    flexibility = widgets.IntSlider(
    value=2,
    min=1,
    max=5,
    step=1,
    description='Flexibilty',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
    )
    body_composition = widgets.Dropdown(
    options=['Acceptable', 'Athletes', 'Obese', 'Essential Fat', 'Fitness'],
    value='Acceptable',
    description='Body Composition:',
    disabled=False,
    )
    composition_percentage = widgets.IntSlider(
    min=1,
    max=100,
    step=1,
    description='Composition Percentage:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
    )
    interactiveness = widgets.IntSlider(
    value=2,min=1, max=5,step=1, description='Interactiveness :', disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
    )
    workout_frequency = widgets.Dropdown(
    options=['Monday To Friday', '3 days of week', 'Alternate Days', 'Any Day of Week', 'Daily','Only Weekends'],
    description='Workout Frequency:',
    disabled=False,
    )
    workout_mode = widgets.Dropdown(
    options=['Outdoor', 'Indoor', 'Both'],
    description='Workout Mode Preferred:',
    disabled=False,
    )
    is_sport_enthusiast = widgets.RadioButtons(
    options=['Yes', 'No', 'Maybe'],
    description='Are You Sports Enthusiast',
    disabled=False
    )
    like_to_be_mentored = widgets.IntSlider(
    min=1, max=5,step=1, description='Do You Like to be mentored? :', disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
    )
    like_to_mentor = widgets.IntSlider(
    min=1, max=5,step=1, description='Do You Like to mentor? :', disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
    )
    fitness_Goal = widgets.RadioButtons(
    options=['All', 'Improve endurance/conditioning', 'Improve athletic skills', 'Lose fat', 'Mesomorph'],
    description='Fitness Goal?',
    disabled=False
    )
    addon_session = widgets.RadioButtons(
    options=['Meditation', 'Yoga', 'Both', 'None'],
    description='Addon Session required?',
    disabled=False
    )
    height = widgets.IntSlider(
    value=160,min=160, max=180,step=1, description='Height in centimeters:', disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
    )
    display(name, gender,date, name_of_area,flexibility,body_composition,composition_percentage,interactiveness,workout_frequency, workout_mode, is_sport_enthusiast,like_to_be_mentored,like_to_mentor, fitness_Goal,addon_session,height)
    
    print(name_of_area)
    
enter_data = widgets.Button(
    description='Submit',
    disabled=False,
    button_style='success', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Click me',
    icon='check' # (FontAwesome names without the `fa-` prefix)
    
#     value=0
)
display(enter_data)
